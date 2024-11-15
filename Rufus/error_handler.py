import logging
import traceback

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("rufus_errors.log"),  
        logging.StreamHandler()  
    ]
)

class ErrorHandler:
    @staticmethod
    def log_error(error_message, exception=None):
        
      """
      Logs an error message with optional exception details.

      If an exception is provided, logs the error message along with
      the exception details and a detailed traceback at the debug level.
      If no exception is provided, logs only the error message.

      :param error_message: A string describing the error.
      :param exception: Optional; an exception object for detailed logging.
      """
      if exception:
          logging.error(f"{error_message}\nException: {str(exception)}")
          logging.debug(traceback.format_exc()) 
      else:
          logging.error(error_message)

    @staticmethod
    def handle_crawl_error(url):
        
        """
        Handle errors related to web crawling.

        :param url: The URL where the error occurred.
        """
        error_message = f"Failed to crawl URL: {url}"
        ErrorHandler.log_error(error_message)

    @staticmethod
    def handle_extraction_error(data):
        
      """
      Handle errors during data extraction.

      :param data: The data that caused the extraction issue.
      Logs the first 100 characters of the data for debugging purposes.
      """
      error_message = f"Data extraction failed for content: {str(data)[:100]}..."  # Log the first 100 chars
      ErrorHandler.log_error(error_message)

    @staticmethod
    def handle_formatting_error(data):
        
        """
        Handle errors during data formatting.

        :param data: The data that caused the formatting issue.
        Logs the first 100 characters of the data for debugging purposes.
        """
        error_message = f"Data formatting failed for content: {str(data)[:100]}..."
        ErrorHandler.log_error(error_message)

    @staticmethod
    def critical_error(exception):

        """
        Handle critical errors that require immediate program termination.

        :param exception: The exception that caused the critical error.
        Logs the error message and a stack trace before exiting the process.
        """

        logging.critical("A critical error occurred. Terminating the process.")
        logging.critical(f"Exception: {str(exception)}")
        logging.debug(traceback.format_exc())
        exit(1)
