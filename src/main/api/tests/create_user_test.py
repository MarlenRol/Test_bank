import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.modules.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateUser:
    
    @pytest.mark.parametrize(
          "create_user_request",
          [RandomModelGenerator.generate(CreateUserRequest)]
      )
    def test_create_user_valid(self, api_manager:ApiManager, create_user_request):
      response= api_manager.admin_steps.create_user(create_user_request)
      assert create_user_request.username == response.username
      assert create_user_request.role == response.role

    @pytest.mark.parametrize("username, password",      
      [("абв","Pas!sw0rd"),
            ("ab","Pas!sw0rd"),
            ("abv!","Pas!sw0rd"),
            ("Max08","Pas!sw0rд"),
            ("Max09","Pas!sw0"),
            ("Max10","pas!sw0rd"),
            ("Max11","PASSW0RD"),
            ("Max12","PAS!SWRD")])
    def test_create_user_invalid(self, username, password, api_manager:ApiManager):
      create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_CREDIT_SECRET")
      api_manager.admin_steps.create_invalid_user(create_user_request)
