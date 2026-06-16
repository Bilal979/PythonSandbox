

a = [1,2,3,4,5]
b = list((1,2,3,'v','c','x'))

print(a[0:4:1])
print(b[::2])
print(b[::-1])

# add to lists
# c = a+b
# print(c)
# OR
a.extend(b)
print(a)

# Add an element in the list
a.append('x')
print(a)

# Remove an element from list

a.pop()
a.pop(-1)
print(a)

# OR

a.remove('c')
print(a)

# count the number of char in list

count = a.count(3)
print(count)

# sort the list elements

d = ['1','3','4','2']
e = ['a','d','c','b']

# d.sort(reverse=True)
d.sort()
print(d)



# To reverse the elements in a list
e.reverse()
print(e)

# common operations

print(min(d))
print(max(e))
# print(sum(d))



# Unpack the list
w,s,x,c = d

print(w)
print(s)
print(x)
print(c)