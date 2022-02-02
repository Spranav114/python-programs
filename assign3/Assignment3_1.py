
def Addition(x):
   isum = 0  
   list = []
   for i in range(x):
     No = int(input())
     list.insert(i,No)
     isum = isum + list[i]
     i += 1
   return isum   

def main():
   sum = 0
   i = int(input("Enter the number of numbers you want to add"))
   sum = Addition(i)
   print("Addition is :",sum)



if __name__ == "__main__":
  main();

