from typing import List, Optional
from src.main.api.modules.base_module import BaseModel


class Transactions(BaseModel):
    transactionId: int
    type: str
    amount: float
    fromAccountId: Optional[int] = None
    toAccountId: Optional[int] = None
    createdAt: str
    creditId: Optional[int] = None

class GetAccountTransactionsResponse(BaseModel):
    id:int
    number:str
    balance:float
    transactions:List[Transactions]