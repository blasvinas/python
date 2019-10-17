#Shows how to work with files

#List files in current directory
import os
for file in os.listdir('.'):
    print(file)

#Write/Read to/from a file
test1 = "This is a teast of the emergency text system"
with open("test.txt", "wt") as fout:
    print(test1, file=fout)

with open("test.txt","rt") as fin:
    test2 = fin.read()
print(test2)
