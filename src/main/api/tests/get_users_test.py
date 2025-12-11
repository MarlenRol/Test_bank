import json
import pytest

from src.main.api.modules.get_admin_users_response import GetAdminUsersResponse
from src.main.api.modules.create_user_request import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager


@pytest.mark.api
class TestUsers:
     def test_get_users(self,api_manager:ApiManager, create_user_request:CreateUserRequest):             
          get_admin_users_response = GetAdminUsersResponse(users=api_manager.admin_steps.get_users())   
          username = [u.username for u  in get_admin_users_response.users if u.username == create_user_request.username]          
          assert  username[0] == create_user_request.username