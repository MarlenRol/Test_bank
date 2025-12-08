from src.main.api.modules.base_module import BaseModel 

class CreateAccountResponse(BaseModel):
    id: int
    number: str
    balance: float