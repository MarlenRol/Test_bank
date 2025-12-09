from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.modules.base_module import BaseModel


class RequestCreditRequest(BaseModel):
    accountId:Annotated[int, CreationRule(regex=r'^1')]
    amount:Annotated[float, CreationRule(regex=r'^(5000\.00|15000\.00|[5-9][0-9]{3}\.[0-9]{2}|1[0-4][0-9]{3}\.[0-9]{2})$')]
    termMonths:Annotated[int, CreationRule(regex=r'^(0[1-9]|1[0-2])$')]

   