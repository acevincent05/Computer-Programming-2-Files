class Employee:
    def __init__(self):
        self._name = ''
        self._gender = ''
        self._bDate = ''
        self._position = ''
        self._rate = ''
        self._daysWork = ''

    @property
    def getName(self):
        return self._name
    
    @getName.setter
    def setName(self, n):
        self._name = n

    @property
    def getGender(self):
        return self._gender
    
    @getGender.setter
    def setGender(self, g):
        self._gender = g
    
    @property
    def get_bDate(self):
        return self._bDate
    
    @get_bDate.setter
    def set_bDate(self, b):
        self._bDate = b
    
    @property
    def getPosition(self):
        return self._position
        
    @getPosition.setter
    def setPosition(self, p):
        self._position = p

    @property
    def getRate(self):
        return self._rate
    
    @getRate.setter
    def setRate(self, r):
        self._rate = r

    @property
    def get_daysWork(self):
        return self._daysWork
    
    @get_daysWork.setter
    def set_daysWork(self, d):
        self._daysWork = d
    
#operations

    #gross salary
    def getGross(self):
        gross = self._daysWork * self._rate
        return gross

    #SSS
    def getSSS(self):
        if self.getGross() < 10000:
            return 500
        elif self.getGross() >= 10000 and self.getGross() <= 20000: 
            return 1000
        else:
            return 1500
        
    #tax
    def getTax(self):
        if self.getGross() < 0:
            return 0
        elif self.getGross() >= 10000 and self.getGross() <= 20000:
            return self.getGross() * 0.10
        elif self.getGross() >= 20000 and self.getGross() <= 30000:
            return self.getGross() * 0.20
        else:
            return self.getGross() * 0.25

    #net salary
    def getNetSalary(self):
        net = self.getGross() - self.getSSS() - self.getTax()
        return net

#outputs

    #employee details
    def getEmployeeDetails(self):
       return (
        f"Name: {self._name}\n"
        f"Gender: {self._gender}\n"
        f"Birth Date: {self._bDate}\n"
        f"Position: {self._position}"
    )
    
    #salary details
    def getSalaryDetails(self):
       return (
        f"Gross Salary: ₱{self.getGross():,.2f}\n"
        f"SSS: ₱{self.getSSS():,.2f}\n"
        f"Tax: ₱{self.getTax():,.2f}\n"
        f"Net Salary: ₱{self.getNetSalary():,.2f}"
    )
    
name = input('Enter Employee Name: ')
gender = input('Enter Gender (M/F): ')
bDate = input('Enter Birth Date: ')
position = input('Enter Position: ')
rate = int(input('Enter Rate per day: '))
daysWork = int(input('Enter Days Worked: '))

emp1 = Employee()
emp1.setName = name
emp1.setGender = gender
emp1.set_bDate = bDate
emp1.setPosition = position
emp1.setRate = rate
emp1.set_daysWork = daysWork

print(emp1.getNetSalary())
print()
print('Employee Details:')
print()
print(emp1.getEmployeeDetails())
print()
print('Salary Details:')
print()
print(emp1.getSalaryDetails())