# Rufus: Intelligent Web Scraping and Data Extraction

Rufus is an AI-powered web scraping and data extraction tool designed to intelligently crawl websites and extract relevant content based on user-defined instructions. It is built to work seamlessly within Retrieval-Augmented Generation (RAG) pipelines, focusing on extracting the most relevant sections of a webpage (e.g., FAQs, pricing, customer support) while minimizing irrelevant data.

## Features

- Intelligent Crawling: Rufus crawls websites based on user-defined prompts, ensuring only relevant pages are scraped.
- AI-Powered Data Extraction: It leverages natural language processing (NLP) models to interpret user instructions and extract the most relevant content (such as product details, FAQs, or pricing).
- Customizable: Users can define specific instructions to guide the web scraping process, making it flexible for various applications.
- Error Handling: Built-in error management to ensure smooth crawling and extraction processes, with helpful feedback on failures.
- Supports Structured and Unstructured Data: Can handle both structured (tables, lists) and unstructured data (text blocks, paragraphs).

## Core Components:
- WebCrawler: Crawls web pages and retrieves raw HTML content.
- DataExtractor: Extracts relevant data using NLP to match user instructions.
- DataFormatter: Formats extracted data into a structured JSON file.


## How to use:

1. clone this repo
2. ```pip3 install -r requirements.txt ```
3.  ```
    from Rufus.agent import Rufus
    import os
    
    key = os.getenv('RUFUS_API_KEY')  # Assuming the API key is stored in environment variables
    client = Rufus(api_key=key)

    instructions = "We're making a chatbot for the HR in San Francisco."
    url = "https://www.sf.gov"

    documents = client.scrape(url, instructions)

    print(documents)
    ```


## Advanced Features

### AI-Powered Instruction Parsing
Rufus uses NLP models to interpret user instructions and extract context. For example, if a user requests “Find product pricing and customer support,” Rufus will focus on these sections of the page.

### Dynamic Web Crawling
Rufus intelligently handles nested links and dynamic page structures, only following relevant links that align with user instructions, ensuring efficient data extraction.

### Error Handling
Rufus includes robust error handling to manage issues during web scraping, such as request failures, parsing issues, or missing data, with clear error messages to guide troubleshooting.

