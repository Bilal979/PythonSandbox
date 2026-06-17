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

#------------Initialization function-------------

print('x'*20)
class map1():
    def __init__(self, attribute):
        self.attribute = attribute
        print(f"I built {attribute}")

    def adder(self):
        a = 2
        b = 2
        x = a + b
        return x


house1 = map1('new house')
house1.attribute2 = 'the new attribute'
print(house1.attribute)
print(house1.attribute2)
print(house1.adder())

print('x'*20)

#------------------Class exercise---------------

class kattle():

    #universal/class space (define universal attributes here)
    power_src = 'electrcity'

    def __init__(self, name,price):
        self.name = name
        self.price = price
        self.power = False

    def switch(self):
        self.power = True


hamilton_kattle = kattle('hamilton', 10)
kenwood_kattle = kattle('kenwood', 20)

print(hamilton_kattle.name)
print(hamilton_kattle.power_src)
print(hamilton_kattle.power)
hamilton_kattle.switch()
print(hamilton_kattle.power)



print('x'*20)

#----------------Class namespace
print(kattle.__dict__)
print(hamilton_kattle.__dict__)

kattle.power_src = 'solar'
hamilton_kattle.power_src = 'AC'


print(hamilton_kattle.__dict__)
print(kattle.__dict__)







