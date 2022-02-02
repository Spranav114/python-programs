
def Pattern(x):
   for i in range(x,0,-1):
      for j in range(0,i):
         print("*",end="  ")
      print("\n")


def main():
   i = int(input("Enter the number"))
   Pattern(i);






if __name__ == "__main__":
  main();

