from src.main.api.modules.base_module import BaseModel


class RepayCreditResponse(BaseModel):
    creditId:int
    amountDeposited:float