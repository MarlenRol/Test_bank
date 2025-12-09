from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.modules.base_module import BaseModel


class DepositAccountRequest(BaseModel):
    accountId:Annotated[int,CreationRule(regex=r'^1')] 
    amount:Annotated[float, CreationRule(regex=r'^((?:1000|[1-8][0-9]{3})(?:\.[0-9]{2})?|9000(?:\.00)?)$')]