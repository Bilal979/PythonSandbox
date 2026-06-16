# Using star args

def greetings(*args):
    print(f'Hello amigo {args[0]}')
    print(f'Hi amigo {args[1]}')
    print(f'Ola amigo {args[2]}')



greetings('Aslan', 'Mac queen', 'Jack', 'Frost')

# The *args are in tuple form
def get_sum(*args):
    print(f'args are {args}')
    result = 0
    for x in args:
        result += x

    return print(result)

get_sum(1,2,3,4)

print('='*20)

# using **kwargs (for named arguments)
# **kwargs are in dictionary form
def myfunc(**kwargs):
    print(f'kwargs are {kwargs}')

    for i,j in kwargs.items():
        print(f'key is {i}, value is {j}')


# myfunc(name='John', email='carter@gmail.com', password='12345678')

# OR

named_arguments = {'name':'John', 'email':'carter@gmail.com', 'password':'12345678'}
myfunc(**named_arguments)


