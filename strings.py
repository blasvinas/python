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
