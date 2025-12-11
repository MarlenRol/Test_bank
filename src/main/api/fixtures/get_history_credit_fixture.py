import pytest

from src.main.api.modules.repay_credit_response import RepayCreditResponse
from src.main.api.modules.request_credit_response import RequestCreditResponse
from src.main.api.fixtures.credit_fixture import CreditRepayFixture, CreditRequestFixture
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest

class GetHistoryFixture:
    user:CreateUserRequest
    response_account: CreateAccountResponse
    def __init__(self,user,response_account):
        self.user = user
        self.response_account = response_account

class GetHistoryRequestFixture:
    user: CreateUserRequest
    request_credit_response:RequestCreditResponse

    def __init__(self,user,request_credit_response):
        self.user=user
        self.request_credit_response = request_credit_response

class GetHistoryRepayFixture:
    user: CreateUserRequest
    repay_credit_response:RepayCreditResponse
    
    def __init__(self,user,repay_credit_response):
        self.user = user
        self.repay_credit_response = repay_credit_response

@pytest.fixture
def get_history(api_manager:ApiManager, create_user_request:CreateUserRequest):
    response_account:CreateAccountResponse = api_manager.user_steps.create_account(create_user_request) 
    return GetHistoryFixture(create_user_request, response_account)

@pytest.fixture
def get_history_request(api_manager:ApiManager, credit_request_fixture:CreditRequestFixture):
    request_credit_response:RequestCreditResponse =  api_manager.credit_steps.credit_request(credit_request_fixture.user, credit_request_fixture.request_credit_request)
    return GetHistoryRequestFixture(credit_request_fixture.user,request_credit_response)

@pytest.fixture
def get_history_repay(api_manager:ApiManager, credit_repay_fixture:CreditRepayFixture ):
    repay_credit_response:RepayCreditResponse = api_manager.credit_steps.credit_repay(credit_repay_fixture.user, credit_repay_fixture.repay_credit_request)
    return GetHistoryRepayFixture(credit_repay_fixture.user, repay_credit_response)