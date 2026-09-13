# Book Manager Project in Python

This is a simple **Book Manager** project made using Python. I created this project to practice basic Python concepts such as functions, loops, conditional statements, exception handling, JSON, file handling, and lists/dictionaries.

## What can it do?

The program allows you to:

* Show all books
* Add a new book
* Update an existing book
* Delete a book
* Save books in a file
* Load the saved books when the program starts

Each book contains:

* Book title
* Author name
* Number of pages

## How it works

The program stores the book data in a file called `Book.txt` using JSON.

When the program starts, it loads the existing books from the file. Whenever a book is added, updated, or deleted, the data is saved again.

If the `Book.txt` file does not exist, the program simply starts with an empty book list.

## Python Concepts Used

Some of the main concepts I used in this project are:

* Functions
* `while` loop
* `if-elif-else`
* Lists
* Dictionaries
* `for` loop
* `enumerate()`
* User input
* `try-except`
* JSON
* File handling
* `json.load()`
* `json.dump()`

## How to Run

Make sure Python is installed on your computer.

Then run:

```bash
python main.py
```

The program will show a menu like:

```text
-----------Book Manager-----------
1.    Show All Books
2.    Add Book
3.    Update Books
4.    Delete Books
5.    Exit
```

Choose an option by entering its number.

## Project Purpose

The main purpose of this project was to practice Python fundamentals by making something that works like a small real-world application instead of only practicing separate coding questions.

This is a basic project, and I plan to improve it as I learn more Python.
