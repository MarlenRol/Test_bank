import pytest

from src.main.api.modules.transfer_account_request import TransferAccountRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.fixtures.deposit_fixture import DepositFixture
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest

class TransferFixture:
         user:CreateUserRequest
         transfer_account_request:TransferAccountRequest
         amount_fixture:float
         def __init__(self, user:CreateUserRequest,transfer_account_request:TransferAccountRequest,amount_fixture:float):
               self.user = user
               self.transfer_account_request = transfer_account_request
               self.amount_fixture = amount_fixture

@pytest.fixture
def transfer_account(api_manager:ApiManager, create_account_deposit:DepositFixture):
    account_one:DepositAccountRequest = create_account_deposit.deposit_accounts[0]
    account_two:DepositAccountRequest = create_account_deposit.deposit_accounts[1]

    api_manager.deposit_steps.deposit_account(create_account_deposit.user, account_one)

    amount_transfer = RandomModelGenerator.generate(TransferAccountRequest).amount
    while account_one.amount<amount_transfer:
         amount_transfer = RandomModelGenerator.generate(TransferAccountRequest).amount

    amount_fixture = account_one.amount-amount_transfer
    return TransferFixture(create_account_deposit.user, TransferAccountRequest(fromAccountId=account_one.accountId,toAccountId=account_two.accountId,amount=amount_transfer),amount_fixture)
    

