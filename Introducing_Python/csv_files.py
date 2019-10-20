#Shows how to work with csv
import csv

#Read a csv file
with open("books.csv","rt") as fin:
    cin = csv.DictReader(fin, fieldnames=["author","book"])
    books = [row for row in cin]
print(books)

#Write to a csv file
books = [
    {'title': 'The Weirdstone of Brisingamen','author': 'Alan Garner','year':'1960'},
    {'title': 'Perdido Street Station','author': 'China Miéville','year':'2000'},
    {'title': 'Thud!','author': 'Terry Pratchett','year':'2005'},
    {'title': 'The Spellman Files','author': 'Lisa Lutz','year':'2007'},
    {'title': 'Small Gods','author': 'Terry Pratchett','year':'1992'},
]

with open("books2.csv","wt") as fout:
    cout = csv.DictWriter(fout,['title','author','year'])
    cout.writeheader()
    cout.writerows(books)