lista = [1,2,3,4,5,6,7]


# Iterate using iter function

var_a = iter(lista)

print(next(var_a))

str = 'asdfg'

var_b = iter(str)

print(next(var_b))


# Iterate using for loop

for x in lista:
    print(x)


# Nested for loop

for i in range(10):
    print(f'x'*10)
    print(f'This is table of {i}')
    print(f'x'*10)

    for j in range(10):
        print(f'{i} multiply by {j} is {i*j}')


# Sum the elements of a lista
sum = 0
for s in range(1,100,2):
    sum = sum + s

print(sum)


# for loop with else

for j in range(5):
    print(j)
else:
    print('the loop ended')


# Zip method

list_a = ['apple','banana','cherry']
list_b = ['orange','mango','grapes']

zip_list= zip(list_a, list_b)

print(zip_list )

for x,y in zip_list:
    print(x,y)


# Loop in dictionary

a = {'key1':'Value of key1', 'key2':'Value of key2','key3':'Value of key3'}

for key,value in a.items():
    print(key, value)

# disp values of list in reverse order

keys = list(a.keys())

print(keys)

reversed_list = sorted(keys, reverse=True)

print(reversed_list)

for key in reversed_list:
    print(a[key])

for k in a:
    print(k)


# For loop on tuple

i = [('a', 'b'), ('c', 'd'), ('e', 'f')]

for (a,b) in i:
    print(a,b)


x= tuple(list(range(10)))

print(f"tuple is {x}")

for j in x:
    print(j)

# using enumerate function

for index,item in enumerate(x):
    print(index,item)


