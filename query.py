from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.llms.anthropic import Anthropic
from llama_index.llms.huggingface import HuggingFaceLLM
from multimodal import text_store, image_store, index

app = Flask(__name__)
CORS(app)

# Initialize different LLM instances
llms = {
    "gpt-4-vision-preview": OpenAIMultiModal(
        model="gpt-4-vision-preview", api_key="your-openai-api-key", max_new_tokens=1000,
        text_store=text_store, image_store=image_store
    ),
    "gpt-3.5-turbo": OpenAIMultiModal(
        model="gpt-3.5-turbo", api_key="your-openai-api-key", max_new_tokens=1000,
        text_store=text_store, image_store=image_store
    ),
    "claude-2": Anthropic(
        model="claude-2", api_key="your-anthropic-api-key", max_new_tokens=1000,
        text_store=text_store, image_store=image_store
    ),
    "mistral-7b": HuggingFaceLLM(
        model="mistral-7b", api_key="your-huggingface-api-key", max_new_tokens=1000,
        text_store=text_store, image_store=image_store
    ),
    "falcon-40b": HuggingFaceLLM(
        model="falcon-40b", api_key="your-huggingface-api-key", max_new_tokens=1000,
        text_store=text_store, image_store=image_store
    )
}

# Create MultiModal index
text_query_engine = index.as_query_engine(llm=llms["gpt-4-vision-preview"])

@app.route('/query', methods=['POST'])
def query():
    query_text = request.json.get('query')
    selected_llm = request.json.get('llm', 'gpt-4-vision-preview')
    
    if selected_llm in llms:
        text_query_engine = index.as_query_engine(llm=llms[selected_llm])
        text_retrieval_results = text_query_engine.query(query_text)
        return jsonify({"results": str(text_retrieval_results)})
    else:
        return jsonify({"error": "Selected LLM is not available"}), 400

if __name__ == '__main__':
    app.run(debug=True)
