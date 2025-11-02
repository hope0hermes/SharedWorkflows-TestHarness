"""
SharedWorkflows Test Harness.

A minimal test package for validating SharedWorkflows CI/CD pipeline.
"""

__version__ = "0.4.0"


def get_version() -> str:
    """Get the package version.

    Returns:
        The current package version string.
    """
    return __version__


def hello() -> str:
    """Return a greeting message."""
    return "Hello from SharedWorkflows Test Harness!"


def get_info() -> dict[str, str]:
    """Get package information.

    Returns:
        Dictionary with package name and version.
    """
    return {
        "name": "SharedWorkflows-TestHarness",
        "version": __version__,
    }


__all__ = ["hello", "get_version", "get_info"]
