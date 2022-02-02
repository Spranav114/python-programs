
def Chknum(j):
   if(j > 0):
     print("Positive Number")
   elif(j < 0):
     print("Negative number")
   elif(j == 0):
     print("Zero")

def main():
   i = int(input("enter the number"))
   Chknum(i);
 


if __name__ == "__main__":
  main();

