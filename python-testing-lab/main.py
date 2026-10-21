from fastapi import FastAPI,HTTPException

app=FastAPI()

students = {
    101:{"id":101,"name":"Rahul"},
    102:{"id":102,"name":"Priya"},
}

@app.get("/api/students/{student_id}")
def get_studnet(student_id:int):
    student=students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404,detail="Student not found",)
    return student