import os
from .crawler import WebCrawler
from .extractor import DataExtractor
from .formatter import DataFormatter

class Rufus:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('RUFUS_API_KEY')

    def scrape(self, url, instructions):
     
        """
        Scrape and process data from the given URL based on user instructions.

        Args:
        - url (str): the URL to scrape.
        - instructions (str): the instructions to guide the data extraction.

        Returns:
        - dict: a dictionary with a single key "extracted_data" that contains a list
          of strings where each string is a relevant line extracted from the pages.
        """
        print(f"Starting scrape for: {url} with instructions: {instructions}")
        crawler = WebCrawler(url)
        raw_data = crawler.crawl()
        
        extractor = DataExtractor(raw_data, instructions)
        extracted_data = extractor.extract()
        
        formatter = DataFormatter(extracted_data)
        formatted_data = formatter.format()
        
        return formatted_data
