class Circle:
    PI = 3.14
    def __init__(self):
         self.radius = 0.0
         self.CalArea = 0.0
         self.Circum = 0.0

    def Accept(self):
        x = float(input("Enter the radius"))
        self.radius = x

    def Area(self):
        self.CalArea = (Circle.PI) * (self.radius) * (self.radius)
        return (self.CalArea) 

    def Circumference(self):
        self.Circum = 2 * (Circle.PI) * (self.radius)           
        return (self.Circum)
    
    def __del__(self):
        print("Inside Destructor")

def main():
    obj1 = Circle()
    print(Circle.PI)

    obj1.Accept()
    ret = 0.0

    ret = obj1.Area()
    print(ret)

    
    ret = obj1.Circumference()
    print(ret) 

if __name__ == "__main__":
    main()