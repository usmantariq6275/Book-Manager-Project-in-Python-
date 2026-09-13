import json
def load_data():
    try:
         with open("Book.txt","r") as file:
              return json.load(file)
    except FileNotFoundError:
         return []
def save_data_helper(books):
     with open("Book.txt","w") as file:
          json.dump(books,file,indent=4)
def show_books(books):
     if len(books)==0:
          print("No Book Added!!!(Add Book First)")
          return
     print("----Books List----")
     for index,books in enumerate(books,start=1):
          print(f"{index}.")
          print(f"Tittle:{books['name']}")
          print(f"Author:{books['author']}")
          print(f"Pages:{books['pages']}")
          print("\t---------")
def add_books(books):
     name=input("Enter Tittle of the Book:")
     author=input("Enter Name of The Author:")
     pages=input("Enter Pages of the Book:")
     books.append({"name":name,"author":author,"pages":pages})
     save_data_helper(books)
     print("Books Added Successfully!")
def update_books(books):
     if len(books)==0:
               print("No Book Added!!!(Add Book First)")
               return
     show_books(books)
     try:
        index=int(input("Enter Book Number you want to Update:"))
        if (index<=0 or index>len(books)):
            print("Invalid Number!")
            return
        name=input("Enter New Tittle of The Book:")
        author=input("Enter New Author of The Book:")
        pages=input("Enter New Pages of The Book:")
        books[index-1]={"name":name,"author":author,"pages":pages}
        save_data_helper(books)
        print("Books Updated Successfully!")
     except ValueError:
          print("Invalid Number!")
def delete_books(books):
    if len(books)==0:
        print("No Book Added!!!(Add Book First)")
        return
    show_books(books)
    try:
        index=int(input("Enter Book Number you want to Delete:"))
        if (index<=0 or index>len(books)):
            print("Invalid Number!")
            return
        books.pop(index-1)
        save_data_helper(books)
        print("Book Deleted Successfully!")
    except ValueError:
         return
def main():
    books=load_data()
    while True:
        print("-----------Book Manager-----------")
        print("1.\tShow All Books")
        print("2.\tAdd Book")
        print("3.\tUpdate Books")
        print("4.\tDelete Books")
        print("5.\tExit(Press any key except 1-3)")
        print("\t------------")
        try:
            ch=int(input("Enter your choice:"))
        except ValueError:
             print("Invalid Number!")
             continue
        if ch==1:
            print("You Selected To Show All the Books!")
            show_books(books)
        elif ch==2:
             print("You Selected to Add a Book!")
             add_books(books)
        elif ch==3:
            print("You Selected to Update the Books!")
            update_books(books)
        elif ch==4:
                print("You Selected to Delete the Books!")     
                delete_books(books)
        else:
             print("Exiting............!")
             break
if __name__=="__main__":
    main()

