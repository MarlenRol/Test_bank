from src.main.api.modules.base_module import BaseModel 

class User(BaseModel):
    username:str
    role:str

class LoginUserResponse(BaseModel):
    token : str
    user: User