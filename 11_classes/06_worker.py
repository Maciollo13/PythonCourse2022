class worker:
    company_name = "Lumos"
    def __init__(self,name,last,payroll,seniority,student):
        self.name = name
        self.last = last
        self.seniority = seniority
        self.payroll = payroll
        self.student = student

    def health_insurance(self):
        if self.student:
            return "No health insurance needed"
        else:
            return self.payroll * 0.08

    def tax(self):
        return self.payroll * 0.1

    def payroll_taxed(self):
        self.payroll -= self.tax()
        if not self.student:
            self.payroll -= self.health_insurance()
        return self.payroll

    def payroll_raise(self):
        for i in range (self.seniority):
            self.payroll += 200
        return self.payroll

    def email(self):
        return f"{self.name}.{self.last}@lumos.eu"

ania = worker("ania","abrams",2000,2,True)
print(ania.payroll_taxed())
print(ania.payroll_raise())
print(ania.email())