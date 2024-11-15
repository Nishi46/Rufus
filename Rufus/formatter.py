import json
from Rufus.error_handler import ErrorHandler

class DataFormatter:
    def __init__(self, data):
        # Initialize with the provided data
        self.data = data
        # Define the output file path (hardcoded in the code)
        self.output_file = 'output_data.json'

    def format(self):
        
        """
        Format data into structured JSON and store it in a file.
        
        :return: None
        :raises RuntimeError: If data formatting or file writing fails
        """
        print("Formatting data into JSON format")
        try:
            # Format the data into a pretty-printed JSON string
            formatted_data = json.dumps(self.data, indent=4)
            
            # Write the formatted JSON to the output file
            with open(self.output_file, 'w') as file:
                file.write(formatted_data)
            
            print(f"Data successfully written to {self.output_file}")
        except Exception as e:
            # Handle any formatting or file-writing errors
            ErrorHandler.handle_formatting_error(self.data)
            raise RuntimeError("Data formatting or file writing failed") from e
