
def Maximum(x):
   imax = 0  
   list = []
   for i in range(x):
     No = int(input())
     list.insert(i,No)
     i += 1
   imax = list[0]
   for i in range(x):
      if(imax <= list[i]):
        imax = list[i]        
   return imax   

def main():
   
   i = int(input("Enter the number of numbers you want to add"))
   max = Maximum(i)
   print("Maximum number is :",max)



if __name__ == "__main__":
  main();

