
def Facto(x):
   fact = 1;
   for i in range(x+1):
      if(i == 0):
        continue;
      else:
        fact = fact * i;
   print(fact);

def main():
   i = int(input("Enter the number"))
   Facto(i);






if __name__ == "__main__":
  main();

