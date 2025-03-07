import os
import time

import tiktoken
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.llms.openai import OpenAI

token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode,
)

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.2)
Settings.callback_manager = CallbackManager([token_counter])


def main() -> None:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        print(f"OPENAI_API_KEY: {openai_api_key}")
    else:
        print("OPENAI_API_KEY is not set")
    start_time = time.time()
    documents = SimpleDirectoryReader("data").load_data()
    end_time = time.time()
    print(f"Time taken to load documents: {end_time - start_time} seconds")

    start_index_time = time.time()
    index = VectorStoreIndex.from_documents(documents)
    end_index_time = time.time()
    print(f"Time taken to create index: {end_index_time - start_index_time} seconds")

    retriever = index.as_retriever()

    query = ""

    nodes = retriever.retrieve(query)
    print(f"Number of nodes retrieved for query: {len(nodes)}")

    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)
    print(token_counter.prompt_llm_token_count)


if __name__ == "__main__":
    main()
