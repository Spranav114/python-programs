def fact(x):
    if(x == 0):
        return 1
    return (x * (fact(x-1))) 


def main():
    y = int(input())
    a = fact(y)
    print(a)


if __name__ == "__main__":
    main()
