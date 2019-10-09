#Read the whole file
with open("file.txt") as f:
    content = f.read()
    print(content)

#Read line by line
with open("file.txt") as f:
    for line in f:
        print(line.strip())


with open("guests.txt","w") as f:
    name = ""
    while name != "quit":
        name = input("Enter your name or quit to exit: ")
        if name != "quit":
            f.write(name + '\n')

with open("guests.txt") as f:
    for guest in f:
        print(guest.strip())
