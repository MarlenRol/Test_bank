from typing import Annotated
from main.api.generators.creation_rule import CreationRule
from src.main.api.modules.base_module import BaseModel


class RequestCreditRequest(BaseModel):
    accountId:int
    amount:Annotated[float, CreationRule(regex=r'^((5000|[1-4][0-9]{3}|15000)(\.\d{2})?)$')]
    termMonths:Annotated[int, CreationRule(regex=r'^(?:0[1-9]|1[0-2])$')]

   