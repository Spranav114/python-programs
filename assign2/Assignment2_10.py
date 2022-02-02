
def Digit(x):
   y = 0
   while(x % 10 != 0):
       y = y + (x%10)
       x = x // 10
   return y



def main():
   i = int(input("Enter the number"))
   count = Digit(i);
   print("Addition of Number of digits in the number is :",count)




if __name__ == "__main__":
  main();

