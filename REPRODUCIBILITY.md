# Reproduce the checks

Use an existing Python 3.11 or compatible interpreter. Both scripts use the standard library.

    python3 -B -I scripts/verify_repository.py
    python3 -B -I verification/src/replay.py

The replay checks repeated parallel rounds and exact first-attainment costs. Matrix controls include positive self-paths, loops and missing edges, with no empty path contributing to the positive-length value.

Use Lean 4.30.0 with its bundled standard library for the partial certificate.

    lean -DwarningAsError=true formal/Q1078Certificate.lean

The certificate proves a Boolean identity, strict adjacent cost improvement, the small path trace and the plus-gate threshold identities for natural numbers. Infinity gates and matrix comparisons are included in the separate Python controls. The circuit lower bound and general program argument remain written proofs. [Paper build](paper/BUILD.md) · [Illustration](visualization/README.md)
