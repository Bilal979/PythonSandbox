data = '12345678'
print(data)
print(data[0:3])
print(data[3::])  # :: operator to show characters till the end of list
print(data[::-1])
print(data[0:7:2])
print(data[::2])
print(data[1::2])

string = 'Hello World'
print(string.lower())
print(string.upper())
print(string.title())

print(string.split())

print(' '.join(string))

print(string.replace('World', 'Python'))

print(string.count('l'))

print(string.find('l'))

print((string+' ')*4)

print(string.strip())

print(string.replace('Hello', 'Olla'))

name = "caesar"
age = 20
# print(name.startswith('Se'))
# print(name.endswith('s'))

string1 = f'Hello {name.title()} your age is {age+6}'
print(string1)

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

print(f'Hello {name.capitalize()} you\'r \n {age/2} years old')

print("""Hello there, this is a long... 

paragraph.""")
