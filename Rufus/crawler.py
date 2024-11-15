import requests
from bs4 import BeautifulSoup
from Rufus.error_handler import ErrorHandler
import time

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.max_retries = 3  # Max retries for each page in case of failure

    def crawl(self, max_pages=10, max_depth=2, delay=1):
       
      """
      Crawl the base URL up to a specified number of pages and depth.

      This function performs a breadth-first crawl starting from the base URL,
      visiting pages up to a maximum number of pages (`max_pages`) and a maximum
      depth (`max_depth`). It collects the HTML content of the pages visited.

      Args:
          max_pages (int): The maximum number of pages to visit. Default is 10.
          max_depth (int): The maximum depth to crawl. Default is 2.
          delay (int): The delay in seconds between requests to avoid rate limiting. Default is 1.

      Returns:
          list: A list containing the HTML content of the pages visited.

      Raises:
          RuntimeError: If a page fails to load after a specified number of retries.
      """
      to_visit = [(self.base_url, 0)]  # List of tuples (url, depth)
      html_content = []

      while to_visit and len(html_content) < max_pages:
          url, depth = to_visit.pop(0)
          if url not in self.visited and depth <= max_depth:
              try:
                  response = self._get_page(url)
                  html_content.append(response.text)
                  self.visited.add(url)

                  if depth < max_depth:
                      links = self._parse_links(response.text)
                      to_visit.extend([(link, depth + 1) for link in links])

                  time.sleep(delay)  # Delay between requests to avoid rate limiting

              except requests.RequestException as e:
                  ErrorHandler.handle_crawl_error(url)
                  raise RuntimeError(f"Crawl failed for {url}") from e

      return html_content

    def _get_page(self, url):
       
        """
        Helper method to request a page and handle retries.

        :param url: The URL of the page to request
        :return: The response object for the page
        :raises: requests.RequestException if all retries fail
        """
        for _ in range(self.max_retries):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Will raise an exception for 4xx/5xx errors
                return response
            except requests.RequestException as e:
                print(f"Retrying {url} due to error: {e}")
                time.sleep(2)  # Wait before retrying
        raise requests.RequestException(f"Failed to fetch {url} after {self.max_retries} retries")

    def _parse_links(self, html):
        
        """Parse HTML content and extract internal links (both relative and absolute)."""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a in soup.find_all('a', href=True):
            link = a['href']
            if link.startswith('/'):  # Internal links
                links.add(self.base_url + link)
            elif self.base_url in link:  # Absolute internal links
                links.add(link)
        return links
