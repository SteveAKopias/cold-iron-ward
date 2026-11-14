import pytest


def test_gate_test_is_skipped_without_gate_flag(pytester: pytest.Pytester) -> None:
    specimen = pytester.copy_example("gate_passing.py")

    result = pytester.runpytest(
        "-p", "support.gate_plugin", "--report-chars=s", specimen
    )
    result.assert_outcomes(skipped=1)
    result.stdout.fnmatch_lines(["*SKIPPED*--gate*"])
