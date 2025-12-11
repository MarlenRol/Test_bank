import json
from typing import Optional
from requests import Response
import requests
from src.main.api.configs.config import Config
from src.main.api.modules.base_module import BaseModel
from src.main.api.foundation.http_requester import HttpRequester
import allure

class CrudRequester(HttpRequester):
    def post(self, model: Optional[BaseModel]) -> Response:
        body = model.model_dump() if model is not None else ""
        with allure.step(f"POST{Config.fetch("backendUrl")}{self.endpoint.value.url}"):
            allure.attach(str(body), "Request body", allure.attachment_type.JSON)

        response = requests.post(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}",
            headers =self.request_spec,
            json = body
        )
        allure.attach(
            response.text,
            "Response body",
            allure.attachment_type.JSON
        )
        self.responce_spec(response)
        return response
    
    def get(self, id:Optional[int])->Response:        
        url_id:str = f"/{id}" if id is not None else ""
        response = requests.get(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}{url_id}",
            headers=self.request_spec
        )
        self.responce_spec(response)
       
        return json.loads(response.text)
  
    def delete(self, user_id:int)-> BaseModel | Response:
        response = requests.delete(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}/{user_id}",
            headers=self.request_spec
        )
        self.responce_spec(response)
        return response