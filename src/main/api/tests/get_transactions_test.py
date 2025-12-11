import pytest

from src.main.api.fixtures.get_transactions_fixture import GetTransactionsDepositFixture, GetTransactionsTransferFixture
from src.main.api.modules.get_account_transactions_response import GetAccountTransactionsResponse
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestGetTransactions:
    def test_transactions_deposit(self,api_manager:ApiManager,get_transactions_deposit_fixture:GetTransactionsDepositFixture):
        account_id = get_transactions_deposit_fixture.deposit_account_response.id
        user = get_transactions_deposit_fixture.user
        response:GetAccountTransactionsResponse = api_manager.get_transactions_steps.get_transactions(account_id, user) 
        assert response.id == account_id
        assert response.balance == get_transactions_deposit_fixture.deposit_account_response.balance

    def test_transactions_transfer(self, api_manager:ApiManager,get_transactions_transfer_fixture:GetTransactionsTransferFixture ):
        account_id = get_transactions_transfer_fixture.response_transfer.fromAccountId
        user = get_transactions_transfer_fixture.user
        response:GetAccountTransactionsResponse = api_manager.get_transactions_steps.get_transactions(account_id,user)
        assert response.balance == get_transactions_transfer_fixture.response_transfer.fromAccountIdBalance
