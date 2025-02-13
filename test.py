from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import StorageContext, Settings, VectorStoreIndex
from llama_index.llms.gemini import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = Gemini(
  model="models/gemini-2.0-flash",
  api_key=GOOGLE_API_KEY,
)

documents = SimpleDirectoryReader("data/").load_data()
gemini_embedding = GeminiEmbedding()

Settings.llm = llm
Settings.embed_model = gemini_embedding
Settings.chunk_size = 1000

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What are some of the important things he learned?")  
print(response)