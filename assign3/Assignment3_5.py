import MarvellousNum as M;


def main():
   sum = 0
   n = int(input("Enter the number of numbers you want to enter"))
   list = []
   for i in range(n):
      x = int(input(""))
      list.insert(i,x)

 
   sum = M.chkprime(list)
   print(sum)
if __name__ == "__main__":
  main();

