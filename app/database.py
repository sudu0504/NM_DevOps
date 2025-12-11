from typing import Dict


class Account:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance
        self.earmarked_amount = 0.0

    def available_balance(self):
        return self.balance - self.earmarked_amount


# Simulated in-memory database
accounts: Dict[str, Account] = {
    "10001": Account("10001", 1000.0),
    "20002": Account("20002", 500.0)
}
