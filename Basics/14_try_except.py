try:
    premium=float(input("Enter annual premium : "))
    
    if premium <=0 :
        raise ValueError("The premium must be greater than zero.")
    
    print("Premium accepted : ",premium)
    
except ValueError as ex:
    print("Invalid premium : ",ex)