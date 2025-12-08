from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.modules.base_module import BaseModel


class DepositAccountRequest(BaseModel):
    accountId:int
    amount:Annotated[float, CreationRule(regex=r'^((1000|[1-4][0-9]{3}|9000)(\.\d{2})?)$')]