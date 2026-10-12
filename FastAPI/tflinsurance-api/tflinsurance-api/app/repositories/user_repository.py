# import mysql.connector 
# from app.models.user import User

# dbConnection=mysql.connector.connect(host="localhost",user="root",password="password",database="tflinsurance_db")
# dbCommand=dbConnection.cursor()

# class UserRepository:
#insert
    # def add_users(self, user:User):
        
    #     sql="INSERT INTO users(id, name,email, password_hash, status, created_at, updated_at) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    #     values=(user.user_id, user.username,user.email, user.password_hash, user.status,user.created_at, user.updated_at)
        
    #     dbCommand.execute(sql,values)
    #     dbConnection.commit()
    #     return {"message":"user added successfully"}

    # def  get_users(self):
    #     sql="SELECT * from users "
    #     dbCommand.execute(sql)
    #     users=dbCommand.fetchall()
    #     return users


    # def put_users(self,user:User):


    #     sql="UPDATE users SET  username=%s, email=%s, password_hash=%s, status=%s, created_at=%s, updated_at=%s WHERE user_id=%s"
    #     values=(user.user_id, user.username, user.email, user.password_hash, user.status, user.created_at, user.updated_at)

    #     dbCommand.execute(sql, values)
    #     dbConnection.commit()

    #     print("users data put succsfully")

    # def delete_users(self, user_id:int):

    #     sql="DELETE FROM  users WHERE user_Id=%s"
    #     values=(user_id,)

    #     dbCommand.execute(sql, values)
    #     dbConnection.commit()

    #     print("user delete succesfullyy here ")

import mysql.connector
from app.schemas.user_schema import UserCreate

class UserRepository:

    def __init__(self):

        self.dbConnection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="tflinsurance_db",
            use_pure=True
        )

        self.dbCommand = self.dbConnection.cursor(dictionary=True)

    def get_users(self):

        sql = "SELECT * FROM users"

        self.dbCommand.execute(sql)

        users = self.dbCommand.fetchall()

        return users

    def add_users(self, user:UserCreate):
        
        sql="INSERT INTO users(username,email, password_hash, status) VALUES(%s,%s,%s,%s)"
        values=(user.username,user.email, user.password_hash,user.status)
        
        self.dbCommand.execute(sql,values)
        self.dbConnection.commit()

        new_id = self.dbCommand.lastrowid

        self.dbCommand.execute("SELECT * FROM users WHERE user_id = %s", (new_id,))
        return self.dbCommand.fetchone()
