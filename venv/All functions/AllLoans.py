class AllLoans(object):

    def __init__(self):
        self.loans = {}

    def add_Loan(self,name,amount):
        self.loans[name] = amount


    def remove_Loan(self,name,amount):
        if name in self.loans.keys():
            self.loans[name] = 0
        else:
            pass
        
    def display(self):
        return self.loans

a = AllLoans()
a.add_Loan("CITI CREDIT CARD",65000)
a.add_Loan("SBI CREDIT CARD",55000)
a.remove_Loan("CITI CREDIT CARD",65000)

print(a.display())

