class Arithematic:
    no = 0.0
    sum = 0
    def __init__(self,value):
        self.no = value
        self.sum = 0

    def chkprime(self):
        self.x = 0
        for i in range(2,self.no):
            if(self.no % i == 0):
                self.x += 1    
        if(self.x == 0):
            return True
        else:
            return False

    def Factors(self,x = 0):
        self.sum = 0
        self.fact = 0
        for i in range(1,self.no):
            if(self.no % i == 0):
                self.sum = self.sum + i
                print(i)

    def chkperfect(self):
        print(self.sum)
        print(self.no)
        if(self.sum == self.no):
            print("Number is perfect")
        else:
            print("Number is not perfect")    

    def factsum(self):
        print("Sum of Factors is :",self.sum)         



def main():
    x = int(input())
    obj = Arithematic(x)
    ret = obj.chkprime()
    obj.Factors()
    obj.chkperfect()
    obj.factsum()
    if(ret == True):
        print("Number is prime")
    else:
        print("Number is not prime")    


if __name__ == "__main__":  
    main() 