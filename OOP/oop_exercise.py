class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Current Balance: {self.balance}")


acc = BankAccount('test', 100)
acc.deposit(50)
acc.withdraw(30)

acc.display_balance()


print('----------------------Composition Exercise----------------------------')

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"{self.title} by {self.author}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        
        if len(self.books) == 0:
            print(f"There are no books in the {self.name}")
            return

        print(f"The books in {self.name} are:")
        for book in self.books:
            book.display()


lib = Library("City Library")

lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Dune", "Frank Herbert"))

lib.list_books()

print('----------------------Encapsulation Exercise----------------------------')

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, amount):
        if amount <0:
            raise ValueError("Salary should be non-negative")
        
        self._salary = amount


emp = Employee("Ali", 5000)

print(f"The salary of {emp._name} is {emp.salary}")

emp.salary = 7000

print(f"The salary of {emp._name} is {emp.salary}")
# emp.salary = -100   # should fail


print('----------------------OOP Consolidation-----------------------------')

class OrderItem:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity

    @property
    def detail(self):
        return f"product name: {self.product_name} - quantity: {self.quantity} - price: {self.price}"


    def __str__(self):
        return f'{self.product_name} X {self.quantity} = {self.total}'


class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        self.order_items.append(item)

    @property
    def total_price(self):
        price = 0
        for item in self.order_items:
            price += item.total
        return price

    def print_receipt(self):
        for item in self.order_items:
            # print(item.detail)
            print(item)


order = Order()

order.add_item(OrderItem("Book", 10, 2))
order.add_item(OrderItem("Pen", 2, 5))

print(order.total_price)
order.print_receipt()
