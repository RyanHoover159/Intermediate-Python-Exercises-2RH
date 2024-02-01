from BankAccount import BankAccount

account = BankAccount("Wally", 70.20)
account.deposit(500)
account.withdraw(200)

print(account.get_balance())
