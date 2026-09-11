import json

class Customer:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    
    def to_dict(self):
        """Convert the customer to a dictionary for JSON serialization."""
        return {"name": self.name,"phone":self.phone}
    
    @staticmethod
    def from_dict(data):
        """Create a customer instance from a dictionary."""
        return Customer(data['name'],data['phone'])
    
def serialize(filename,customers):
    """Serialize the list of customers and save it to a JSON file."""
    with open(filename,'w') as file:
        json_customers = [customer.to_dict() for customer in customers]
        json.dump(json_customers,file,indent=4)
    print(f"Customers saved to {filename}.")
    
def deserialize(filename):
    """Deserialize the list of customer from a JSON file."""
    try:
        with open(filename,'r') as file:
            json_customers=json.load(file)
            customers=[Customer.from_dict(customer) for customer in json_customers]
        print(f"Customer loaded from {filename}:")
        for customer in customers:
            print(customer.name, customer.phone)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filename}.")
        
        
if __name__=="__main__":
    customers=[
        Customer("Shivkumar","8393747309"),
        Customer("Sameer","93047526349"),
        Customer("Manoj","9840273846")
    ]
    
    filename='customers.json'
    
    serialize(filename,customers)
    deserialize(filename)