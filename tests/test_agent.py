import pytest
from Rufus.agent import Rufus

def test_agent_initialization():
    """Test if the Rufus agent initializes correctly."""
    agent = Rufus(api_key="test_key")
    assert agent.api_key == "test_key"

def test_agent_scrape(monkeypatch):
    """Test the scrape method of the Rufus agent."""
    def mock_crawl(self):
        return ["<html><body>Sample HTML</body></html>"]

    monkeypatch.setattr("Rufus.crawler.WebCrawler.crawl", mock_crawl)

    def mock_extract(self):
        return {"extracted_data": ["Sample content"]}

    monkeypatch.setattr("Rufus.extractor.DataExtractor.extract", mock_extract)

    agent = Rufus(api_key="test_key")
    result = agent.scrape("https://cnn.com", "HEadlines")
    assert "extracted_data" in result
