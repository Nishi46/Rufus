import pytest
from Rufus.crawler import WebCrawler

def test_crawl_success(monkeypatch):
    """Test successful crawling of a URL."""
    def mock_get(url):
        class MockResponse:
            status_code = 200
            text = "<html><body>Sample HTML</body></html>"

            def raise_for_status(self):
                pass

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    crawler = WebCrawler("https://cnn.com")
    html_content = crawler.crawl()
    assert len(html_content) == 1
    assert "Sample HTML" in html_content[0]

def test_crawl_failure(monkeypatch):
    """Test handling of a crawl failure."""
    def mock_get(url):
        raise Exception("Request failed")

    monkeypatch.setattr("requests.get", mock_get)

    crawler = WebCrawler("https://cnn.com")
    with pytest.raises(RuntimeError):
        crawler.crawl()
