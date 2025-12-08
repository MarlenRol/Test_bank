from src.main.api.modules.base_module import BaseModel


class TransferAccountResponse(BaseModel):
  fromAccountId:int
  toAccountId:int
  fromAccountIdBalance:float