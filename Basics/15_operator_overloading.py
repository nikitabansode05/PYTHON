class InsurancePolicy:
    def __init__(self,policy_id,customer,coverage):
        self.policy_id=policy_id
        self.customer=customer
        self.coverage=coverage
        
    def __str__(self):
        return (f"Policy Id :{self.policy_id} , Customer : {self.customer}, Coverage : {self.coverage}")
        
    def __add__(self,other):
        
        if isinstance(other,InsurancePolicy):
            combined_coverage=(self.coverage+other.coverage)
            
            return InsurancePolicy("COMBINED",self.customer,combined_coverage)
        
        return NotImplemented
    
policy1=InsurancePolicy("P1","Nikita",1000000)
policy2=InsurancePolicy("P2","Ravi",3000000)

combined_policy=policy1+policy2

print(combined_policy)