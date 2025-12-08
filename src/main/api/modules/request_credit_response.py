from src.main.api.modules.base_module import BaseModel


class RequestCreditResponse(BaseModel):
    id:int
    amount:float
    termMonths:int
    balance:float
    creditId:int