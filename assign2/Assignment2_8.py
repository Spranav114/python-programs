
def Pattern(x):
   y = 1;
   for i in range(0,x):
      y = 1;
      for j in range(0,x):
         if(i >= j):
           print(y,end="  ")
         y += 1
      print("\n")


def main():
   i = int(input("Enter the number"))
   Pattern(i);






if __name__ == "__main__":
  main();

