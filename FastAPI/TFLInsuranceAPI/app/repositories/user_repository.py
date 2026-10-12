import mysql.connector



class UserRepository:
    def __init__(self):
       self.connection=mysql.connector.connect(host="localhost",user="root",password="password",database="tflinsurance_db")
       self.cursor=self.connection.cursor()
        
    def get_all_users(self):
        sql="SELECT * FROM users"
        self.cursor.execute(sql)
        users=self.cursor.fetchall()
        return users        
    
    def get_user_by_id(self,user_id:int):
        sql="SELECT * FROM users WHERE user_id=%s"
        self.cursor.execute(sql,(user_id,))
        self.user=self.cursor.fetchall()
        return self.user