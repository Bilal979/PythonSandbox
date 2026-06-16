num = [1,2,3,4,5,6,7,8,9]

sqr_num1 = []

for i in num:
    sqr_num1.append(i**2)

print(sqr_num1)

print('---------With List Comprehension-----------')

sqr_num2 = [j**2 for j in num]
print(sqr_num2)


print('x'*40)
print('----------Finding evens with list comp----------------')

evens = [x for x in range(10) if x%2 == 0]

print(evens)



print('x'*40)
print('----------Nested For list comp----------------')

my_list = [x*y for x in [1,2,3] for y in [4,5,6] if x*y != 10 if x*y != 12]

print(my_list)


print('------------Use of else in list comprehension-------------------')

list_ = [['a','b', 'c'],['d', 'e', 'f'],['g','h','i']]

list_sc = [lis if not 'g' in lis else 'The letter g was detected' for lis in list_ ]

print(list_sc)