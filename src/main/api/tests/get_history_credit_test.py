import pytest

from src.main.api.modules.get_history_credit_response import GetHistoryCreditResponse
from src.main.api.fixtures.get_history_credit_fixture import GetHistoryFixture, GetHistoryRepayFixture, GetHistoryRequestFixture
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestGetHistoryCredit:
    
    def test_get_history(self,api_manager:ApiManager, get_history:GetHistoryFixture):
        response_history:GetHistoryCreditResponse = api_manager.get_history_credit_steps.get_history_credit(get_history.user)
        assert response_history.credits == []

    def test_get_history_request(self,api_manager:ApiManager, get_history_request:GetHistoryRequestFixture):
        response_history:GetHistoryCreditResponse = api_manager.get_history_credit_steps.get_history_credit(get_history_request.user)
        assert response_history.credits[0].balance == (get_history_request.request_credit_response.balance *-1)
        assert response_history.credits[0].accountId == get_history_request.request_credit_response.id

    def test_get_history_repay(self,api_manager:ApiManager, get_history_repay: GetHistoryRepayFixture):
        response_history:GetHistoryCreditResponse = api_manager.get_history_credit_steps.get_history_credit(get_history_repay.user)
        assert response_history.credits[0].balance == 0