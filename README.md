# Python Notes
This file has some basic notes about how to use Python

* [Variables](#variables)
* [Numbers](#numbers)
* [if](#if)
* [Strings](#strings)
* [Loops](#loops)
* [Tuples](#tuples)
* [Lists](#lists)
* [Dictionaries](#dictionaries)
* [Sets](#sets)
* [Functions](#functions)

# Variables
In python variable a just references to an object in memory.  For example:

```python
 x = 7
 y = x
 ```


The first line creates a integer object in memory and then makes x refers to it.  The second line makes y refers to the same object.

# Numbers
* Booleans
* Intergers
* Floats

## Booleans
The boolean values are True and False. Nonzero numbers are considered True, zero-value are considered False.

## Integers
You can start an interger with 0b for binary, 0o for octal, and 0x for hexadecimal.

You can use underscores to improve readability.  For example 1_000_000  is the same than 1000000

### Operators

| Operator  | Description       | Example   | Result    |
|:--------- | :---------------- | :-------- | :-------- |
| +         | Addition          | 2 + 3     | 5         |
| -         | Substraction      | 20 - 5    | 15        |
| *         | Multiplication    | 9 * 4     | 36        |
| /         | Floating Division | 10 / 4    | 2.5       |
| //        | Integer Division  | 9 // 4    | 2         |
| %         | Modulus           | 9 % 4     | 1         |
| **        | Exponentiation    | 2 ** 3    | 8         |

## Type Conversions

To conver data type to an integer iuse int().  For example:

```python
bool(1) # True
bool(0) # False
int(10.3)  # 10
int(1.0e3) # 1000
int('23')  # 23
float(20) # 20.0
float('50.5') # 50.5
```

## Example using numbers
```python
# Calculate how many seconds are in an hour
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = minutes_per_hour * seconds_per_minute
print(f'The number of seconds in an hour is {seconds_per_hour}')

# Calculate the numbers of seconds in a day
hours_per_day = 24
seconds_per_day = hours_per_day * seconds_per_hour
print(f'The number of seconds in a day is {seconds_per_day}')

# Calculate the hours in a day using seconds_per_hour and seconds_per_day
print(f'The number of hours in a day are: {seconds_per_day / seconds_per_hour}')
```

# if, elif, and else

Below are some of the code structures using if

```python
if condition:
    statement1
    statement2
    ...

if condition:
    statements
else:
    statement

if condition:
    statements
elif condition:
    statements
else:
    statements
```

## Comparison operators

| Operator  | Description           |
| --------- | --------------------- |
| ==        | equality              |
| !=        | inequality            |
| <         | less than             |
| <=        | less than or equal    |
| >         | greater than          |
| >=        | greater than or equal |

## Logical operators

* and
* or
* not

If you have multiple and operation using one variable, Python let you do this:

```python
2 < y < 8 # The same as 2 < y and y < 8
```

## False values
 The following are consided false

 * None
 * 0
 * 0.0
 * ''
* []
* {}
* set()

## multiple comparisons with in

You can do multiple comparisons using in.  For example:

```python
number in [1, 2, 3 ,4 ,5]
```

## Walrus operator
 The walrus operator let you combine assigment and conditional test.  For example:

```python
if number := x - y > 0:
    print('Positive')
else:
    print('Negative')
```
## Example usinfg if - elif - else

```python
secret = 5
guess = 2

if secret > guess:
    print('Too low')
elif secret < guess:
    print('Too high')
else:
    print('Just right')
```
# Strings
In Python, string are immutable.  

You can use single or double quotes for your string.  For example:

* 'This is a sample string'
* "This is a sample string"

Also you can use triple quotes strings using either ''' or """.  This is use for multi-liner strings.  For example:

```python
s = '''This is a 
    string containing 
    multiple
    lines
```

## f-strings
You can format string using f or F  For example:

```python
a = 5
b = 10
c = a + b
s = f'The sum of {a} + {b} is {c}' # 'The sum of 5 + 10 is 15'
```

You can add padding to the left, center or righ, using a specific character.  For example:

```python
name1 = 'Blas'
name2 = 'Yady'
name3 = 'Natalia'
f'Name1: {name1}. Name2: {name2}.  Name3: {name3}'                  # 'Name1: Blas. Name2: Yady.  Name3: Natalia'
f'Name1: {name1:>10}. Name2: {name2}.  Name3: {name3}'              # 'Name1:       Blas. Name2: Yady.  Name3: Natalia'
f'Name1: {name1:>10}. Name2: {name2:^10}.  Name3: {name3:<10}'      # 'Name1:       Blas. Name2:    Yady   .  Name3: Natalia   '
>>> f'Name1: {name1:>10}. Name2: {name2:.^10}.  Name3: {name3:<10}' # 'Name1:       Blas. Name2: ...Yady....  Name3: Natalia   '
```
if you want to print the variables names and its value, yo can use {variable_name=}.  For example:

```python
f'{name1=}. {name2=}. {name3=}' # "name1='Blas'. name2='Yady'. name3='Natalia'"
```
## Raw Strings
You can start a string with r or R to create a raw string.  Raw string  prevent escape sequences.  For example"

```python
s = r'Use \n to add a new line'  # 
print(s) # Use \n to add a new line
```

## Convert to string

You can convert other type to string using the str() function.  For example:

```python
str(20.6)  # '25.6'
str(False) # 'False'
```
## Concatenate strings

You can concanenatestring using +.  For example:

```python
a = 'Hello'
b = 'World!'
s = a + ' ' + b
print(s) #Hello World!
```
## Duplicate a string

You can duplicate a string using *.  For example:

```python
>>> a = 'Hello'
>>> s = a * 5
>>> print(s) # HelloHelloHelloHelloHello
```
## Get individual characters
You can use [] to get individual characters from strings.  For example:

 ```python
s = '123456789'
s[0] # '1'
s[1] # '2'
s[-1] # '9'
s[-2] # '8'
s[5] # '6'
 ```
## Substrings

You can get a substring using slice.  You define a slice using [], start, end, and step.  
* [:] The whole string
* [start:]  from start to the end
* [: end] from the beginning to one before end
* [start : end] from start to one before end
* [start: end: step] from start to one before end, skipping character by step.

Examples:

```python
s = '123456789'
s[:] #'123456789'
s[3:] # '456789'
s[:5] # '12345'
s[::2] #'13579'
s[-1::-1] #'987654321'
```
## Common string functions

### len()
You can get the length of a string using len() for example:

```python
s = '123456789'
print(len(s)) # 9
```
### split()
split() takes a string a retuen a list of smaller string based on the separator.  For example:

```python
s = 'one, two, three, four, five'
s.split(',') # ['one', ' two', ' three', ' four', ' five']
```

### join()
join() is the opposite of split.  It takes a list and retun a string with each item separated by the specified separator.  For example:

```python
list = ['one', ' two', ' three', ' four', ' five']
s = ','.join(list) # 'one, two, three, four, five'
```
### replace()
Use replace() to substitute a part of a string with another. The sytanx is replace(old string, new string, how many instances) For example:

```python
s = 'I like C++ programming'
s.replace('C++','Python') # 'I like Python programming'
```
If you omit the number of instances, it only replace the first one.

### strip()

You can remove whitesapces or other chararter from the begining or the end of a string using strip().  If you do not specify any parameters, whitespaces ill be remove.  You can specify other charaters.  lstrip() remove only from the left, and rstrip() just from ther right.  For example:

```python
s = '         Hello      '
s.strip() # 'Hello'
s.lstrip() # 'Hello      '
s.rstrip() # '         Hello'

>>> string.whitespace
' \t\n\r\x0b\x0c'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> s = '>>>>Hello Word !!!!.'
>>> s.strip(string.punctuation)
'Hello Word '
```

### startwith() and endswith()
You you want to check if a string starts or ends with a prticular substring you can use startswith(substring) or endswith(substring).  For example:

```python
s = 'Hello world, Python programmers!!!'
s.startswith('Hello') #True
s.endswith('!!!') #True
```

### find() and index()
Use find(substring) or index(substring) to find the position of the first occurence of the substring.  If you need to start from the end use rfind() or rindex().  For example:

```python
>>> s = 'Hello world, Python programmers!!!'
s.find('Python') # 13
s.index('Python') # 13
```

If the substring is not found, find will retuern -1, but index will return an exception.

### Case functions

* capitalize() capitalize the first letter of the string.
* title() capitalize ther first letter of each word.
* upper() covert all characters to uppercase.
* lower() convert all characters to lowercase.
* swapcase()  swap uppercase and lowercase.

### alignment
You can align center, left or right with the specified number of spaces.  For example:

```python
s.center(50)    # '        Hello world, Python programmers!!!        '
s.ljust(50)     # 'Hello world, Python programmers!!!                '
s.rjust(50)     #'                Hello world, Python programmers!!!'
```

## Example using strings
```python
# How to work with strings

#Print the string, lowercase, uppcase and title
name = "Blas vinas"
print(f'Hello {name}')
print(name.upper())
print(name.lower())
print(name.title())

text = '   Text with spaces at the begining and the end    '
print(text)
print(text.rstrip())
print(text.lstrip())
print(text.strip())

# Capitalize the word starting with m

song = "When an ell grabs your arm, and it causes great harm, that's - a moray!"
index = song.find(' m')
if index != -1:
    new_song = song[:index] + ' M' + song[index+2:]
    print(new_song)
else:
    print('There are no words sarting with m')
```

# Loops

Python has two choices for loops:  while and for.

## while

Below is an example of a while loop the prints the numbers from 1 to 5.

```python
n = 1
while n <=5:
    print(n)
    n += 1
```

You can cancel a loop with break or skip until the next iteration with continue.  Below is an example of a  infinite while loop that stops when the udse enters 'q'.

```python
>>> while True:
...     s = input('Enter a string to ve converted to uppercase or q to quit')
...     if s == 'q':
...             break
...     print(s.upper())
```

The following example uses continue to skips the odd numbers and only prints the even ones.

```python
n = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n)
```

You can use else with break.  If no break if called, the statements that belong to the else block will be executed.  For example:

```python
numbers = [1, 4, 8, 9]
n = 1
count = len(numbers)
while n < count:
    if numbers[n] < 0:
            break
    n += 1
else:
    print('No negatives numbers were found')
```

## for

You can use for with in to traverse string and some data structures like list, tuples and dictionaries.   The following example prints the letters of a string one at the time.

```python
 s = 'Hello world!'
 for c in s:
    print(c)
```

You can use continue, break and else the same way explaned about for the while loop.

### range()
range() us frequently used for for loops.  rage() will return a stream of numbers within the specified range.  The syntax in range(start, stop, step).  This will generate a stream start at starty until stop - 1 and skippig the nuber specified by step.  For example:

```python
range(0,5) # 0,1,2,3,4
range(5,-1,-1) # 5,4,3,2,1,0

# prints numbers from 0 to 9
for x in range(1,10):
    print(x)
```
# Tuples

Tuple is a immutable sequence structure.  Each item in the tuple can be any Python object.

You create tuples using ().  For example:

```python
t = ()  # Empty tuple
days = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
year = (2020, ) # one element tuples must include the comma at the end.
```

You can convert other structures to tuple using the tuple() function.  For example:
```python
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
```
You can combine tuples using +.  For example:
```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
```

You can duplicate a tuple using *.  For example:
```python
t = (1, 2, 3)
t * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

# Lists

List are similar to tuples but the big difference is that list are mutable.

You create a list using [].  For example:

```python
l = [] # empty list
numbers = [1, 2, 3, 4, 5]
```

You can convert other typles to a list using the list() function.  For example:

```python
my_tuple = ('a', 'b', 'c', 'd')
my_list = list(my_tuple)
```

You can use an index to access individual elements of a list.  For example:

```python
numbers = [1, 2, 3, 4, 5]
numbers[1] # 2
numbers[-1] # 5
```

You can also use slices.  Check strings for more information about slices.

## List common functions

### reverse()
reverse() reverses a list in place.  For example:
```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse() # [5, 4, 3, 2, 1]
```

### append()

append() adds an element at the end of the list.  For example:

```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6) # [1, 2, 3, 4, 5, 6]
```

### insert()

insert() add an element before the specified position.  For example:

```python
my_list = [1, 2, 3, 4, 5]
my_list.insert(2,10) # [1, 2, 10, 3, 4, 5, 6]
```

### Change items with slice

You can change the items in a list using slices.  Fr example:

```python
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [7, 8] # [1, 7, 8, 4, 5]
my_list[2:4] = [10, 11, 12, 13] #[1, 7, 10, 11, 12, 13, 5]
```
### del

del deletes ther specified element.  For example:

```python
my_list = [1, 2, 3, 4, 5]
del my_list[3] # [1, 2, 3, 5]
```

### remove()

You can remove an item by  value using remove().  For example:

```python
my_list = ['one', 'two', 'three', 'four']
my_list.remove('three') # ['one', 'two', 'four']
```

### pop()

pop() removes an item from the list and return its value. pop() without paremeters use -1.  For example:

```python
my_list = ['one', 'two', 'three', 'four']
n = my_list.pop() # n = 'four'. my_list = ['one', 'two', 'three'] 
>>> n = my_list.pop(1) # n = 'two'. my_list = ['one', 'three']
```

### clear()

Delete all elements in a list.  For example my_list.clear().

### index()

index() return the first  index of the specify value.   If the value does not exist, you get an exception.  For example:

```python
my_list = ['one', 'two', 'three', 'four']
my_list.index('two') # 1

my_list.index('five')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'five' is not in list
```

### in

in returns True is the element exist in the list.  For example:

```python
my_list = ['one', 'two', 'three', 'four']
'three' in my_list # True
```

### count()

count() counts the number of ocurrences of a value.  For example:

```python
my_list = ['one', 'two', 'three', 'four', 'two']
my_list.count('two') # 2
```

### sort() and sorted()

sort() sorts a list in place.  sorted() return a new sorted list.  For example:

```python
my_list = [4, 2, 6, 1, 3]
my_list.sort() # [1, 2, 3, 4, 6]
my_list = [4, 2, 6, 1, 3]
new_list = sorted(my_list) # new_list = [1, 2, 3, 4, 6]. my_list =  [4, 2, 6, 1, 3]
```
###  len()

len() returns the length of the list.  For example len(my_list).

### copy()

When you assign a list to more than one variable, changes using one variable also change the other.  For example:

```python
a = [1, 2, 3]
b = a
a[0] = 4 # b = [4, 2, 3]
```

Use copy to make a  copy of the list.  For example:

```python
a = [1, 2, 3]
b = a.copy()
>>> a[0] = 4 # a = [4, 2, 3]. b = [1, 2, 3]
```

### deepcopy()

copy() make a shallow copy, which means that if the list have mutable items, if you change them in the original  variavble, it will change the copies.  For example:

```python
a = [1, 2, [6, 7]]
b = a.copy()
a[2][1]=8 # a = [1, 2, [6, 8]]. b = [1, 2, [6, 8]]
```

To avoid this you need to use deepcopy().  For example:

```python
import copy
a = [1, 2, [6, 7]]
b = copy.deepcopy(a)
a[2][1]=8 # a = [1, 2, [6, 8]]. b = [1, 2, [6, 7]]
```

### zip()

You can iterate multipe sequences using zip().  For example:

```python
numbers = ['one','two','three']
numeros = ['uno','dos','tres']
for number, numero in zip(numbers, numeros):
    print(f'{number} , {numero}')
# one , uno
# two , dos
# three , tres
```

If the list are not the same length, zip() will stop with the shortest one.

## List Comprehension

You can create list using list comprenhension.  The sytam is: [expression for item in iterable if condition].  For example:

```python
even = [number for number in range(0,11) if number %2 == 0] # [0, 2, 4, 6, 8, 10]
```

## Example using lists

```python
#Create a list with numbers in words
my_list = ['one','two','three','four']

#Create a new list using list comprehension with item capitalized
new_list = [number.capitalize() for number in my_list]
print(new_list)

#Create a new list sprted alphabetically
new_list = sorted(my_list)
print(new_list)

#add a element to the list
my_list.append('five')
print(my_list)

#Delete the first item
del my_list[0]
print(my_list)
```

# Dictionaries

A dictionary a sequence of key-value pairs.  They are mutable.

You can create a dictionary with {}.  For example:  

```python
my_dict = {}
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday"}
```
Also you can use the dict() function to create a dictionary or convert other structures to a dictionary.  For example:

```python
my_list = [[1, "Monday"], [2, "Tuesday"], [3, "Wednesday"]] # [[1, 'Monday'], [2, 'Tuesday'], [3, 'Wednesday']]
my_dict = dict(my_list) # {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday'}
```

## Dictionaries common functions

### Add or change an item by key

To add an item to a dictionary refer to the item by its key and assign a value.  If the item already exist, the existing value will be replaced.  For example:

```python
my_dict = {"one": "uno", "two": "dos", "three": "tres"}
my_dict["four"] = "cuatro"
my_dict # {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro'}
```

### Get an Item by Key

You can get an item specifying the dictionary and the key.  If the key does not exist, you will get an exception.  For example:

```python
my_dict = {"one": "uno", "two": "dos", "three": "tres"}
my_dict["two"] # "dos"
```

To avoid getting an exception, you can use the get() function.  The function does not return anything is the key does not exist.  Optionally, you can specify a default value to return if the key does not exist.  For example:

```python
my_dict.get("five") # none
my_dict.get("five","Not found") # 'Not found'
my_dict.get("one","Not found") # 'uno'
```

### keys(), values(), and items()

You can get all the keys with the keys() function and all the values with the values() function.  For example:

```python
my_dict = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro"}
my_dict.keys() # dict_keys(['one', 'two', 'three', 'four'])
my_dict.values() # dict_values(['uno', 'dos', 'tres', 'cuatro'])
```
keys() and values() return dict_keys(), which is an iterable view  of the keys and values.  If you need a list you need to convert it using list(my_dict.keys())

You can get all the key-value pair using items(). items() returns a dict_items view of tuples with the key-value pairs.  For example:

```python
my_dict = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro"}
my_dict.items() # dict_items([('one', 'uno'), ('two', 'dos'), ('three', 'tres'), ('four', 'cuatro')])
```

### len()

You can get the lenght of a dictionary using len().  For example: len(my_dict)

### Combine dictionaries

You can combine several dictionaries using **.  For example:

```python
a = {1: "one", 2: "two"}
b = {3: "three", 4: "four"}
c = {5: "five", 6: "six"}
d = {**a, **b, **c} # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
```
Also you can combine dictionaries with update().   For example:

```python
a = {1: "one", 2: "two"}
b = {3: "three", 4: "four"}
a.update(b) #  a = {1: 'uno', 2: 'two', 3: 'three', 4: 'four'}
```

### del

You can delete an item from a dictionary using del.  For example del my_dict["one"]

### pop()

pop() takes a key as an argument and return the value and delete the item.  If the key does not exist, it raises an exception.  For example:

```python
my_dict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro'}
v = my_dict.pop("three")
# v = 'tres'
# my_dict = {'one': 'uno', 'two': 'dos', 'four': 'cuatro'}
```

### clear()

clear() deletes all the items in the dictionary.  For example:  my_dict.clear().

### in

You can test if a key exist in a dictionary using in.  For example:  "one" in my_dict

### copy() and deepcopy()

These two functions work in a similar way than list.  Please check them in the list section for more details.

### Compare dictionaries

You can compare dictionaries using == and !=.  Python compares if each key-value pair from one dictionary is present in the other one.  The order of then keys is not important.

## Iterate over a dictionary

Iterating over a dictionary usinfg in returns the keys.  For example:

```python
 my_dict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro'}
 for value in my_dict:
     print(value)

# one
# two
# three
# four
```

Also you can use iterate using items as shown in the example below.

```python
for key, value in my_dict.items():
    print(key, value)
# one uno
# two dos
# three tres
# four cuatro
```
## Dictionary comprehensions

Dictionaries also have comprenhensions similar to list. The syntax is {key_expression, value_expression for expression in iterable if condition }  For example:

```python
names = ['john','Katy','Chris','Nancy']
my_dict = { names.index(name) + 1  : name  for name in names } # {1: 'john', 2: 'Katy', 3: 'Chris', 4: 'Nancy'}
```

## Example usinf dictionaries

```python
 Create an English-French dictiorary

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(f"Walrus in French is {e2f['walrus']}")

#  Create a French to English dictionary

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
```

# Sets

The items in a set must be unique.  Sets are unordered and mutsble.  You can create set using set().  For example:

```python
my_set = set() # set()
my_set = {1,2,3,4,5} # {1, 2, 3, 4, 5}
```
You can covert other structure to sets using set().  For example:

```python
my_list = [1,2,3,4,5]
my_set = set(my_list) # {1, 2, 3, 4, 5}
```

## Common Set Functons

### len()

You can get the length of a set using len().  For example:  len(my_set).

### add()

You can add a item to a set using add().  For example:

```python
my_set = {1,2,3,4,5}
my_set.add(6) # {1, 2, 3, 4, 5, 6}
```
### remove()

You can remove an item from a set using remove().  For example:

```python
my_set = {1,2,3,4,5}
my_set.remove(3) # {1, 2, 4, 5, 6}
```

### in

You can check if an item is in a set using in.  For example 4 in my_set.

### Operators

#### Intersection (&)

You can get the intersection of two sets using the & operator.  For example:

```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1 & s2 # {4, 5}
```

#### Union (|)

You can get the union of two sets using the | operator.  For example:

```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1 | s2 # {1, 2, 3, 4, 5, 6, 7, 8}
```

#### diference() (-)

To get the difference between to sets use difference() or the  - operator.  For example:

```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.difference(s2) # {1, 2, 3}
s1 - s2 # {1, 2, 3}
```

#### Exclusive or (^)

You can get the exclusive or using the ^ operator.  For example:

```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1 ^ s2 # {1, 2, 3, 6, 7, 8}
```

#### Subset

You can find if a set is a subset of another ser using issubset() or the <= operator.  For example:

```python
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s1 <= s2 # True
s1.issubset(s2) # True
```

You if need to now if a set is a proper subset (the second set needs to have al members of the first and more) use <.

#### Superset

You can find if a set is a superset of another ser using issuperset() or the >= operator.  For example:

```python
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s2 >= s1 # True
s2.issuperset(s1) # True
```

You if need to now if a set is a proper superset (the first set needs to have al members of the second and more) use >.

## Set Comprehensions

You can use set comprehension in a similar one that you use it with other structures.  The syntax is: { expression for expression in iterable if condition } . For example:

```python
my_set = { number * 2 for number in range(0, 11) if number %2 == 0} # {0, 4, 8, 12, 16, 20}
```

## Immutable Sets

You can create immutable sets using frozenset.  For example:  fs = frozenset([1, 2, 3])

## Example using sets

```python
# Create a set with odd number using comprehensions
odd_numbers = { number for  number in range(0,10) if number % 2 != 0}
print(odd_numbers)

#Create a set with the even numbers using comprehension
even_numbers = { number for number in range(0, 11) if number % 2 == 0}
print(even_numbers)

#Get the union between odd_numbers and even_numbers
numbers = even_numbers | odd_numbers
print(numbers)
```

# Functions

In Python you define a function using def, followed by the name of the function and then parenthesis with zero or more parameters inside.  Also, function might return zero ort more values.  For example:

```python
# This function takes zero paramenters and return zero values
def f1():
    pass

# This function takes one parameter but it does not return any values
def f2(message):
    print(message)

# This function takes one parameter and returns one value
def f3(number):
    return number * 2
```

