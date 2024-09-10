from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from multimodal import text_store, image_store, index

mm_llm = OpenAIMultiModal(
    model="gpt-4o", api_key="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", max_new_tokens=1000,
    text_store=text_store, image_store=image_store
)

text_query_engine = index.as_query_engine()

query_text = "Who is the best nba team"

text_retrieval_results = text_query_engine.query(query_text)

