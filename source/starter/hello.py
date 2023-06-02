"""Module Docstring."""

import logging

log = logging.getLogger("starter")


def say(name: str) -> str:
    """Function Docstring."""
    log.info("Hello %s", name)
    return f"Hello {name}"
