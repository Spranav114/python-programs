
def Minimum(x):
   imin = 0  
   list = []
   for i in range(x):
     No = int(input())
     list.insert(i,No)
     i += 1
   imin = list[0]
   for i in range(x):
      if(imin >= list[i]):
        imin = list[i]        
   return imin   

def main():
   i = int(input("Enter the number of numbers you want to add"))
   min = Minimum(i)
   print("Minimum number is :",min)



if __name__ == "__main__":
  main();

