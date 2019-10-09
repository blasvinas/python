#Changing the case
name = 'ada lovelace'
print(name)
print(name.title())
print(name.upper())
print(name.lower())

#Concatenation
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)

#Stripping Whitespace
original_string = '   This string has space on the left and right    '
print('String with spaces and the right and left: {}'.format(original_string))
#Removing spaces from the right
print('String with right spaces removed: {}'.format(original_string.rstrip()))
#Removing spaces from the left
print('String with the left spaces removed: {}'.format(original_string.lstrip()))
#Romiving spaces right and left
print('String with the left and right  spaces removed: {}'.format(original_string.strip()))