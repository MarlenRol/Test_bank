from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.modules.base_module import BaseModel


class TransferAccountRequest(BaseModel):
    fromAccountId:Annotated[int,CreationRule(regex=r'^1')] 
    toAccountId:Annotated[int,CreationRule(regex=r'^1')] 
    amount:Annotated[float, CreationRule(regex=r'^((500|[1-4][0-9]{3}|10000)(\.\d{2})?)$')]