file = open('file.txt','r')

for sen in file:
    if 'python' in sen.lower():
        print(sen)

file.close()

print('x'*20)

# using with open
with open('file.txt','r') as file:
    for line in file:
        print(line)



print('x'*20)

# using read line function

with open('file.txt','r') as file:
    # readline fun reads the next line from file
    line = file.readline()
    # line2 = file.readline()
    # print(line)
    # print('-'*12)
    # print(line2)
    while line:
        print(line, end='')
        line = file.readline()


print('-'*20)

# using readLines function
with open('file.txt', 'r') as file:
    lines_list = file.readlines()

for line in lines_list[::-1]:
    print(line, end='')


print('-'*20)
# using read function

file = open('file.txt','r')

chars = file.read()

for char in chars[::-1]:
    print(char, end='')

file.close()

# Write a file

data_list = ['I','am', 'speed']

with open('temp_file.txt', 'w') as temp_file:
    for data in data_list:
        print(data, file=temp_file)


# Append data in file

with open('temp_file.txt', 'a') as file:
    for i in range(1,10):
        for j in range(1,10):
            print(f'{i} times {j} is {i*j}', file=file)

        print('x'*10, file=file)



