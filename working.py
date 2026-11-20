from oops import *
from pathlib import Path

account_name = "Sam"
account = SavingsAccount(account_name, 100)
account.deposit(25)
account.withdraw(10)

account_name="john"
account = CheckingAccount(account_name, 200)
account.deposit(50)
account.withdraw(300)  # This will trigger the balanceexception and print an error message

account_name = "Alice"
account = SavingsAccount(account_name, 500)
account.deposit(100)
account.withdraw(50)
print(f"\nTransaction history for {account_name}:")
print(f"\n{account.account_type} balance: ${account.get_balance()}")

transactions = account.get_transactions()

for transaction_type, amount, balance in transactions:
    print(f"\n{transaction_type}: ${amount}, \tbalance: ${balance}")

log_path = Path(__file__).with_name("transactions.txt")
with log_path.open("a", encoding="utf-8") as log_file:
    log_file.write(f"{account.account_type} account for {account_name}\n")
    for transaction_type, amount, balance in transactions:
        log_file.write(
            f"{transaction_type}: ${amount}, balance: ${balance}\n"
        )
    log_file.write("\n")
