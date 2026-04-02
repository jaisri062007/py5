class EB:
    def __init__(self):
        self.units=int(input("Enter units used:"))
    def display(self):
        amo=0
        if self.units <=100:
            amo="No Amount"
        elif self.units>100 and self.units <=200:
            amo=amo+((self.units-100)*1.5)
        elif self.units>200 and self.units <=300:
            amo=amo+(100*1.5)+((self.units-200)*5)
        elif self.units>300 and self.units <=400:
            amo=amo+(100*1.5)+(200*2.5)+((self.units-300)*4)
        elif self.units >=401:
            amo=amo+(100*1.5)+(200*2.5)+(300*4)+((self.units-400)*5)
        print("\nUnits used:",self.units,"\nElectricity Bill Amount:",amo)
eb=EB()
eb.display()
