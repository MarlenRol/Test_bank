from src.main.api.modules.repay_credit_request import RepayCreditRequest
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.modules.request_credit_request import RequestCreditRequest
from src.main.api.steps.base_steps import BaseSteps


class CreditSteps(BaseSteps):
    def credit_request(self, create_user_request:CreateUserRequest,request_credit_request:RequestCreditRequest ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_creared()
        ).post(request_credit_request)
        return response
    
    def credit_repay(self,create_user_request:CreateUserRequest, repay_credit_request:RepayCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(repay_credit_request)
        return response