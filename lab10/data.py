class Bank:
    
    def __init__(self):
        self.Accounts = []
        self.Customers = []

    def add_customer(self, name, personal_nbr):
        self.Customers.append(Customer(len(self.Customers)+1, personal_nbr, name))

    def get_customer(self, customer_id):
        for customer in self.Customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def find_customer_by_part_of_name(self, name_part):
        found = []
        for customer in self.Customers:
            if name_part in customer.name:
                found.append(customer)
        return found

    def create_account(self, customer_id):
        pass

    def get_account(self, account_nbr):
        pass

    def remove_account(self, account_nbr):
        pass

    def transfer(self, from_acc_nbr, to_acc_nbr, amount):
        pass

    def all_accounts(self):
        pass

    def accounts_by_customer(self, customer_id):
        pass

    def all_customers_sorted_by_name(self):
        pass

class Customer:

    def __init__(self, customer_id, personal_nbr, name):
        self.customer_id = customer_id
        self.personal_nbr = personal_nbr
        self.name = name

    def __str__(self):
        string = str(self.customer_id) + ' ' + str(self.personal_nbr) + ' ' + str(self.name)
        return string

class Account:

    def __init__(self, customer_id, account_nbr):
        self.customer_id = customer_id
        self.account_nbr = account_nbr
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return False
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount

    def __str__(self):
        return 'kontonummer: ' + str(self.customer_id) + ', saldo: ' + str(self.balance) + ' ' + str(self.account_nbr)
    