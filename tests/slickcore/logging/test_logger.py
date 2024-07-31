from assertpy import assert_that

from slickcore.logging._logger import foo


def test_foo() -> None:
    assert_that(foo()).is_equal_to(42)
