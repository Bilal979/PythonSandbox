dict_a = {'key1':'val1', 'key2':'val2','key3':'val3'}

print(dict_a['key1'])

print(dict_a.get('key4'))

print(dict_a)
a,b,c= dict_a.keys()
print(a)
print(b)
print(c)

print(dict_a.values())

print(dict_a.items())

new_dict = dict([('key4', 'val4'), ('key5', 'val5'), ('key6', 'val6')])

# new_dict.pop('key4')
#
# new_dict.popitem()

del new_dict['key5']

print('new dict is ')
print(new_dict)