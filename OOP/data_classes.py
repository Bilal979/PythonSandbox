from dataclasses import dataclass
from dataclasses import field, asdict

@dataclass
class User:
    username: str
    email: str


user = User('ALi', 'ali@gmail.com')

print(user)


print('------------------defaults------------------')

@dataclass
class ShoppingCart:
    owner: str
    items: list = field(default_factory=list)

    def add_item(self, item):
        self.items.append(item)


c1 = ShoppingCart('Ali')
c2 = ShoppingCart('Sara')

c1.add_item('Book')

print(c1.items)
print(c2.items)


print('----------------__post_init__---------------')

@dataclass
class Product:
    name: str
    price: float
    stock: int = 0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError('Price can not be negative')
        if self.stock < 0:
            raise ValueError('Stock can not be less than 0')

p = Product("Notebook", 10)

print(p)


print('------------------converting objects ↔ dictionaries--------------------')

@dataclass
class OrderResponse:
    order_id: int
    total: float
    items: list = field(default_factory=list)


order_response = OrderResponse(1, 10, ['x','y', 'z'])

response_dict = asdict(order_response)
print(response_dict)

new_order_response = OrderResponse(**response_dict)
print(new_order_response)

