# Python Notes
This file has some basic notes about how to use Python

* [Variables](#variables)
* [Numbers](#numbers)
* [Strings](#strings)
* [if](#if)

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

You can format string using f or F  For example:

```python
a = 5
b = 10
c = a + b
s = f'The sum of {a} + {b} is {c}' # 'The sum of 5 + 10 is 15'
```
Also you can start a string with r or R to create a raw string.  Raw string  prevent escape sequences.  For example"

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
