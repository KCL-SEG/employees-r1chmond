"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Bonus:
    def __init__(self,rate):
        self.value = rate

class ContractCommission:
    def __init__(self, num_of_contract, rate_per_contract):
        self.description = f"commission for {num_of_contract} contract(s) at {rate_per_contract}/contract"
        self.value = num_of_contract * rate_per_contract

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        if self.commission:
            self.get_base_pay() + self.commission.value
        return self.get_base_pay()

    def __str__(self):
        if self.commission:
            return f"{self.name} works on a {self.get_contract_desc()}" + \
            (f" and receives a {self.commission.description}") + \
                f". Their total pay is {self.get_pay()}."
        return f"{self.name} works on a {self.get_contract_desc()}" + \
                f". Their total pay is {self.get_pay()}."

class SalariedEmployee(Employee):
    def __init__(self, name, base_salary, commission = None):
        super().__init__(name, commission)
        self.base_salary = base_salary

    def get_contract_desc(self):
        return f"monthly salary of {self.base_salary}"
    
    def get_base_pay(self):
        return self.base_salary



class HourlyEmployee(Employee):
    def __init__(self, name, rate_per_hour, hours_worked, commission=None):
        super().__init__(name,commission)
        self.rate_per_hour = rate_per_hour
        self.hours_worked = hours_worked

    def get_base_pay(self):
        return self.rate_per_hour * self.hours_worked

    def get_contract_desc(self):
        return f"contract of {self.hours_worked} hours at {self.rate_per_hour}/hour"
    
    


billie = SalariedEmployee("Billie", 4000)
charlie = HourlyEmployee("Charlie", 25,100)
renee = SalariedEmployee("Renee", 3000, ContractCommission(4, 200))
"""
jan = HourlyEmployee("Jan", 25, 3, 220, 150, True)
robbie = SalariedEmployee("Robbie", 2000, 0, 1500, True)
ariel = HourlyEmployee("Ariel", 30, 0, 600, 120, True)"""

print(renee)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
#charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
#renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
#jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
#robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
#ariel = Employee('Ariel')

