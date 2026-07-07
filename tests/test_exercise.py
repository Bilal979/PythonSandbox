import pytest


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount

def test_success_withdraw():
    #Arrange
    balance = 100
    amount = 50
    expected = 50

    #Act
    result = withdraw(balance, amount)

    #Assert
    assert result == expected

def test_withdraw_entire_balance():
    #Arrange
    balance = 100
    amount = 100
    expected = 0

    #Act
    result = withdraw(balance, amount)

    #Assert
    assert result == expected

def test_insufficient_balance():
    #Arrange
    balance = 100
    amount = 200

    with pytest.raises(ValueError):
        withdraw(balance, amount)



# The use of Fixtures

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

@pytest.fixture
def account():
    return BankAccount('Alex', 100)


def test_deposit(account):
    #Arrange
    amount = 50
    expected = 150

    #Act
    account.deposit(amount)

    #Assert
    assert account.balance == expected

def test_withdraw(account):
    #Arrang
    amount = 50
    expected = 50

    #Act
    account.withdraw(amount)

    #Assert
    assert account.balance == expected


def test_overdraw(account):
    #Arrange
    amount = 200

    with pytest.raises(ValueError):
        account.withdraw(amount)

# Parametrized tests

def is_even(number):
    return number % 2 == 0


@pytest.mark.parametrize("number, expected", [
    (2,True), 
    (3, False), 
    (0, True), 
    (-4, True), 
    (-5, False)
    ])

def test_is_even(number, expected):
    assert is_even(number) == expected 


