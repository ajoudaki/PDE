"""Restore one damaged frozen-basis ZIP member from five identical saved copies.

No array arithmetic or training. Preserve the original archive and every byte
outside the damaged uncompressed member. Fail unless donor bytes match the
original member's declared size/CRC and all five independent saved copies.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import struct
import sys
import zipfile
import zlib


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    base = Path(__file__).resolve().parents[2] / "data/generated/random_dictionary_learned_circle_20260920"
    target = base / "scaling_confirm2_refined01/outliers_confirm2_ours_p9/arrays.npz"
    out = base / "scaling_archive_repair01"
    out.mkdir(exist_ok=False)
    original = target.read_bytes()
    backup = out / "original_corrupt_arrays.npz"
    backup.write_bytes(original)
    assert backup.read_bytes() == original
    member = "b1.npy"
    donors, copies = [], []
    for root in ("scaling_confirm2_primary01", "scaling_confirm2_refined01"):
        for case in ("pairs_confirm2", "outliers_confirm2", "negative_confirm2"):
            path = base / root / (case + "_ours_p9") / "arrays.npz"
            if path == target:
                continue
            raw = path.read_bytes()
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                assert archive.testzip() is None
                payload = archive.read(member)
            copies.append(payload)
            donors.append(dict(path=str(path), archive_sha256=digest(raw), member_sha256=digest(payload)))
    assert len(copies) == 5 and all(payload == copies[0] for payload in copies)
    payload = copies[0]
    with zipfile.ZipFile(io.BytesIO(original)) as archive:
        failures = []
        for item in archive.infolist():
            try:
                archive.read(item.filename)
            except zipfile.BadZipFile:
                failures.append(item.filename)
        assert failures == [member], failures
        info = archive.getinfo(member)
        assert info.compress_type == zipfile.ZIP_STORED and not (info.flag_bits & 1)
        assert len(payload) == info.file_size == info.compress_size
        assert zlib.crc32(payload) == info.CRC
        fields = struct.unpack_from("<IHHHHHIIIHH", original, info.header_offset)
        assert fields[0] == 0x04034B50
        start = info.header_offset + 30 + fields[-2] + fields[-1]
        end = start + len(payload)
        assert original[info.header_offset + 30:info.header_offset + 30 + fields[-2]] == member.encode()
    damaged = original[start:end]
    changed = [i for i, (a, b) in enumerate(zip(damaged, payload)) if a != b]
    assert changed
    repaired = original[:start] + payload + original[end:]
    assert len(repaired) == len(original)
    assert repaired[:start] == original[:start] and repaired[end:] == original[end:]
    with zipfile.ZipFile(io.BytesIO(repaired)) as archive:
        assert archive.testzip() is None
        assert archive.read(member) == payload
    record = dict(
        command=[sys.executable, "-B", *sys.argv], source_sha256=digest(Path(__file__).read_bytes()),
        target=str(target), preserved_original=str(backup), original_sha256=digest(original),
        repaired_sha256=digest(repaired), member=member, member_sha256=digest(payload),
        expected_crc32=info.CRC, damaged_actual_crc32=zlib.crc32(damaged),
        member_offset=start, member_size=len(payload), donors=donors,
        changed_byte_count=len(changed), changed_bit_count=sum((damaged[i] ^ payload[i]).bit_count() for i in changed),
        changed_member_offsets=changed, all_other_archive_bytes_identical=True,
        no_training_or_scientific_array_recomputation=True,
        qualification="Cause of corruption unknown. Restored frozen basis from five unanimous same-initialization copies matching original CRC; replay audit still required.")
    (out / "repair.json").write_text(json.dumps(record, indent=2) + "\n")
    temporary = out / "repaired_arrays.npz"
    temporary.write_bytes(repaired)
    assert digest(temporary.read_bytes()) == record["repaired_sha256"]
    os.replace(temporary, target)
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
