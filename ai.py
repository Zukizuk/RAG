from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage
from llama_index.core import StorageContext, Settings
from llama_index.llms.gemini import Gemini
from llama_index.core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PERSIST_DIR = "./storage"

# Create text QA template
text_qa_template = PromptTemplate(
    "You are an AI assistant that provides clear, insightful, and well-structured responses based on the context. "
    "Be friendly and helpful in your responses."
    "Integrate them fluidly into responses without prefacing with \"According to the text\" or similar phrases. "
    "If you cannot find a relevant passage, you can provide a general response. But let the user know that you are doing so. "
    "Get to the point efficiently without unnecessary framing.\n\n"
    "Context information is below:\n"
    "----------------\n"
    "{context_str}\n"
    "----------------\n"
    "Given this information, please answer the following question: {query_str}\n"
)

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


if not os.path.exists(PERSIST_DIR):
  documents = SimpleDirectoryReader("data/").load_data()
  index = VectorStoreIndex.from_documents(documents)
  index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
  storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
  index = load_index_from_storage(storage_context)


def get_response(text) -> str:
    """
    Ask the AI model a question and get a response back
    """
    query_engine = index.as_query_engine(
        text_qa_template=text_qa_template,
    )
    response = query_engine.query(text)
    return response.response

def get_streaming_response(text):
    """
    Get a streaming response from the query engine
    """
    query_engine = index.as_query_engine(
        streaming=True,
        similarity_top_k=1,
        text_qa_template=text_qa_template,
    )
    return query_engine.query(text)