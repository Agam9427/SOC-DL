class List():
    pass


class Person:
    
    def __init__(self,salary_per_month,investing_percentage):
        self.salary=salary_per_month
        self.percentage=investing_percentage
        self.cash=investing_percentage*salary_per_month/100

    def sal_chng(self,new_salary):
        self.salary=new_salary
        
    def per_chng(self,new_perc):
        self.percentage=new_perc
        
    def add_cash(self):
        self.cash+=self.percentage*self.salary/100

    def buy():
        pass

    def sell():
        pass

    def hold():
        pass


def Momentum():
    