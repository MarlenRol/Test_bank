from src.main.api.modules.base_module import BaseModel 

class CreateUserResponse(BaseModel):
    id:int
    username:str
    password:str
    role:str