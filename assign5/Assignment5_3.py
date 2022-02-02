class Arithematic:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0

    def Accept(self):
        self.v1 = int(input("Enter the first number"))
        self.v2 = int(input("Enter the second number"))    

    def Addition(self):
        return self.v1 + self.v2

    def Substraction(self):
        return self.v1 - self.v2

    def Multiplication(self):
        return self.v1 * self.v2

    def Division(self):
        x = self.v1
        y = self.v2
        ans = x/y
        return ans
    


def main():
    obj1 = Arithematic()
    obj1.Accept()
    print(obj1.Addition())
    print(obj1.Substraction())
    print(obj1.Multiplication())
    print(obj1.Division())
    print("HELLO")
    
if __name__ == "__main__":
    main()    

