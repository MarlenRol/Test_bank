from typing import Dict, Callable

from src.main.api.foundation.endpoint import Endpoint



class HttpRequester:
    def __init__(self, request_spec: Dict[str,str], endpoint:Endpoint, responce_spec:Callable):
        self.request_spec = request_spec
        self.endpoint = endpoint
        self.responce_spec = responce_spec