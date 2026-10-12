from fastapi import FastAPI
from database import get_connection
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    id:int
    name:str
    email:str
@app.get("/api/students")
def get_students():
    connection = get_connection()
    cursor=connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    cursor.close()
    connection.close()
    return students

@app.post("/api/student")
def insert_student(student:Student):
    connection=get_connection()
    cursor=connection.cursor()
    
    query="INSERT INTO students(name,email) VALUES(%s,%s)"
    
    cursor.execute(query,(student.name,student.email))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return {
        "message":"Student created successfully"
    }
    
@app.put("/api/student")
def update_student(student:Student):
    connection=get_connection()
    cursor=connection.cursor()
    query="UPDATE students SET name=%s,email=%s WHERE id=%s"
    
    cursor.execute(query,(student.name,student.email,student.id))
    connection.commit()
    rows_affected=cursor.rowcount
    
    cursor.close()
    connection.close()
    
    if rows_affected==0:
        return {"message":"Student not found"}
    
    return {
        "message":"Student updated successfully"
    }
    
@app.delete("/api/student/{student_id}")
def delete_student(student_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s",(student_id,))
    connection.commit()
    rows_affected=cursor.rowcount
    cursor.close()
    connection.close()
    
    if rows_affected==0:
        return{"message":"student not found"}
    
    return {"message":"Student deleted successfully"}
