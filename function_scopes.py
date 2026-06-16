import os


clothes = 'Dirty Clothes'

def washing_machine(clean_clothes):
    global clothes
    clothes = clean_clothes
    print(clothes)

print(clothes)

washing_machine('Clean Clothes')


print(f'the final one ------ {clothes}')



print('='*30)

# Using global,enclosing local scopes


def washing_machine1():
    # Enclosing Scope
    clothes1 = 'Dry and wet'
    def dry_clean():
        nonlocal clothes1
        clothes1 = 'Dry and clean'
        # print(clothes1)

    dry_clean()
    print(clothes1)

washing_machine1()

print('='*20)

# calculate factorial
def fact_calc(x):
    result = 1
    for n in range(2,x+1):
        result = n * result
    return result

number = int(input('Pleas enter the number to calculate factorial: '))

print(f'The factorial is {fact_calc(number)}')


print('============ Factorial Using Recursion ===================')

def recursive_fun(n):
    if n <= 1:
        return 1
    else:
        a = n * recursive_fun(n-1)
        return a

number = int(input('Pleas enter the number to calculate factorial(Using Recursion): '))


print(f'The factorial is {recursive_fun(number)}')



print('============ Fibonacci Using Recursion ===================')

def fab(n):
    if n<2:
        return n
    else:
        x = fab(n-1) + fab(n-2)
        return x

for i in range(10):
    print(f'fibonacci of {i} is {fab(i)}')


print('============= List the OS directories|files using OS import ===================')

# list_ = os.walk('D:\\PycharmProjects\\PythonProject')
search_key = input('Please enter the file name:-')
# for root,direct,files in list_:
#     # print(f'The root name is {root}')
#     # print(f'The direct name is {direct}')
#     # print(f'The files names are {files}')
#     for f in files:
#         if search_key in f:
#             print(f'found the file--- {f}')
#     # if 'search_key' in files:
#     #     print(f'Found the files list {files}')


print('======================= List Directories using recursive function =============================')


def list_direct_outer(s):

    def list_direct(d):
        my_files = os.listdir(d)

        for my_file in my_files:
            current_dir = os.path.join(d,my_file)

            if os.path.isdir(current_dir):
                print(f'Directory---- {current_dir}')
                list_direct(current_dir)
            else:
                # print(f'File-----{current_dir}')
                if search_key in current_dir:
                    print(f'Found the file---- {current_dir}')


    if os.path.exists(s):
        print('----Found the directory. Listing...')
        list_direct(s)

    else:
        print('Directory not found.')



list_direct_outer('D:\\PycharmProjects\\PythonProject')





print('================ Print Table Using recursive function ==================')

def recursive_table(n,v):

    result = n*v
    print(f'{n} x {v} is {result}')
    v += 1
    if v < 11:
        recursive_table(n,v)


recursive_table(2,1)