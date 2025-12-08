import pytest

from src.main.api.modules.repay_credit_response import RepayCreditResponse
from src.main.api.modules.repay_credit_request import RepayCreditRequest
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.modules.request_credit_response import RequestCreditResponse
from src.main.api.modules.request_credit_request import RequestCreditRequest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest
@pytest.mark.api
class TestCredit:

    def test_credit_request(self,api_manager:ApiManager, create_user_request:CreateUserRequest):
      response:CreateAccountResponse = api_manager.user_steps.create_account(create_user_request)
      assert response.balance == 0

      request_credit_request = RequestCreditRequest(accountId=response.id,amount=5000,termMonths=12)
      request_credit_response:RequestCreditResponse = api_manager.credit_steps.credit_request(create_user_request,request_credit_request)
      assert request_credit_response.id == request_credit_request.accountId and request_credit_response.amount == request_credit_request.amount and request_credit_request.termMonths == request_credit_response.termMonths

    def test_credit_repay(self, api_manager:ApiManager, create_user_request:CreateUserRequest):
       
      response:CreateAccountResponse = api_manager.user_steps.create_account(create_user_request)
      assert response.balance == 0

      request_credit_request = RequestCreditRequest(accountId=response.id,amount=5000,termMonths=12)
      request_credit_response:RequestCreditResponse = api_manager.credit_steps.credit_request(create_user_request,request_credit_request)
      assert request_credit_response.id == request_credit_request.accountId and request_credit_response.amount == request_credit_request.amount and request_credit_request.termMonths == request_credit_response.termMonths

      repay_credit_request = RepayCreditRequest(creditId=request_credit_response.creditId,accountId=request_credit_response.id,amount=5000)
      repay_credit_response:RepayCreditResponse = api_manager.credit_steps.credit_repay(create_user_request, repay_credit_request)
      assert repay_credit_response.creditId == repay_credit_request.creditId and repay_credit_response.amountDeposited == request_credit_request.amount



       
   
      