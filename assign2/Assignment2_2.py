
def Pattern(x):
   for i in range(x):
      for j in range(x):
         print("*",end="    ")
      print("\n")


def main():
   i = int(input("Enter the number"))
   Pattern(i);






if __name__ == "__main__":
  main();

