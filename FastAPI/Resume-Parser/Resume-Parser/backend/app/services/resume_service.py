import logging
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from app.schemas.resume_schema import ResumeData

logger = logging.getLogger("LANGCHAIN")

class ResumeService:

    def __init__(self):
        logger.info("Initializing Gemini ResumeService")
        # Gemini
        self.model = ChatGoogleGenerativeAI(model="gemini-3.8-flash",temperature=0,max_retries=2)
        logger.info("Gemini model initialized")
        # Structured output
        self.structured_model = (self.model.with_structured_output(ResumeData))
        # Prompt
        self.prompt = (ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """
                        You are a professional
                        resume information extraction
                        system.
                        Extract structured information
                        from the provided resume.
                        
                        Rules:

                        1. Do not invent information.
                        2. Only extract information
                           explicitly present in the
                           resume.
                        3. If information is unavailable,
                           return an empty string.
                        4. If a list has no information,
                           return an empty list.
                        5. Preserve the meaning of the
                           candidate's information.
                        """
                    ),
                    (
                        "human",
                        """
                        Extract structured information
                        from the following resume:
                        {resume_text}
                        """
                    )
                ]
            )
        )
        # LangChain pipeline
        self.chain = (self.prompt|self.structured_model)
        logger.info("Gemini LangChain chain initialized")
        
    def extract_resume_data(self,resume_text: str):
        logger.info(f"Starting Gemini resume extraction|text_length={len(resume_text)}")
        start_time = (time.perf_counter())
        try:
            result = (self.chain.invoke({"resume_text": resume_text}))
            duration = (time.perf_counter() - start_time)
            logger.info(f"Gemini extraction completed | duration={duration:.2f}s")
            return result
        except Exception:
            logger.exception("Gemini extraction failed")
            raise