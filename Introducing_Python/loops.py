#while loop
i = 0
while i <= 5:
    print(i)
    i += 1

#The same with for and range
for i in range(0,6):
    print(i)

#break and continue

d  = -1
while d != 0:
    d = int(input("Enter a number between 1 and 9.  0 to exit.  Only odd numbers will be print out:  "))
    if d == 0:
        break
    if d%2 == 0:
        continue
    print(d)

#Using else with for (Also works with while).

odd_numbers = [1,3,5,7,9]
for i in odd_numbers:
    if i % 2 == 0:
        print("Oops.  It was supposed to be only odd numbers.")
        break
    print(i)
else: # runs if the loop finished normally without break
    print("No odd numbers where found")

