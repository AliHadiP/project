# this code create an example of company class
class company():
    def __init__(self, name, manager, address, NOF, income): #NOF = number of employees
        self.name = name
        self.manager = manager
        self.address = address
        self.NOF = NOF
        self.income = income

    def __str__(self):
        return f"Company Name: {self.name}\nManager: {self.manager}\nAddress: {self.address}\n"
    
    def productivity(self):
        productivity = self.income/self.NOF
        return f"productivity per employees equal to {productivity}"
    
company1 = company("Apple","Tim Cook","One Apple Park Way; Cupertino, CA 95014, U.S.A",100,1000)

print(company1,company1.productivity())