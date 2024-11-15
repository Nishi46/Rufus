from Rufus.agent import Rufus
import os


key = os.getenv('RUFUS_API_KEY')  # Assuming the API key is stored in environment variables
client = Rufus(api_key=key)

instructions = "We're making a chatbot for the HR in San Francisco."
url = "https://www.sf.gov"

documents = client.scrape(url, instructions)

print(documents)
