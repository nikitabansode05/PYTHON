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
    
def update_student():
    id=int(input("Enter the id : "))
    name=input("Enter the correct name : ")
    email=input("Enter the correct mail : ")
    
    sql="UPDATE students SET name=%s,email=%s WHERE id=%s"
    values=(name,email,id)
    dbCommand.execute(sql,values)
    dbConnection.commit()   
    
    print("Data updated successfully") 
#menu

while True:
    print("\n1)Add Student")
    print("\n2)Update student information")
    print("\n3) Exit")
    
    choice=input("\nEnter Choice : ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
        
dbCommand.close()
dbConnection.close()