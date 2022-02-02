class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Amount):
        self.CAmount = Amount
        self.Name = Name

    def __Deposit(self,DAmount):
        if(DAmount == 0):
            print("Please enter valid Amount")
        self.CAmount = self.CAmount + DAmount
        print(DAmount,"rupees have been deposited successfully","Your Net Balance is :",self.CAmount)

    def __Withdrawl(self,WAmount):
        if(WAmount > self.CAmount):
            print("Please enter valid Amount")
            return False
        else:
            self.CAmount = self.CAmount - WAmount
            print(WAmount,"ruppes Money Withdrwal successfully")
            

    def CalculateIntrest(self):
        RateOFIntrest = self.CAmount * (BankAccount.ROI)/100
        print(RateOFIntrest,"is your Rate of Intrest")

    def Display(self):   
        while(True):
                print("type 1 for MoneyWithdrawl")
                print("Press 2 for Money Deposit")
                print("Press 3 for your Rate of Intrest")
        
                self.x = int(input())
                if(self.x == 1): 
                    self.i = int(input("Enter Amount"))
                    self.__Withdrawl(self.i)   

                elif(self.x == 2):
                    self.b = int(input("Enter Amount To Deposit"))
                    self.__Deposit(self.b)

                elif(self.x == 3):
                    self.CalculateIntrest()

                else:
                    print("Closing")
                    break
                    
              


def main():
    obj1 = BankAccount("Pranav",1000)
    obj2 = BankAccount("Ayan",2000)
    obj3 = BankAccount("Rohit",3000) 

    obj1.Display() 

if __name__ == "__main__":
    main()