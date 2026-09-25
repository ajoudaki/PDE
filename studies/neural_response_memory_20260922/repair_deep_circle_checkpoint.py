"""Recover one verified checkpoint bit from the redundant valid terminal state.

This narrow repair is specific to the recorded corrupt quadrant-pairs dense
checkpoint. Original files are opened read-only and remain unchanged. All
other replay-view files are symlinks; only the copied summary's checkpoint
hash changes. No dynamics, metrics, or floating-point computation is rerun.
"""

import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import struct
import sys
import zipfile
import zlib

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "data/generated/neural_response_memory_20260922/deep_circle_primary01/runs/16_quadrant_pairs_dense_rtol1.25e-05"
CHECKPOINT = "checkpoint_loss_0p001.npz"
ORIGINAL_SHA256 = "858d50a62ad9be4953c3848c53f680903bae58430ba41aae7fc978fb280742e2"
FINAL_SHA256 = "be37d8ca5a12c8bca1007839864b9db26eaec6b1b9369da54737ac896a008402"
EXPECTED_WORD_INDEX = 14205696
EXPECTED_ORIGINAL_WORD = 0xBF8DBF86B3A6A13B
EXPECTED_FINAL_WORD = 0xBF8DBF86F3A6A13B


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            result.update(chunk)
    return result.hexdigest()


def identical(left, right):
    left, right = np.asarray(left), np.asarray(right)
    return left.shape == right.shape and left.dtype == right.dtype and left.tobytes(order="C") == right.tobytes(order="C")


def repair(output):
    original, terminal = RUN / CHECKPOINT, RUN / "arrays.npz"
    assert digest(original) == ORIGINAL_SHA256
    assert digest(terminal) == FINAL_SHA256
    summary = json.loads((RUN / "summary.json").read_text())
    assert summary["checkpoint_sha256"][CHECKPOINT] == ORIGINAL_SHA256
    assert summary["arrays_sha256"] == FINAL_SHA256
    with zipfile.ZipFile(original) as archive:
        assert archive.testzip() == "W3.npy"
        info = archive.getinfo("W3.npy")
        assert info.compress_type == zipfile.ZIP_STORED
    with zipfile.ZipFile(terminal) as archive:
        assert archive.testzip() is None
    with original.open("rb") as stream:
        stream.seek(info.header_offset)
        header = struct.unpack("<IHHHHHIIIHH", stream.read(30))
        assert header[0] == 0x04034B50 and header[3] == zipfile.ZIP_STORED
        assert header[6] == info.CRC
        member_offset = info.header_offset + 30 + header[-2] + header[-1]
        stream.seek(member_offset)
        raw_member = bytearray(stream.read(info.compress_size))
    old_crc = zlib.crc32(raw_member) & 0xFFFFFFFF
    assert old_crc != info.CRC
    decoded = np.lib.format.read_array(io.BytesIO(raw_member), allow_pickle=False)
    with np.load(terminal, allow_pickle=False) as final:
        reference = final["W3"]
        assert decoded.shape == reference.shape == (4096, 4096)
        assert decoded.dtype == reference.dtype == np.dtype("float64")
        assert decoded.flags.c_contiguous and reference.flags.c_contiguous
        differences = np.flatnonzero(decoded.ravel().view(np.uint64) != reference.ravel().view(np.uint64))
        assert differences.tolist() == [EXPECTED_WORD_INDEX]
        old_word = int(decoded.ravel().view(np.uint64)[EXPECTED_WORD_INDEX])
        new_word = int(reference.ravel().view(np.uint64)[EXPECTED_WORD_INDEX])
        assert old_word == EXPECTED_ORIGINAL_WORD and new_word == EXPECTED_FINAL_WORD
        xor = old_word ^ new_word
        assert xor and not (xor & (xor - 1)), "the discrepancy must be exactly one bit"
        with np.load(original, allow_pickle=False) as checkpoint:
            assert set(checkpoint.files) == {"w", "W2", "W3", "c", "physical_time", "training_mse"}
            intact_fields = {}
            for key in checkpoint.files:
                if key == "W3":
                    continue
                wanted = np.asarray(final["losses"][-1]) if key == "training_mse" else final[key]
                intact_fields[key] = identical(checkpoint[key], wanted)
            assert all(intact_fields.values())
        payload_offset = len(raw_member) - decoded.nbytes
        word_offset = payload_offset + EXPECTED_WORD_INDEX * 8
        old_bytes = bytes(raw_member[word_offset:word_offset + 8])
        new_bytes = reference.ravel()[EXPECTED_WORD_INDEX:EXPECTED_WORD_INDEX + 1].tobytes()
        changed_bytes = [index for index, (a, b) in enumerate(zip(old_bytes, new_bytes)) if a != b]
        assert len(changed_bytes) == 1
        byte_in_word = changed_bytes[0]
        assert (old_bytes[byte_in_word] ^ new_bytes[byte_in_word]).bit_count() == 1
        raw_member[word_offset:word_offset + 8] = new_bytes
        restored_crc = zlib.crc32(raw_member) & 0xFFFFFFFF
        assert restored_crc == info.CRC, "redundant final-state bit must restore the original recorded CRC"
        assert identical(np.lib.format.read_array(io.BytesIO(raw_member), allow_pickle=False), reference)

    output = Path(output).resolve()
    allowed = ROOT / "data/generated/neural_response_memory_20260922"
    assert output.is_relative_to(allowed) and output != allowed
    output.mkdir(parents=True, exist_ok=False)
    recovered = output / CHECKPOINT
    shutil.copyfile(original, recovered)
    absolute_byte_offset = member_offset + word_offset + byte_in_word
    with recovered.open("r+b") as stream:
        stream.seek(absolute_byte_offset)
        assert stream.read(1) == old_bytes[byte_in_word:byte_in_word + 1]
        stream.seek(absolute_byte_offset)
        stream.write(new_bytes[byte_in_word:byte_in_word + 1])
    with zipfile.ZipFile(recovered) as archive:
        assert archive.testzip() is None
    with np.load(recovered, allow_pickle=False) as checkpoint, np.load(terminal, allow_pickle=False) as final:
        for key in checkpoint.files:
            wanted = np.asarray(final["losses"][-1]) if key == "training_mse" else final[key]
            assert identical(checkpoint[key], wanted)
    recovered_hash = digest(recovered)
    assert digest(original) == ORIGINAL_SHA256 and digest(terminal) == FINAL_SHA256

    view = output / "run_view"
    view.mkdir()
    for path in sorted(RUN.iterdir()):
        if path.name == "summary.json":
            continue
        (view / path.name).symlink_to(recovered if path.name == CHECKPOINT else path.resolve(), target_is_directory=path.is_dir())
    updated = json.loads((RUN / "summary.json").read_text())
    updated["checkpoint_sha256"][CHECKPOINT] = recovered_hash
    (view / "summary.json").write_text(json.dumps(updated, indent=2) + "\n")
    for key in summary:
        if key != "checkpoint_sha256":
            assert updated[key] == summary[key]
    assert {key: value for key, value in updated["checkpoint_sha256"].items() if key != CHECKPOINT} == {
        key: value for key, value in summary["checkpoint_sha256"].items() if key != CHECKPOINT}

    manifest = dict(status="PASS", original_run=str(RUN), original_checkpoint=str(original),
        original_checkpoint_sha256=ORIGINAL_SHA256, redundant_final=str(terminal), redundant_final_sha256=FINAL_SHA256,
        recovered_checkpoint=str(recovered), recovered_checkpoint_sha256=recovered_hash, replay_view=str(view),
        original_summary_sha256=digest(RUN / "summary.json"), replay_summary_sha256=digest(view / "summary.json"),
        summary_changed_field="checkpoint_sha256." + CHECKPOINT, member="W3.npy", word_index=EXPECTED_WORD_INDEX,
        original_word=hex(old_word), restored_word=hex(new_word), xor_mask=hex(xor),
        absolute_changed_byte_offset=absolute_byte_offset, original_byte=old_bytes[byte_in_word], restored_byte=new_bytes[byte_in_word],
        original_computed_crc=hex(old_crc), original_recorded_crc=hex(info.CRC), restored_computed_crc=hex(restored_crc),
        intact_fields_equal_terminal=intact_fields, recovered_all_fields_equal_terminal=True,
        originals_unchanged=True, source_sha256=digest(__file__), command=sys.argv, numpy=np.__version__)
    (output / "repair_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest), flush=True)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    repair(parser.parse_args().out)
