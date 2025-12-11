from typing import List, Optional
from src.main.api.modules.base_module import BaseModel

class Credits(BaseModel):
    creditId: int
    accountId: int
    amount: float
    termMonths: int
    balance: float
    createdAt: str

class GetHistoryCreditResponse(BaseModel):
    userId:int
    credits:Optional[List[Credits]] = []
   