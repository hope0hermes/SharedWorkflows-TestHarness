"""Tests that should pass - for validating CI/CD workflows."""

import pytest

from testharness import __version__, hello


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_hello_function() -> None:
    """Test the hello function returns expected message."""
    result = hello()
    assert result == "Hello from SharedWorkflows Test Harness!"
    assert isinstance(result, str)


def test_basic_math() -> None:
    """Test basic arithmetic operations."""
    assert 1 + 1 == 2
    assert 2 * 3 == 6
    assert 10 / 2 == 5


def test_string_operations() -> None:
    """Test string manipulation."""
    test_string = "hello world"
    assert test_string.upper() == "HELLO WORLD"
    assert test_string.split() == ["hello", "world"]
    assert "hello" in test_string


def test_list_operations() -> None:
    """Test list operations."""
    test_list = [1, 2, 3, 4, 5]
    assert len(test_list) == 5
    assert sum(test_list) == 15
    assert max(test_list) == 5
    assert min(test_list) == 1


def test_dict_operations() -> None:
    """Test dictionary operations."""
    test_dict = {"name": "test", "value": 42}
    assert test_dict["name"] == "test"
    assert test_dict["value"] == 42
    assert "name" in test_dict
    assert len(test_dict) == 2


@pytest.mark.unit
def test_with_marker() -> None:
    """Test with unit marker."""
    assert True


def test_with_fixture(sample_message: str, sample_number: int) -> None:
    """Test using fixtures from conftest."""
    assert sample_message == "Test message"
    assert sample_number == 42


class TestClassExample:
    """Example test class."""

    def test_method_one(self) -> None:
        """Test method in class."""
        assert 1 == 1

    def test_method_two(self) -> None:
        """Another test method."""
        assert "test" == "test"
