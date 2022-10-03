"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

#class Employee:
    #def __init__(self, name):
     #   self.name = name

    #def get_pay(self):
     #   pass

    #def __str__(self):
        #return self.name

class Employee:
    commission = False
    def __init__(self, name, rate, numberOfContracts, isCommissioned = None):
        self.name = name
        self.rate = rate
        self.numberOfContracts = numberOfContracts
        if isCommissioned is None:
            isCommissioned = self.commission
        else:
            self.commission = isCommissioned

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getRate(self):
        return self.rate

    def getNumberOfContracts(self):
        return self.numberOfContracts

    def getIsCommissioned(self):
        return self.commission



class SalariedEmployee(Employee):
    def __init__(self, name, rate, numberOfContracts,commissionRate, isCommissioned = None):
        super().__init__(name, rate, numberOfContracts, isCommissioned)
        self.commissionRate = commissionRate

    def getCommissionRate(self):
        return self.commissionRate



class HourlyEmployee(Employee):
    def __init__(self, name, rate, numberOfContracts,commissionRate,hoursWorked, isCommissioned = None):
        super().__init__(name, rate, numberOfContracts, isCommissioned)
        self.commissionRate = commissionRate
        self.hoursWorked = hoursWorked

    def getCommissionRate(self):
        return self.commissionRate

    def getHoursWorked(self):
        return self.hoursWorked



class Payroll:
    def __init__(self, Employee):
        self.Employee = Employee

    def hourlyPay(self):
        return self.Employee.getRate() * self.Employee.getHoursWorked()

    def getPay(self):
        if self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getNumberOfContracts() > 0:
                return (self.Employee.getRate() * self.Employee.getHoursWorked()) + \
                        (self.Employee.getCommissionRate() * self.Employee.getNumberOfContracts())

        elif not self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getCommissionRate() == 0:
             return self.Employee.getRate() * self.Employee.getHoursWorked()

        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, SalariedEmployee) and \
         self.Employee.getNumberOfContracts() == 0:
                return self.Employee.getRate() + self.Employee.getCommissionRate()

        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getNumberOfContracts() == 0:
                return (self.Employee.getRate() * self.Employee.getHoursWorked()) \
                             + self.Employee.getCommissionRate()

        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, SalariedEmployee) and \
         self.Employee.getNumberOfContracts() > 0:
                return self.Employee.getRate() + \
                        (self.Employee.getCommissionRate() * self.Employee.getNumberOfContracts())

        else:
            return self.Employee.getRate()

    def str(self):
        if not self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getCommissionRate() == 0:
            return f"{self.Employee.getName()} works on a contract of {self.Employee.getHoursWorked()} hours at {self.Employee.getRate()}/hour. Their total pay is {self.getPay()}."
        
        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, SalariedEmployee) and \
         self.Employee.getNumberOfContracts() > 0:
            return f"{self.Employee.getName()} works on a monthly salary of {self.Employee.getRate()} and receives a commission for {self.Employee.getNumberOfContracts()} contract(s) at {self.Employee.getCommissionRate()}/contract. Their total pay is {self.getPay()}."

        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getNumberOfContracts() > 0:
            return f"{self.Employee.getName()} works on a contract of {self.Employee.getHoursWorked()} hours at {self.Employee.getRate()}/hour and receives a commission for {self.Employee.getNumberOfContracts()} contract(s) at {self.Employee.getCommissionRate()}/contract. Their total pay is {self.getPay()}."

        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, SalariedEmployee) and \
         self.Employee.getNumberOfContracts() == 0:
            return f"{self.Employee.getName()} works on a monthly salary of {self.Employee.getRate()} and receives a bonus commission of {self.Employee.getCommissionRate()}. Their total pay is {self.getPay()}."
        
        elif self.Employee.getIsCommissioned() and \
         isinstance(self.Employee, HourlyEmployee) and \
         self.Employee.getNumberOfContracts() == 0:
            return f"{self.Employee.getName()} works on a contract of {self.Employee.getHoursWorked()} hours at {self.Employee.getRate()}/hour and receives a bonus commission of {self.Employee.getCommissionRate()}. Their total pay is {self.getPay()}."

        else:
            return f"{self.Employee.getName()} works on a monthly salary of {self.getPay()}. Their total pay is {self.getPay()}."


billie = SalariedEmployee("Billie", 4000, 0,0)
charlie = HourlyEmployee("Charlie", 25, 0,0,100)
renee = SalariedEmployee("Renee", 3000, 4, 200, True)
jan = HourlyEmployee("Jan", 25, 3, 220, 150, True)
robbie = SalariedEmployee("Robbie", 2000, 0, 1500, True)
ariel = HourlyEmployee("Ariel", 30, 0, 600, 120, True)

billiePayroll = Payroll(billie)
charliePayroll = Payroll(charlie)
reneePayroll = Payroll(renee)
janPayroll = Payroll(jan)
robbiePayroll = Payroll(robbie)
arielPayroll = Payroll(ariel)


print(billiePayroll.str())
print()
print(charliePayroll.str())
print()
print(reneePayroll.str())
print()
print(janPayroll.str())
print()
print(robbiePayroll.str())
print()
print(arielPayroll.str())

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

