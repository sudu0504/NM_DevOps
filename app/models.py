from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float

class EarmarkRequest(BaseModel):
    amount: float
