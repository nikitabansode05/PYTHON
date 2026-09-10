import mysql.connector

dbConnection=mysql.connector.connect(host="localhost",user="root",password="password",database="tap")
dbCommand=dbConnection.cursor()

#insert

def add_student():
    id=int(input("Enter Id :"))
    name=input("Enter name : ")
    email=input("Enter email : ")
    
    sql="INSERT INTO students(id,name,email) VALUES(%s,%s,%s)"
    values=(id,name,email)
    
    dbCommand.execute(sql,values)
    dbConnection.commit()
    
    print("Student added successfully")
    
#menu

while True:
    print("\n1)Add Student")
    print("\n2) Exit")
    
    choice=input("Enter Choice : ")
    
    if choice=="1":
        add_student()
    elif choice == "2":
        break
    else:
        print("Invalid choice")
        
dbCommand.close()
dbConnection.close()