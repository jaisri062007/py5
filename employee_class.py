class employee:
    def __init__(self):
        self.id=int(input("Enter ID:"))
        self.name=input("Enter your name:")
        self.basic=int(input("Enter Basic Pay:"))
    def display(self):
        da=0.10*self.basic
        hra=0.20*self.basic
        g=da+hra+self.basic
        print("Employee Details...")
        print("Employee ID:",self.id,"\nEmployee Name",self.name,"\nDearness Allowance:",da)
        print("House Rent Allowance:",hra,"Gross Salary:",g)
e=employee()
e.display()
