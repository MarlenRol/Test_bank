from src.main.api.modules.base_module import BaseModel


class RepayCreditRequest(BaseModel):
    creditId:int
    accountId:int
    amount:float