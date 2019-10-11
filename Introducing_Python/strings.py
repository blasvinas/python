#Initialing string
s1 = 'Hello'
s2 = "World!"
s3 = ''' This is an
examples of a
multiline string'''
s4 = """This is
another
example"""
print(s1)
print(s2)
print(s3)
print(s4)

#Converting other type to string
s1 = str(13.5)
s2 = str(20)
print(s1, s2)

#Concatenate string
s1 = 'Hello'
s2 = 'World'
s3 = s1 + " " + s2
s4 = "Hola " "Mundo"
print(s3)
print(s4)


#Duplicate
s1 = "Hello" * 5
print(s1)

#Get individual characters
s1 = "aeiou"
print(s1[0],s1[1],s1[2],s1[3],s1[4])

#Slices
s1 = "I like programming in Python"
s2 = s1[:]
s3 = s1[:18]
s4 = s1[22:]
s5 = s1[-6:]
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

#Length 
s1 = "Hello World!"
l = len(s1)
print(l)

#split and  join
s1 = "uno, dos, tres, cuatro, cinco"
numbers = s1.split(',')
s2= ','.join(numbers)
print(numbers)
print(s2)

#Replace
s3 = s1.replace("dos","two")
print(s3)

#Strip
s1 = "     Hello World      "
s2 = ".....Hola Mundo......."
s3 = s1.strip()
s4 = s2.strip('.')
s5 = s2.lstrip('.')
s6 = s2.rstrip('.')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

#Search
s1 = "i like programming in Python"
print(s1)
print("Does s1 staet with 'i like'?", s1.startswith("i like"))
print("Index of like:", s1.index("like"))
print("Index of Python: ", s1.rindex("Python"))
#print("Index of Python: ", s1.index("go")) #Cause a ValueError exception
#The same with find
print("Index of like:", s1.find("like"))
print("Index of Python: ", s1.rfind("Python"))
print("Index of Python: ", s1.find("go"))  #Return -1

#Case
s2 = s1.capitalize()
s3 = s1.title()
s4 = s1.upper()
s5 = s4.lower()
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

#f-string
s1 = "Hello"
d1 = 50
f1 = 14.5

s2 = f'String: {s1}.  Integer: {d1}.  Float: {f1}'
print(s2)