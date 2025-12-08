from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.login_user_request import LoginUserRequest
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.steps.base_steps import BaseSteps


class DepositSteps(BaseSteps):

    def create_account(self, create_user_request:CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_creared()
        ).post()
        return response

    def deposit_account(self, create_user_request:CreateUserRequest,deposit_account_request:DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response