def printstar(x):
    if(x == 1):
        return
    x -= 1    
    printstar(x)
    print(x,end = "\t")    


def main():
    y = int(input())
    printstar(y+1)


if __name__ == "__main__":
    main()
