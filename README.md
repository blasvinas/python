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

## Walrun operator
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
In python you can use single or double quotes for your string.  For example:

* 'This is a sample string'
* "This is a sample string"