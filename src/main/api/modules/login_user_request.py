from src.main.api.modules.base_module import BaseModel 

class LoginUserRequest(BaseModel):
    username: str
    password: str 
    