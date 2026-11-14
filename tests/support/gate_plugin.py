import pytest


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    skip_gate = pytest.mark.skip(
        reason="acceptance gate test: run with --gate on the target host"
    )

    for item in items:
        if item.get_closest_marker("gate") is not None:
            item.add_marker(skip_gate)
