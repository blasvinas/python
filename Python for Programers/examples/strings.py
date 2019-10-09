# strings.py
''' SHows how to work with strings '''

n1 = 10
n2 = 15.35
str1 = 'hello'
str2 = 'I like programming in Python'
str3 = 'server01,linux,10.1.1.1'

print(f'{n1:10d}')
print(f'{n2:10.1f}')
print(f'{str1:>10s}')
print(str2.title())
server, os, ip = str3.split(',')
print(f'{server} {os} {ip}')
print('like' in str2)
print(str2.count('in'))
print(str3.replace(',',':'))
