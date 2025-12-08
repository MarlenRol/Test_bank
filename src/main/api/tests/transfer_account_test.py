import pytest

from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.modules.transfer_account_request import TransferAccountRequest
from src.main.api.modules.transfer_account_response import TransferAccountResponse
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestTransferAccount:
    def test_treansfer_account(self,api_manager:ApiManager, create_user_request:CreateUserRequest):
        response_account_1:CreateAccountResponse = api_manager.deposit_steps.create_account(create_user_request)
        response_account_2:CreateAccountResponse = api_manager.deposit_steps.create_account(create_user_request)
        assert response_account_1.balance == 0 and response_account_2.balance == 0

        deposit_account_request = DepositAccountRequest(accountId=response_account_1.id, amount=1500)
        response_deposit:DepositAccountResponse = api_manager.deposit_steps.deposit_account(create_user_request,deposit_account_request)
        assert response_account_1.id == response_deposit.id and response_deposit.balance == 1500

        request_transfer = TransferAccountRequest(fromAccountId=response_account_1.id, toAccountId=response_account_2.id, amount=500)
        response_transfer:TransferAccountResponse = api_manager.transfer_steps.transfer_account(create_user_request,request_transfer)
        assert  response_transfer.fromAccountIdBalance == 1000