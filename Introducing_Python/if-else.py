secret = 8
guess = 0
while guess != secret:
    guess = int(input("Enter a number between 1 and 10 "))
    if guess == secret:
        print("You got it")
    elif guess > secret:
        print("Too high")
    else:
        print("Too low") 