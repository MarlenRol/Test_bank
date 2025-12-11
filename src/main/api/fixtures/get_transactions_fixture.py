import pytest
from src.main.api.modules.transfer_account_response import TransferAccountResponse
from src.main.api.fixtures.transfer_fixture import TransferFixture
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.fixtures.deposit_fixture import DepositFixture
from src.main.api.classes.api_manager import ApiManager

class GetTransactionsDepositFixture:
    user:CreateUserRequest
    deposit_account_response:DepositAccountResponse
    def __init__(self,user,deposit_account_response):
        self.user=user
        self.deposit_account_response=deposit_account_response

class GetTransactionsTransferFixture:
    user:CreateUserRequest
    response_transfer:TransferAccountResponse
    def __init__(self,user,response_transfer):
        self.user = user
        self.response_transfer = response_transfer        

@pytest.fixture
def get_transactions_deposit_fixture(api_manager:ApiManager, create_account_deposit:DepositFixture):
    account:DepositAccountRequest = create_account_deposit.deposit_accounts[0]    
    deposit_account_response:DepositAccountResponse = api_manager.deposit_steps.deposit_account(create_account_deposit.user, account)
    return GetTransactionsDepositFixture(create_account_deposit.user,deposit_account_response)

@pytest.fixture 
def get_transactions_transfer_fixture(api_manager:ApiManager,transfer_account:TransferFixture):
    response_transfer:TransferAccountResponse = api_manager.transfer_steps.transfer_account(transfer_account.user,transfer_account.transfer_account_request)    
    return GetTransactionsTransferFixture(transfer_account.user, response_transfer)