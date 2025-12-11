from typing import Optional, Protocol
from requests import Response
from src.main.api.modules.base_module import BaseModel


class CrudEndpoint(Protocol):
    def post(self, model:Optional[BaseModel])->BaseModel | Response:...
    def get(self, user_id: Optional[int])-> BaseModel | Response:...
    def delete(self, user_id: int) -> BaseModel | Response:...
    
