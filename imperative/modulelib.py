import random
import datetime
import timeit

x = random.randint(0,10)
print(x)

date = datetime.datetime.now()

print(date)

dob = datetime.date(1998, 6,16)

today = datetime.date.today()

age = today - dob

print(age)


print('-'.join(str(n) for n in range(100)))

print(timeit.timeit(stmt="'-'.join(str(n) for n in range(100))", number=10000))