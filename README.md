# GenAI

Small Python workspace for experimenting with generative AI workflows using LangChain, Google Gemini, Streamlit, embeddings, and structured output parsing.

## Project Contents

- `main.py` - minimal project entry point.
- `generativeAI/embedings_modal/document_similarity.py` - compares a query with sample documents using Gemini embeddings and cosine similarity.
- `generativeAI/CineSage/core.py` - command-line movie information extractor that returns structured data with a Pydantic schema.
- `generativeAI/CineSage/UICode.py` - Streamlit UI for extracting structured movie data from a paragraph.
- `generativeAI/1_langchainintro.ipynb` - introductory LangChain notebook.

## Tech Stack

- Python 3.12+
- LangChain
- Google Gemini via `langchain-google-genai`
- Streamlit
- Pydantic
- scikit-learn
- NumPy
- python-dotenv

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If you are using `uv`, you can install from `pyproject.toml` instead:

```powershell
uv sync
```

3. Create a `.env` file in the project root:

```env
GEMNI_API_KEY=your_google_gemini_api_key_here
```

Note: the current code reads `GEMNI_API_KEY`, so keep that spelling unless you update the code to use `GEMINI_API_KEY`.

## Usage

Run the basic project entry point:

```powershell
python main.py
```

Run the document similarity example:

```powershell
python generativeAI\embedings_modal\document_similarity.py
```

Run the CineSage command-line extractor:

```powershell
python generativeAI\CineSage\core.py
```

Run the CineSage Streamlit app:

```powershell
streamlit run generativeAI\CineSage\UICode.py
```

## Example Features

### Document Similarity

The embedding example:

- creates embeddings for a small list of cricket-related documents,
- embeds a user query,
- compares them with cosine similarity,
- prints the closest matching document and similarity score.

### CineSage Movie Extractor

CineSage converts an unstructured movie paragraph into structured JSON-like data:

- title
- release year
- genre
- director
- cast
- rating
- summary

## Environment Variables

| Variable | Description |
| --- | --- |
| `GEMNI_API_KEY` | Google Gemini API key used by the current scripts. |

## Notes

- The project currently contains learning/demo scripts, so some inputs are hardcoded.
- The `document_similarity.py` example uses the Gemini embedding model `gemini-embedding-exp-03-07`.
- The CineSage examples use `gemini-2.5-flash`.
- Do not commit your `.env` file or API keys.
