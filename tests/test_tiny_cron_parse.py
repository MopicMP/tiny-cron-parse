"""Tests for tiny-cron-parse."""

import pytest
from tiny_cron_parse import parse


class TestParse:
    """Test suite for parse."""

    def test_basic(self):
        """Test basic usage."""
        result = parse("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            parse("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = parse(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
