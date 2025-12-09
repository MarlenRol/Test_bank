import pytest
from src.main.api.fixtures.deposit_fixture import DepositFixture
from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestDepositAccount:    
        
    def test_deposit_account(self,api_manager:ApiManager, create_account_deposit:DepositFixture):
       account:DepositAccountRequest = create_account_deposit.deposit_accounts[0]
       response_deposit:DepositAccountResponse = api_manager.deposit_steps.deposit_account(create_account_deposit.user, account)
       assert  response_deposit.balance == account.amount



    



      


