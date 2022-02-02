
def Chkprime(x):
   count = 0;
   for i in range(x):
      if(i == 0):
        continue;
      elif(i == 1):
        continue;
       #print(count)
      if(x % i == 0):
       count = count + 1; 
  
   return count;      



def main():
   i = int(input("Enter the number "))
   num = Chkprime(i);
   if(num == 0):
     print("number is prime");
   else:
     print("Number is not prime")


if __name__ == "__main__":
  main();

