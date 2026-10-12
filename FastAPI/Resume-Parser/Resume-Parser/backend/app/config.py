import os
from dotenv import load_dotenv
load_dotenv()
# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# LangSmith
# LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING","false")
# LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
# LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT","resume-parser-gemini")