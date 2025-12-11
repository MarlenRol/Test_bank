import pytest

from src.main.api.modules.get_account_transactions_response import GetAccountTransactionsResponse
from src.main.api.fixtures.transfer_fixture import TransferFixture
from src.main.api.modules.transfer_account_response import TransferAccountResponse
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account(self,api_manager:ApiManager, transfer_account:TransferFixture):
        response_transfer:TransferAccountResponse = api_manager.transfer_steps.transfer_account(transfer_account.user,transfer_account.transfer_account_request)
        response_get_transactions:GetAccountTransactionsResponse = api_manager.get_transactions_steps.get_transactions(response_transfer.fromAccountId, transfer_account.user)
        assert  response_transfer.fromAccountIdBalance == response_get_transactions.balance