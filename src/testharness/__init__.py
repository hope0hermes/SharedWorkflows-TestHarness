"""SharedWorkflows Test Harness - minimal package for testing workflows."""

__version__ = "0.1.0"


def hello() -> str:
    """Return a greeting message."""
    return "Hello from SharedWorkflows Test Harness!"


__all__ = ["hello"]
