import pickle
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core.indices import VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
# from conversions import text_to_pdf
from conversions import convert_to_images
import openai

qdrant_store = 'my_qdrant_store.pk'
image_store_file = 'my_image_store_file.pk'
text_store_file = 'my_text_store_file.pk'

openai.api_key = "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"
text_path = "/Users/ryanasermely/Desktop/podcom/store"
image_path = "/Users/ryanasermely/Desktop/podcom/image_store"

# text_to_pdf(text_path)
# convert_to_images(pdf_path)

def initialize_qdrant_client(database_path):
    qdrant_client = QdrantClient(
        url="https://1794eea8-b24b-42b0-964e-04b7e8f29a54.us-east4-0.gcp.cloud.qdrant.io:6333", 
        api_key="1jyHUExxUbJPUjKDLcUIN5doZKcUjMaFICrOli9ICIhTCI0xVWIwGg"
    )
    return qdrant_client

# def initialize_qdrant_client(database_path):
#     if not os.path.exists(database_path):
#         client = qdrant_client.QdrantClient(path=database_path)
#         return client
#     else:
#         qdrant_client_instance = qdrant_client.QdrantClient(path=database_path)
#         return qdrant_client_instance

client = initialize_qdrant_client('qdrant_mm_db')

def set_text_store(my_client):
    text_store = QdrantVectorStore(
        client=my_client, collection_name="text_collection"
    )
    return text_store

text_store = set_text_store(client)
    
def set_image_store(my_client):
    image_store = QdrantVectorStore(
        client=my_client, collection_name="image_collection"
    )
    return image_store

image_store = set_image_store(client)

def set_storage_context(my_text_store, my_image_store):   
    storage_context = StorageContext.from_defaults(
        vector_store=my_text_store, image_store=my_image_store
    )
    print("storage context working")
    return storage_context

storage_context = set_storage_context(text_store, image_store)


def setup_multimodal_index(text_documents_path, image_documents_path):
    text_documents = SimpleDirectoryReader(text_documents_path).load_data()
    image_documents = SimpleDirectoryReader(image_documents_path).load_data()
    all_documents = text_documents + image_documents
    print("all documents set")
    multimodal_index = VectorStoreIndex.from_documents(
        all_documents,
        storage_context=storage_context,
    )
    print("index created!!!")
    return multimodal_index

index = setup_multimodal_index(text_path, image_path)

