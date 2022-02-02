class BookStore:
    NoOfBooks = 0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.name,"By", self.author)
        print( "No of Books are : ",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programing", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programing","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":  
    main() 