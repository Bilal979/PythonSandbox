#Creating tuple

tuple_a = 1,2,3,4
# or
tuple_b = ('a','b','c','d')

print(tuple_b)
print(tuple_b)

# Tuple are immutable, cannot manipulate but can reassign

tuple_c = tuple_a[0],tuple_b[0],'c', 'd'

print(tuple_c)

# unpack tuple

a,b,c,d = tuple_a

print(a)
print(b)
print(c)
print(d)
