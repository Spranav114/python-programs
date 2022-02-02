class Demo:
    variable = 10
    def __init__(self,a,b):
        self.a = a
        self.b = b
        

    def Fun(self):
        print(self.a) 
        print(self.b)

    @classmethod
    def Gun(cls):
        print(Demo.variable)

def main():
    obj1 = Demo(11,22)
    obj1.Fun()
    print(obj1.a)
    print(obj1.b)
    Demo.Gun()

if __name__ == "__main__":
    main()    