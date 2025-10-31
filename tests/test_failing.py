"""
Tests that intentionally fail - for validating CI/CD error handling.

These tests are SKIPPED by default to keep CI green.
Uncomment the @pytest.mark.skip decorator to test failure scenarios.
"""

import pytest


@pytest.mark.skip(reason="Intentionally failing test - enable to test CI failure handling")
def test_intentional_failure():
    """This test intentionally fails to validate CI error handling."""
    assert False, "This is an intentional failure for testing CI/CD"


@pytest.mark.skip(reason="Intentionally failing test - enable to test CI failure handling")
def test_assertion_error():
    """Test assertion error handling."""
    assert 1 == 2, "Math is broken!"


@pytest.mark.skip(reason="Intentionally failing test - enable to test CI failure handling")
def test_type_error():
    """Test type error handling."""
    result = "string" + 123  # This should raise TypeError


@pytest.mark.skip(reason="Intentionally failing test - enable to test CI failure handling")
def test_zero_division():
    """Test zero division error handling."""
    result = 1 / 0


@pytest.mark.skip(reason="Intentionally failing test - enable to test CI failure handling")
def test_missing_key():
    """Test missing key error handling."""
    test_dict = {"key1": "value1"}
    _ = test_dict["nonexistent_key"]
