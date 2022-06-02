class Account:
    def __init__(self, name: str, password: str,phone_number: str):
        self.password = password
        self.balance = 0
        self.name = name
        self.phone_number = phone_number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount: int, password: str):
        if password is not self.password:
            raise ValueError("your password can be wrong")
        if password is self.password:
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            if amount > self.balance:
                raise ValueError("insufficient balance")
            self.balance -= amount

    def load_airtime(self, amount, phone_number):
        if phone_number is phone_number:
            if amount > 0:
                self.balance -= amount

    # def transfer(self, amount,password):
    #     if amount
    def transfer(self, amount, receiver_account, password):
        self.withdraw(amount,password)
        receiver_account.deposit(amount)

