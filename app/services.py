from .database import accounts


def get_account(acc_no: str):
    if acc_no not in accounts:
        raise ValueError("Account not found")
    return accounts[acc_no]


def balance_enquiry(acc_no: str):
    acct = get_account(acc_no)
    return {
        "account": acc_no,
        "balance": acct.balance,
        "earmarked": acct.earmarked_amount,
        "available_balance": acct.available_balance()
    }


def post_transaction(acc_no: str, amount: float):
    acct = get_account(acc_no)

    if amount < 0 and abs(amount) > acct.available_balance():
        raise ValueError("Insufficient balance")

    acct.balance += amount
    return {"message": "Transaction successful", "new_balance": acct.balance}


def earmark_funds(acc_no: str, amount: float):
    acct = get_account(acc_no)

    if amount > acct.available_balance():
        raise ValueError("Insufficient available balance to earmark")

    acct.earmarked_amount += amount
    return {"message": "Funds earmarked", "earmarked": acct.earmarked_amount}


def release_earmark(acc_no: str, amount: float):
    acct = get_account(acc_no)

    if amount > acct.earmarked_amount:
        raise ValueError("Cannot release more than earmarked amount")

    acct.earmarked_amount -= amount
    return {"message": "Earmark released", "earmarked": acct.earmarked_amount}
