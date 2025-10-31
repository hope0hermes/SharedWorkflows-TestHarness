"""Shared pytest fixtures for SharedWorkflows Test Harness."""

import pytest


@pytest.fixture
def sample_message() -> str:
    """Provide a sample message for testing."""
    return "Test message"


@pytest.fixture
def sample_number() -> int:
    """Provide a sample number for testing."""
    return 42
