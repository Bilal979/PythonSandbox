# x = int(input('enter a value'))
#
# if x>2:
#     print('the condition is true')
# else:
#     print('the condition is false')
#
#
# number = float(input('Enter your amount:'))
#
# if number<1000:
#     discount = number*.05
#     print(f'your discount is {discount}')
# elif number<5000:
#     discount = number*.1
#     print(f'your discount is {discount}')
# else:
#     discount = number*.15
#     print(f'your discount is {discount}')
#

# sentence = 'a quick brown fox jumps over the lazy dog'
#
# word = input('Enter your word:')
#
# if word in sentence:
#     print(f'{word} exists in the sentence')
# else:
#     print(f'{word} does not exists in the sentence')
#


# get clean number

# number = '192.131.12.10'
# clean_number = ''
# for i in range(len(number)):
#     if number[i] in '0123456789':
#         clean_number += number[i]
#
#
# print(clean_number)


# FOr and if togather

# grocery_list = ['rice','pasta','milk','cheese', 'bread']
#
# for x in grocery_list:
#     if x == 'cheese':
#         print('Won\'t by '+x)
#         continue
#     print('Will buy '+x)


# check prime number

# x = int(input('Please enter a number:'))
#
# if x > 1:
#     for i in range(2,x//2+1):
#         if x%i == 0:
#             print(f'{x} is not prime')
#             print(f'{i} times by {x/i} is {x}')
#             break
#     else:
#         print(f'{x} is a prime')
# else:
#     print(f'{x} is not prime')


# word counter

sentence = 'A quick brown fox jumps over the lazy dog'

count = 1

for char in sentence:
    if char == ' ':
        count += 1

print(f'total words are {count}')


