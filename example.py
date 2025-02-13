from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import StorageContext, Settings, VectorStoreIndex, load_index_from_storage
from llama_index.llms.gemini import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PERSIST_DIR = "./storage"

llm = Gemini(
  model="models/gemini-2.0-flash",
  api_key=GOOGLE_API_KEY,
)

gemini_embedding = GeminiEmbedding()

Settings.llm = llm
Settings.embed_model = gemini_embedding
Settings.chunk_size = 1000

if not os.path.exists(PERSIST_DIR):
  documents = SimpleDirectoryReader("data/").load_data()
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
  storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
  index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine(streaming=True, similarity_top_k=1)
streaming_response = query_engine.query("Who is Chris?") 
# for text in streaming_response.response_gen:
#     # do something with text as they arrive.
#     print(text)
streaming_response.print_response_stream()