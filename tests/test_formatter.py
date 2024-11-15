import pytest
from Rufus.formatter import DataFormatter

def test_format_json():
    """Test JSON formatting of data."""
    data = {"key": "value"}
    formatter = DataFormatter(data)
    result = formatter.format()
    assert isinstance(result, str)
    assert '"key": "value"' in result

def test_format_empty_data():
    """Test formatting of empty data."""
    data = {}
    formatter = DataFormatter(data)
    result = formatter.format()
    assert result == "{}"
