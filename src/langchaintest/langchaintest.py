import os
import requests
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

# Load environment variables from .env file
load_dotenv()

# Make sure to set your OpenAI API key in the environment variable "OPENAI_API_KEY"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("Please set the 'OPENAI_API_KEY' environment variable.")

# URL to fetch the content from
URL = "https://ethz.ch/de.html"

def fetch_url_content(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    # Fetch webpage content
    content = fetch_url_content(URL)
    
    # Wrap the fetched content in a LangChain Document
    document = Document(page_content=content)
    
    # Initialize the OpenAI LLM with LangChain
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
    
    # Load a summarization chain
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    
    # Generate the summary from the document
    summary = chain.run([document])
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()