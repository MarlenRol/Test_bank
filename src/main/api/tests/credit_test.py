import pytest

from src.main.api.modules.get_history_credit_response import GetHistoryCreditResponse
from src.main.api.fixtures.credit_fixture import CreditRepayFixture, CreditRequestFixture
from src.main.api.modules.repay_credit_response import RepayCreditResponse
from src.main.api.modules.repay_credit_request import RepayCreditRequest
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.modules.request_credit_response import RequestCreditResponse
from src.main.api.modules.request_credit_request import RequestCreditRequest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest
@pytest.mark.api
class TestCredit:

    def test_credit_request(self,api_manager:ApiManager, credit_request_fixture:CreditRequestFixture):
      request_credit_response:RequestCreditResponse = api_manager.credit_steps.credit_request(credit_request_fixture.user,credit_request_fixture.request_credit_request)
      response_history:GetHistoryCreditResponse = api_manager.get_history_credit_steps.get_history_credit(credit_request_fixture.user)
      assert request_credit_response.amount == response_history.credits[0].amount 

    def test_credit_repay(self, api_manager:ApiManager, credit_repay_fixture:CreditRepayFixture):
      repay_credit_response:RepayCreditResponse = api_manager.credit_steps.credit_repay(credit_repay_fixture.user, credit_repay_fixture.repay_credit_request)
      response_history:GetHistoryCreditResponse = api_manager.get_history_credit_steps.get_history_credit(credit_repay_fixture.user)
      assert repay_credit_response.amountDeposited == response_history.credits[0].amount 



       
   
      