from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import (CORSMiddleware)
from app.logging_config import (setup_logging)
from app.routes.resume_routes import (router)
# Logging
setup_logging()
# FastAPI
app = FastAPI(title="Gemini Resume Parser API",description="Resume extraction using FastAPI + LangChain + Gemini",version="1.0.0")
# CORS
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
# Routes
app.include_router(router)

@app.get("/")
def home():

    return {"message":"Gemini Resume Parser API is running"
}