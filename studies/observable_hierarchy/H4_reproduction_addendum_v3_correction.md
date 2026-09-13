# Correction to the H4 reproduction correspondence addendum v3

The frozen addendum's sentence “The original code-only edition has no `code/README.md`” is incorrect as a statement about the current directory. The precise statement is:

> The original executed edition manifest has no `code/README.md` entry. The current original-edition directory does contain that path. The addendum's own static record already reports `original_guide_absent: false`. No original-guide content was read or used, and no original/final guide byte comparison was performed.

I independently rechecked the original manifest's membership, the existing static record and the path's existence/size. The path currently exists and is 61,678 bytes. These checks did not read its contents or establish when it was added.

This corrects only the directory-absence wording. The direct comparison of all 25 originally manifested code/test/plan files, the 23 byte-identical files, the two inspected test-text differences, and the runtime/plan correspondence are unaffected. No tests, trajectories or experiments were run.

The original reproduction report, frozen addendum and existing records remain unchanged. The frozen addendum retains SHA-256 `7df71242fc718a679d877a25806d7506a4cceceba71dd33d5b413f916a0e5ed7`; this separate correction supersedes only the quoted absence statement and any inference from it that the current old-edition guide path is absent.
