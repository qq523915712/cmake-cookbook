import account

account1 = account.new()

account.deposit(account1, 100.0)
account.deposit(account1, 100.0)

account2 = account.new()

account.deposit(account2, 200.0)
account.deposit(account2, 200.0)

account.withdraw(account1, 50.0)

assert account.get_balance(account1) == 150.0
account.free(account1)

assert account.get_balance(account2) == 400.0
account.free(account2)
