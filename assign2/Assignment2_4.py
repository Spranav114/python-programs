
def fact(x):
   sum = 0;
   for i in range(x):
      if(i == 0):
        continue;
      if(x % i == 0):
        sum = sum + i;
      if(x == x//6):
        break;
   return sum;


def main():
   i = int(input("Enter the number"))
   isum = fact(i);
   
   print(isum);


if __name__ == "__main__":
  main();

