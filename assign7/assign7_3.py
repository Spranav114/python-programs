def printstar(x):
    if(x == 0):
        return
    print(x,end = "\t")    
    x -= 1        
    printstar(x)


def main():
    y = int(input())
    printstar(y)


if __name__ == "__main__":
    main()
