from fastapi import FastAPI, HTTPException
from .models import Transaction, EarmarkRequest
from .services import (
    balance_enquiry,
    post_transaction,
    earmark_funds,
    release_earmark
)

app = FastAPI(title="Banking API", version="1.0")


@app.get("/balance/{acc_no}")
def get_balance(acc_no: str):
    try:
        return balance_enquiry(acc_no)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/transaction/{acc_no}")
def transaction(acc_no: str, trx: Transaction):
    try:
        return post_transaction(acc_no, trx.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/earmark/{acc_no}")
def earmark(acc_no: str, req: EarmarkRequest):
    try:
        return earmark_funds(acc_no, req.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/release/{acc_no}")
def release(acc_no: str, req: EarmarkRequest):
    try:
        return release_earmark(acc_no, req.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def root():
    return {"message": "Banking API is running"}
