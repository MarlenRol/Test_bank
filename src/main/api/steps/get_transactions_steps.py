from src.main.api.modules.get_account_transactions_response import GetAccountTransactionsResponse
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.steps.base_steps import BaseSteps


class GetTransactionsSteps(BaseSteps):
        def get_transactions(self,id_account:int ,create_user_request:CreateUserRequest):
            response = CrudRequester(
                RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
                Endpoint.TRANSACTIONS_GET_ACCOUNT,
                ResponseSpecs.request_ok()
            ).get(id_account)
            return GetAccountTransactionsResponse(**response)