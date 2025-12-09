from typing import List
import pytest

from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest

class DepositFixture:
    user:CreateUserRequest
    deposit_accounts:DepositAccountRequest

    def __init__(self,user:CreateUserRequest,deposit_account:DepositAccountRequest):
        self.user=user
        self.deposit_accounts = deposit_account

        

@pytest.fixture
def create_account_deposit(api_manager:ApiManager, create_user_request:CreateUserRequest):
    user_request = create_user_request    

    response_account_one:CreateAccountResponse = api_manager.user_steps.create_account(user_request)
    response_account_two:CreateAccountResponse = api_manager.user_steps.create_account(user_request)

    amount_random_one = RandomModelGenerator.generate(DepositAccountRequest).amount
    amount_random_two = RandomModelGenerator.generate(DepositAccountRequest).amount

    deposit_account_request_one = DepositAccountRequest(accountId=response_account_one.id, amount=amount_random_one)
    deposit_account_request_two = DepositAccountRequest(accountId=response_account_two.id, amount=amount_random_two)

    return DepositFixture(user_request,[deposit_account_request_one, deposit_account_request_two])