import requests
from src.main.api.modules.request_credit_request import RequestCreditRequest
from src.main.api.modules.request_credit_response import RequestCreditResponse
from src.main.api.requests.requester import Requester


# class RequestCreditRequester(Requester):   
#     def post(self, request_credit_requester:RequestCreditRequest)->RequestCreditResponse:
#         url = f"{self.base_url}/credit/request"
#         response = requests.post(
#             url=url,
#             json=request_credit_requester.model_dump(),
#             headers=self.headers
#         )
#         self.response_spec(response)
#         return RequestCreditResponse(**response.json())