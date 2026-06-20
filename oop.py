import datetime

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


print('x'*20)

#-----------Bank Class

class Account():

    @staticmethod
    def current_time():
        time = datetime.datetime.now()
        return time;

    def __init__(self,name, balance):
        self._name = name   # programers convention (to treat name as private variable)
        self.__balance = balance    # name mangling, python will not allow name mangling
        self.trans_list = [(balance, Account.current_time())]
        print(f'Account created for {name} with balance {balance}')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self.show()
        self.trans_list.append((amount, Account.current_time()))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.trans_list.append((amount*-1, Account.current_time()))
        else:
            print(f'{self._name} you have not enough balance')
        self.show()

    def show(self):
        print(f'The balance of {self._name} is {self.__balance}')

    def show_trans(self):
        for amount, date in self.trans_list:
            type=''
            if amount > 0:
                type = 'Deposit'
            else:
                type = 'Withdraw'
            
            print(f'Amount {amount} dollars, {type} from/to {self._name} account on date {date}.')




zahir_account = Account('zahir', 10)
zahir_account.deposit(30)

zahir_account.withdraw(10)
zahir_account.show_trans()

print(zahir_account.__dict__)

print('x'*20)

# Magic/dunder methods (double leading and trailing underscores)

print(dir(zahir_account))  # <- Will print all the dunder methods (dunder methods are used internally by python)









