
def printstar(y):
    if(y == 0):
        return
    print("*",end = "\t")
    y -= 1
    printstar(y)

def main():
    x = int(input())
    printstar(x)


if __name__ == "__main__":
    main()