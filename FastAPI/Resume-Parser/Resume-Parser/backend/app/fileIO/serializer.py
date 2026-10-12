import json
from app.schemas.resume_schema import ResumeData
class Serializer:
    def serialize(self,filename,resumes):
        with open(filename,'w') as file:
            json_resume=[resume.to_dict() for resume in resumes]
            json.dump( json_resume,file)
            
    def deserialize(self,filename):
        try:
            with open(filename,'r') as file:
                json_resumes=json.load(file)
                resumes=[ResumeData.model_validate(resume) for resume in json_resumes]
                return resumes
        except FileNotFoundError:
            print("file not found")
        except json.JSONDecodeError:
            print("Error decoding json data from file")