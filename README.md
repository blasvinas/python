# Table of Contents

- [Table of Contents](#table-of-contents)
- [Variables](#variables)
  - [Numbers](#numbers)
  - [Booleans](#booleans)
  - [Integers](#integers)
    - [Operators](#operators)
  - [Type Conversions](#type-conversions)
  - [Example using numbers](#example-using-numbers)
- [if, elif, and else](#if-elif-and-else)
  - [Comparison operators](#comparison-operators)
  - [Logical operators](#logical-operators)
  - [False values](#false-values)
  - [multiple comparisons with in](#multiple-comparisons-with-in)
  - [Walrus operator](#walrus-operator)
  - [Example using if - elif - else](#example-using-if---elif---else)
- [Strings](#strings)
  - [f-strings](#f-strings)
  - [Raw Strings](#raw-strings)
  - [Convert to string](#convert-to-string)
  - [Concatenate strings](#concatenate-strings)
  - [Duplicate a string](#duplicate-a-string)
  - [Get individual characters](#get-individual-characters)
  - [Substrings](#substrings)
  - [Common string functions](#common-string-functions)
    - [len()](#len)
    - [split()](#split)
    - [join()](#join)
    - [replace()](#replace)
    - [strip()](#strip)
    - [startwith() and endswith()](#startwith-and-endswith)
    - [find() and index()](#find-and-index)
    - [Case functions](#case-functions)
    - [alignment](#alignment)
  - [Example using strings](#example-using-strings)
- [Loops](#loops)
  - [while](#while)
  - [for](#for)
    - [range()](#range)
- [Tuples](#tuples)
- [Lists](#lists)
  - [List common functions](#list-common-functions)
    - [reverse()](#reverse)
    - [append()](#append)
    - [insert()](#insert)
    - [Change items with slice](#change-items-with-slice)
    - [del](#del)
    - [remove()](#remove)
    - [pop()](#pop)
    - [clear()](#clear)
    - [index()](#index)
    - [in](#in)
    - [count()](#count)
    - [sort() and sorted()](#sort-and-sorted)
    - [len()](#len-1)
    - [copy()](#copy)
    - [deepcopy()](#deepcopy)
    - [zip()](#zip)
  - [List Comprehension](#list-comprehension)
  - [Example using lists](#example-using-lists)
- [Dictionaries](#dictionaries)
  - [Dictionaries common functions](#dictionaries-common-functions)
    - [Add or change an item by key](#add-or-change-an-item-by-key)
    - [Get an Item by Key](#get-an-item-by-key)
    - [keys(), values(), and items()](#keys-values-and-items)
    - [len()](#len-2)
    - [Combine dictionaries](#combine-dictionaries)
    - [del](#del-1)
    - [pop()](#pop-1)
    - [clear()](#clear-1)
    - [in](#in-1)
    - [copy() and deepcopy()](#copy-and-deepcopy)
    - [Compare dictionaries](#compare-dictionaries)
  - [Iterate over a dictionary](#iterate-over-a-dictionary)
  - [Dictionary comprehensions](#dictionary-comprehensions)
  - [Example using dictionaries](#example-using-dictionaries)
- [Sets](#sets)
  - [Common Set Functons](#common-set-functons)
    - [len()](#len-3)
    - [add()](#add)
    - [remove()](#remove-1)
    - [in](#in-2)
    - [Operators](#operators-1)
      - [Intersection (&)](#intersection)
      - [Union (|)](#union)
      - [diference() (-)](#diference)
      - [Exclusive or (^)](#exclusive-or)
      - [Subset](#subset)
      - [Superset](#superset)
  - [Set Comprehensions](#set-comprehensions)
  - [Immutable Sets](#immutable-sets)
  - [Example using sets](#example-using-sets)
- [Functions](#functions)
  - [Arguments](#arguments)
    - [Positional Arguments](#positional-arguments)
    - [Keyword Arguments](#keyword-arguments)
    - [Default Values](#default-values)
    - [Variable number of Arguments](#variable-number-of-arguments)
  - [Docstring](#docstring)
  - [Function are Objects](#function-are-objects)
  - [Inner Functions](#inner-functions)
  - [Closures](#closures)
  - [Lambda Functions](#lambda-functions)
  - [Generators](#generators)
    - [Generator Functions](#generator-functions)
    - [Generator Comprehensions](#generator-comprehensions)
  - [Decorators](#decorators)
  - [Namespaces and Scope](#namespaces-and-scope)
  - [__ in Names](#in-names)
- [Exceptions](#exceptions)

# Variables

In python a variable a just references to an object in memory.  For example:

```python
 x = 7
 y = x
 ```

The first line creates a integer object in memory and then makes x refers to it.  The second line makes y refers to the same object.

## Numbers

- Booleans
- Integers
- Floats

## Booleans

The boolean values are True and False. Nonzero numbers are considered True, zero-value are considered False.

## Integers

You can start an integer with 0b for binary, 0o for octal, and 0x for hexadecimal.

You can use underscores to improve readability.  For example 1_000_000  is the same than 1000000

### Operators

| Operator | Description       | Example | Result |
| :------- | :---------------- | :------ | :----- |
| +        | Addition          | 2 + 3   | 5      |
| -        | Substraction      | 20 - 5  | 15     |
| *| Multiplication    | 9* 4    | 36     |
| /        | Floating Division | 10 / 4  | 2.5    |
| //       | Integer Division  | 9 // 4  | 2      |
| %        | Modulus           | 9 % 4   | 1      |
| **| Exponentiation    | 2** 3   | 8      |

## Type Conversions

To convert data type to an integer use int().  For example:

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

| Operator | Description           |
| -------- | --------------------- |
| ==       | equality              |
| !=       | inequality            |
| <        | less than             |
| <=       | less than or equal    |
| >        | greater than          |
| >=       | greater than or equal |

## Logical operators

- and
- or
- not

If you have multiple and operation using one variable, Python let you do this:

```python
2 < y < 8 # The same as 2 < y and y < 8
```

## False values

The following are considered false

- None
- 0
- 0.0
- ''
- []
- {}
- set()

## multiple comparisons with in

You can do multiple comparisons using in.  For example:

```python
number in [1, 2, 3 ,4 ,5]
```

## Walrus operator

 The walrus operator let you combine assignment and conditional test.  For example:

```python
if number := x - y > 0:
    print('Positive')
else:
    print('Negative')
```

## Example using if - elif - else

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

- 'This is a sample string'
- "This is a sample string"

Also you can use triple quotes strings using either ''' or """.  This is use for multi-liner strings.  For example:

```python
s = '''This is a
    string containing
    multiple
    lines'''
```

## f-strings

You can format string using f or F  For example:

```python
a = 5
b = 10
c = a + b
s = f'The sum of {a} + {b} is {c}' # 'The sum of 5 + 10 is 15'
```

You can add padding to the left, center or right, using a specific character.  For example:

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

- [:] The whole string
- [start:]  from start to the end
- [: end] from the beginning to one before end
- [start : end] from start to one before end
- [start: end: step] from start to one before end, skipping character by step.

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

split() takes a string a return a list of smaller string based on the separator.  For example:

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

You can remove whitesapces or other character from the beginning or the end of a string using strip().  If you do not specify any parameters, whitespaces ill be remove.  You can specify other characters.  lstrip() remove only from the left, and rstrip() just from the right.  For example:

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

Use find(substring) or index(substring) to find the position of the first occurrence of the substring.  If you need to start from the end use rfind() or rindex().  For example:

```python
>>> s = 'Hello world, Python programmers!!!'
s.find('Python') # 13
s.index('Python') # 13
```

If the substring is not found, find will return -1, but index will return an exception.

### Case functions

- capitalize() capitalize the first letter of the string.
- title() capitalize the first letter of each word.
- upper() covert all characters to uppercase.
- lower() convert all characters to lowercase.
- swapcase()  swap uppercase and lowercase.

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

text = '   Text with spaces at the beginning and the end    '
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
    print('There are no words starting with m')
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

You can cancel a loop with break or skip until the next iteration with continue.  Below is an example of a  infinite while loop that stops when the use enters 'q'.

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

del deletes the specified element.  For example:

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

count() counts the number of occurrences of a value.  For example:

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

### len()

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

copy() make a shallow copy, which means that if the list have mutable items, if you change them in the original  variable, it will change the copies.  For example:

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

You can iterate multiple sequences using zip().  For example:

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

You can create list using list comprehensions.  The syntax is: [expression for item in iterable if condition].  For example:

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

#Create a new list sorted alphabetically
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

You can get the length of a dictionary using len().  For example: len(my_dict)

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

Iterating over a dictionary using in returns the keys.  For example:

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

Dictionaries also have comprehensions similar to list. The syntax is {key_expression, value_expression for expression in iterable if condition }  For example:

```python
names = ['john','Katy','Chris','Nancy']
my_dict = { names.index(name) + 1  : name  for name in names } # {1: 'john', 2: 'Katy', 3: 'Chris', 4: 'Nancy'}
```

## Example using dictionaries

```python
 Create an English-French dictionary

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(f"Walrus in French is {e2f['walrus']}")

#  Create a French to English dictionary

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
```

# Sets

The items in a set must be unique.  Sets are unordered.  You can create set using set().  For example:

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
# This function takes zero parameters and return zero values
def f1():
    pass

# This function takes one parameter but it does not return any values
def f2(message):
    print(message)

# This function takes one parameter and returns one value
def f3(number):
    return number * 2
```

## Arguments

### Positional Arguments

Positional arguments is when the values are copied to their corresponding parameters in order.  For example:

```python
def name(first_name, middle_name, last_name):
    print(f"First Name: {first_name}.  Middle Name: {middle_name}.  Last Name: {last_name}")

name("Jose","Maria","Feliciano") # First Name: Jose.  Middle Name: Maria.  Last Name: Feliciano
```

### Keyword Arguments

You can also specify arguments bythe names of their corresponding parameters, even in a different order.  For example:

```python
def name(first_name, middle_name, last_name):
    print(f"First Name: {first_name}.  Middle Name: {middle_name}.  Last Name: {last_name}")

name(last_name="Feliciano", first_name="Jose", middle_name="Maria") # First Name: Jose.  Middle Name: Maria.  Last Name: Feliciano
name("Jose", last_name="Feliciano", middle_name="Maria") # First Name: Jose.  Middle Name: Maria.  Last Name: Feliciano
```

The last line in the previous example mixed positional and keyword arguments.  Just make sure that the positional arguments come first.

### Default Values

You can specify default values for parameters.  The default value is use if the function is called without providing a corresponding argument.  For example.

```python
def name(first_name, middle_name, last_name="Unknown"):
    print(f"First Name: {first_name}.  Middle Name: {middle_name}.  Last Name: {last_name}")
name("Jose","Maria") # First Name: Jose.  Middle Name: Maria.  Last Name: Unknown
```

The argument with default values must be and the end of the argument list.

### Variable number of Arguments

You can define a function to take a variable number of arguments as shown in the example below.

```python
def var_args(*args):
    for item in args:
        print(item)

var_args()
var_args(1,2,3)
# 1
# 2
# 3
```

You can combine required argument with variable ones, but the variable must be the last ones.  For example:

```python
def var_args(a,b,*args):
    print(a)
    print(b)
    for item in args:
        print(item)

var_args('a','b',1,2,3)
# a
# b
# 1
# 2
# 3
```

Also you can pass a variable number of keyword arguments as shown below.

```python
def var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
var_kwargs(one='uno', two='dos')
# one uno
# two dos
```

## Docstring

You can attach documentation to a function definition by including a string at the beginning of the body.  For example:'

```python
def add(a,b):
    'return the addition of two numbers'
    return a + b
```

You can print the documentation of the function as shown below.

```python
help(add)
Help on function add in module __main__:

add(a, b)
    return the addition of two numbers

print(add.__doc__)
return the addition of two numbers
```

## Function are Objects

Functions are objects like any other type in Python, so the function name without the parenthesis, returns the object.  You can pass a function as a parameter to another function.  For example:

```python
def add(a,b):
    'return the addition of two numbers'
    return a + b

def run_function(func, x, y):
    print(func(x,y))

run_function(add,4,3) # 7
```

## Inner Functions

You can define a function inside another function as shown below:

```python
def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

outer(2,5) # 7
```

## Closures

A closure is a inner function that remember the values of the variables that were created outside the function.  For example:

```python
def outer(a,b):
    def inner():
        return a + b
    return inner()

outer(2,5) # 7
```

## Lambda Functions

Lambda function is an anonymous function expressed as a single statement.  For example:

```python
x =  lambda a: a * 2
x(2) # 4
```

The inner function above, can we rewritten using lambdas as follow.

```python
def outer(a,b):
    return (lambda a,b: a  + b)(a,b)

outer(5,4) # 9
```

Lambda  a normally used to define callback functions.

## Generators

A generator can create huge sequences without storing the entire sequence in memory.  Generators  are often the source of iterators.

### Generator Functions

Generator functions are similar to regular function, but they return a value using yield instead of return.  Below is a version of range.

```python
>>> def my_range(first=0, last=10, step=1):
...     number = first
...     while number < last:
...             yield number
...             number += step
...
range = my_range()
for item in range:
    print(item)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

### Generator Comprehensions

You can use generator comprehension in a similar way that you use comprehensions for list and dictionaries.   For example:

```python
g = (item for item in range(1,10))
for i in g:
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

## Decorators

Decorators let you change an existing function without changing the source code.  For example:

```python
def triple(func):
    def f(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * result * result
    return f

@triple
def add(a,b):
    return a + b

add(2,3) # 125
```

## Namespaces and Scope

Variables defines outside any functions are global variables and variable define inside a function are local variables.  If you assign a value tpo a variable with the same name as a global variable, it will create a different local variable.  If you need to change the value of the global variable use global variable_name = value.   For example:

```python
number = 10
def f():
    number = 5
    print(number)

f() #5
number # 10

def f():
    print(number)
    number = 5
    print(number)

f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f

def f():
    global number
    number = 5
    print(number)
...
f() # 5
number # 5
```

As you can see in the examples above, if you get the value of a global variable and then try to change it, you will get an error.

Python has 2 function to access the content of your workspaces:

* locals() returns a dictionary of the contents of the local namespace.
* globals() returns a dictionary  of the contents of the global namespace.

## __ in Names

Names that start and end with two underscores are reserved for Python.  __name__ contains the name of the function and __doc__ contains its documentation string.

```python
def add(a,b):
    'adds two numbers'
    return a + b

add.__name__ # 'add'
add.__doc__ # 'adds two numbers'
```

# Exceptions

You can handle exception with the try - except block as show in the example below:

```python
my_list = [1,2,3,4,5]

def print_item(number):
    try:
            print(my_list[number])
    except IndexError as err:
            print(f'Bad Index. {err}')
    except Exception as other:
            print(f'Error: {other}')

print_item(3) # 4
print_item(7) # Bad Index. list index out of range
```
