import pytest
from Rufus.extractor import DataExtractor

def test_extraction_basic():
    """Test data extraction from raw HTML."""
    raw_data = ["<html><body>Product features and FAQs are here.</body></html>"]
    instructions = "Find product features and FAQs"
    extractor = DataExtractor(raw_data, instructions)
    result = extractor.extract()
    assert "extracted_data" in result
    assert len(result["extracted_data"]) > 0

def test_empty_raw_data():
    """Test behavior with empty raw data."""
    raw_data = []
    instructions = "Find something"
    extractor = DataExtractor(raw_data, instructions)
    result = extractor.extract()
    assert result["extracted_data"] == []
