message='Hello world'
print(message)

#String methods
print(message.lower())
print(message.upper())
print(len(message))
print(message.count('l'))
print(message.find('llo'))
print(message.find('mouse'))
message=message.replace('Hello', 'Goodbye')
print(message)
print(message[0:5])
print(message[:5])
print(message[6:])
new_message="Lida's file"
new_message="""this
shall not pass"""


#Formatted Strings

greeting='Hello'
name='Lida'
message='{}, {}. Welcome!!!'.format(greeting,name)
message=f'{greeting}, {name}. Welcome!!!'
print(message)

print(dir(message))
print(help(str))
print(help(str.find))
