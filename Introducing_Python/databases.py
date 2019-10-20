#Shows how to use databases
import sqlite3, csv

#Create the database
conn = sqlite3.connect("books.db")
curs = conn.cursor()
# curs.execute('''CREATE TABLE books
#     (title varchar(30) primary key,
#      author varchar(30),
#      year varchar(4))''')

#Read a csv file
with open("books2.csv","rt") as fin:
    cin = csv.DictReader(fin, fieldnames=["title","author","year"])
    books = [row for row in cin]

#Insert books into the database
for book in books:
    # print(f"Title: {book['title']}. Author: {book['author']}. Year: {book['year']}")
    ins = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
    conn.execute(ins, (book['title'], book['author'], book['year']))

#Query books
curs.execute("SELECT * FROM books ORDER BY year")
for row in curs.fetchall():
    print(row)

#close the cursor and the connection    
curs.close()
conn.close()