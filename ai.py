from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import StorageContext, Settings
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PERSIST_DIR = "./chroma_db"

# Initialize Gemini LLM and embedding model
llm = Gemini(
    model="models/gemini-2.0-flash",
    api_key=GOOGLE_API_KEY,
)

gemini_embedding = GeminiEmbedding()

# Configure global settings
Settings.llm = llm
Settings.embed_model = gemini_embedding
Settings.chunk_size = 1000

# Initialize ChromaDB
db = chromadb.PersistentClient(path=PERSIST_DIR)
chroma_collection = db.get_or_create_collection("my_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Check if we need to create a new index or load existing one
if not os.path.exists(PERSIST_DIR) or len(chroma_collection.get()['ids']) == 0:
    # Load documents and create index
    documents = SimpleDirectoryReader("data/").load_data()
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )
else:
    # Load existing index
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context
    )

def get_response(text) -> str:
    """
    Ask the AI model a question and get a response back
    """
    query_engine = index.as_query_engine()
    response = query_engine.query(text)
    return response.response

def get_streaming_response(text):
    """
    Get a streaming response from the query engine
    """
    query_engine = index.as_query_engine(streaming=True, similarity_top_k=1)
    return query_engine.query(text)

# Optional: Add streaming functionality
# query_engine = index.as_query_engine(streaming=True, similarity_top_k=1)
# streaming_response = lambda text: query_engine.query(text)