from src.main.api.modules.base_module import BaseModel


class DepositAccountResponse(BaseModel):
    id:int
    balance:float