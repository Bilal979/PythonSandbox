class map():
    attribute = 'house'
    print(f'I built {attribute}')
    def adder(self):        # <- is a method
        a = 2
        b = 2
        x = a+b
        return  x




house = map()
print(house.attribute)

# ---------Dynamic nature of attribute in python classes

house.attribute = 'new house'
house.attribute1 = 'new house 1'

print(house.attribute)
print(house.attribute1)

print(house.adder())



