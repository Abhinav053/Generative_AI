from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.chat_models import init_chat_model

from pydantic import BaseModel
from typing import List, Optional

# Load environment variables
load_dotenv()

# Correct env variable name, with a fallback for the current .env typo.
api_key = os.getenv("GEMNI_API_KEY") or os.getenv("GEMNI_API_KEY")

# Initialize model
llm = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    google_api_key=api_key
)

# Pydantic Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """Extract movie information from the paragraph.
{format_instructions}
"""),
    ("human", "{paragraph}")
])

# Input
para = input("Give your paragraph: ")

# Build prompt
final_prompt = prompt.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})

# Call model (FIX: use llm, not model)
response = llm.invoke(final_prompt)

# Parse response
movie_data = parser.parse(response.content)

print(movie_data)
