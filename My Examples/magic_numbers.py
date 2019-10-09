magic_numbers = [3,9]
changes = 3
for attempt in range(changes):
    print ("Attempt number: " + str(attempt + 1))
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You go it right")
    else:
        print("You got it wrong")

    
