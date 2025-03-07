import os

import requests
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()


class OpenaiKeyNotFoundError(ValueError):
    def __init__(self) -> None:
        super().__init__("OpenAI API key not found. Please set the 'OPENAI_API_KEY' environment variable.")


# Make sure to set your OpenAI API key in the environment variable "OPENAI_API_KEY"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise OpenaiKeyNotFoundError

# URL to fetch the content from
URL = "https://ethz.ch/de.html"


def fetch_url_content(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def main() -> None:
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
