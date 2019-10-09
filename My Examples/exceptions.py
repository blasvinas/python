while True:
    print("Enter 2 number to be added.  Enter q to quit")
    num1 = input("Enter the first number or q to quit: ")
    if num1 == 'q':
        break
    num2 = input("Enter the seond number or q to quit: ")
    if num2 == 'q':
        break

    try:
        n1 = int(num1)
        n2 = int(num2)
        result = n1 + n2
        print("{} + {} = {}".format(n1,n2,result))
    except ValueError:
        print("Please enter Integer numbers")