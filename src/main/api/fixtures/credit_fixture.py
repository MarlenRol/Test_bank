import pytest

from src.main.api.modules.request_credit_response import RequestCreditResponse
from src.main.api.modules.repay_credit_request import RepayCreditRequest
from src.main.api.modules.request_credit_request import RequestCreditRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager

class CreditRequestFixture:
    user:CreateUserRequest
    request_credit_request:RequestCreditRequest
    
    def __init__(self,user,request_credit_request):
        self.user = user
        self.request_credit_request = request_credit_request
        
class CreditRepayFixture:
    user:CreateUserRequest
    repay_credit_request:RepayCreditRequest
    
    def __init__(self, user, repay_credit_request):
        self.user = user
        self.repay_credit_request = repay_credit_request

@pytest.fixture
def credit_request_fixture(api_manager:ApiManager,create_user_request:CreateUserRequest):    
    user_request = create_user_request
    response_account:CreateAccountResponse = api_manager.user_steps.create_account(user_request)

    request_credit_random:RequestCreditRequest = RandomModelGenerator.generate(RequestCreditRequest)
   
    return  CreditRequestFixture(user_request,RequestCreditRequest(accountId=response_account.id,
                                amount=request_credit_random.amount, 
                                termMonths=request_credit_random.termMonths) )

@pytest.fixture
def credit_repay_fixture(api_manager:ApiManager,credit_request_fixture:CreditRequestFixture):

   request_credit_response:RequestCreditResponse =  api_manager.credit_steps.credit_request(credit_request_fixture.user, credit_request_fixture.request_credit_request)

   return CreditRepayFixture(credit_request_fixture.user,RepayCreditRequest(creditId=request_credit_response.creditId,
                                                                            accountId=request_credit_response.id, 
                                                                            amount=request_credit_response.amount) )

  

