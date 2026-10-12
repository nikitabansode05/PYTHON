from typing import List
from pydantic import BaseModel

class Education(BaseModel):
    degree: str
    institution: str
    year: str

class Experience(BaseModel):
    company: str
    role: str
    duration: str

class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]
    education: List[Education]
    experience: List[Experience]
    projects: List[str]