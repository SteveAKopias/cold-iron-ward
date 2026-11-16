import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--gate",
        action="store_true",
        default=False,
        help="run acceptance gate tests on the target host",
    )


def pytest_collection_modifyitems(
    items: list[pytest.Item], config: pytest.Config
) -> None:
    gate_enabled = config.getoption("--gate")
    skip_gate = pytest.mark.skip(
        reason="acceptance gate test: run with --gate on the target host"
    )

    if not gate_enabled:
        for item in items:
            if item.get_closest_marker("gate") is not None:
                item.add_marker(skip_gate)
