class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'

def validate():
    while True:
        password = input("Enter a password: ")
        if password == '1234':
            break
        else:
            print("Wrong password")
validate()
class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.amount = amount
        self._balance += amount
        print('Amount : ',amount)

    def charge(self):
        amount = float(input("Enter the amount of1 withdraw: "))
        if self._balance >= amount:
            self._balance -= amount
            print("You withdraw: ", amount)
        else:
            print("Not enough balance ")
    def display(self):
        print("Net Available Balance=", self._balance)

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'

bank = Bank()

c = bank.create_customer('John', 'Brown')
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)

c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)

# creating an object of class
s = Account('John')

# calling functions with that class
s.deposit()
s.charge()
s.display()