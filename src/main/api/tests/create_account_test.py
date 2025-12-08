import pytest
from src.main.api.classes.api_manager import ApiManager

@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, api_manager:ApiManager, create_user_request):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0