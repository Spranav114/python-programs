
def Minimum(x,y):
   count = 0  
   list = []
   for i in range(x):
     No = int(input())
     list.insert(i,No)
     if(list[i] == y):
        count += 1
     i += 1
   return count

def main():
   i = int(input("Enter the number of numbers you want to add"))
   j = int(input("Enter the number"))

   fre = Minimum(i,j)
   print("Frequency of the given number is :",fre)



if __name__ == "__main__":
  main();

