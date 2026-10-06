from app.models.user import User
import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="password",database="tflinsurance_db")
cursor=connection.cursor()

class UserRepository:
    def __init__(self,user:User):
        self.user=user
        
    def get_all_users(self):
        sql="SELECT * FROM users"
        cursor.execute(sql)
        users=cursor.fetchall()
        return users        
    
    def get_user_by_id(self,user_id:int):
        sql="SELECT * FROM users WHERE user_id=%s"
        cursor.execute(sql,(user_id,))
        self._user=cursor.fetchall()
        return self._user