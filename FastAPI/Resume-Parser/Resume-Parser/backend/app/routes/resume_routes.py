import logging
import os
import shutil
import time
from fastapi import (APIRouter,UploadFile,File,HTTPException)
from app.services.pdf_service import (extract_text_from_pdf)
from app.services.resume_service import (ResumeService)
from app.fileIO.serializer import Serializer
logger = logging.getLogger("API")

router = APIRouter(prefix="/api/resume",tags=["Resume"])
resume_service = ResumeService()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    start_time = (time.perf_counter())
    logger.info("========================================")
    logger.info("Resume upload started")
    
    # 1. Validate file
    
    logger.info(f"File received|type={file.content_type}")
    if not file.filename:
        logger.warning("No filename provided")
        raise HTTPException(status_code=400,detail="Filename is required")

    if not file.filename.lower().endswith(".pdf"):
        logger.warning("Invalid file type")
        raise HTTPException(status_code=400,detail="Only PDF files are allowed")
    
    # 2. Temporary storage
    
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads",file.filename)
    try:
        logger.info("Saving PDF temporarily")
        with open( file_path, "wb" ) as buffer:
            shutil.copyfileobj(file.file,buffer)
        logger.info("PDF saved successfully")
        
        # 3. PDF extraction
        
        resume_text, page_count = (extract_text_from_pdf( file_path))
        if not resume_text.strip():
            logger.warning("PDF contains no extractable text")
            raise HTTPException(status_code=400,
                detail=("Could not extract text from PDF"))
            
        # 4. Gemini + LangChain
        
        logger.info("Sending resume to Gemini through LangChain")
        resume_data = (resume_service.extract_resume_data(resume_text))
        # print(type(resume_data),resume_data)
        
        # save in file
        fileIO=Serializer()
        existing_resume=fileIO.deserialize("data/resumes.json")
        resumes=[existing_resume,]
        resumes.add(resume_data)
        fileIO.serialize("data/resumes.json",resumes)
        # 5. Metrics
        
        processing_time = (time.perf_counter() - start_time)
        skills_count = len(resume_data.skills)
        education_count = len(resume_data.education)
        experience_count = len(resume_data.experience)
        projects_count = len(resume_data.projects)
        logger.info("Resume extraction successful")
        logger.info(f"Skills extracted: {skills_count}")
        logger.info(f"Education entries: {education_count}")
        logger.info(f"Experience entries: {experience_count}")
        logger.info(f"Projects extracted: {projects_count}")
        logger.info(f"Total processing time: {processing_time:.2f}s")
        
        # 6. Response
        
        return {"status": "success",
            "metrics": {
                "page_count":page_count,
                "text_length":len(resume_text),
                "skills_count":skills_count,
                "education_count":education_count,
                "experience_count":experience_count,
                "projects_count":projects_count,
                "processing_time_seconds":round(processing_time,3)
            },
            "data":resume_data
        }
    except HTTPException:
        raise
    except Exception:
        logger.exception("Resume processing failed")
        raise HTTPException(status_code=500,detail="Resume processing failed")

    finally:
        # 7. Delete temporary PDF
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info("Temporary PDF deleted")
        logger.info("Resume request completed")
        logger.info("========================================")