import subprocess

from assertpy import assert_that

from slickcore import __version__


def test_version() -> None:
    """Validates the current version."""
    expected = subprocess.check_output(
        args=(
            "poetry",
            "version",
        ),
        text=True,
    )
    actual = _poetry_version(
        version=__version__,
    )

    assert_that(expected).is_equal_to(actual)


def _poetry_version(version: str) -> str:
    """Creates `poetry` version."""
    return f"slickcore {version}\n"
