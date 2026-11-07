#handler is a function pointer
#handlers are just functions (first-class objects) passed around,
# not raw memory pointers, 
# but they behave like references to executable code.

class EventDispatcher:

    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_name, handler):

        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(handler)

    def publish(self, event_name, data):

        print(f"\nEvent Published: {event_name}")

        for handler in self.handlers.get(event_name, []):
            handler(data)   #This is called passing functions as values / first-class functions in Python.
            
def validate_claim(data):   #handler

    print("Validating claim:", data["claim_id"])

    if data["amount"] <= 0:
        print("Invalid claim amount")
        return

    print("Claim validation completed")


def notify_customer(data):#handler

    print("Sending claim acknowledgement to:",
          data["customer_email"])


def notify_claims_officer(data):#handler

    print("Notifying claims officer about:",
          data["claim_id"])


def update_audit_log(data):#handler

    print("Recording claim submission in audit log")
    
dispatcher = EventDispatcher()
dispatcher.subscribe("ClaimSubmitted", validate_claim)
dispatcher.subscribe("ClaimSubmitted", notify_customer)
dispatcher.subscribe("ClaimSubmitted", notify_claims_officer)
dispatcher.subscribe("ClaimSubmitted", update_audit_log)

claim = {
    "claim_id": "CLM1001",
    "customer_name": "Rahul",
    "customer_email": "rahul@example.com",
    "amount": 50000
}

dispatcher.publish("ClaimSubmitted", claim)