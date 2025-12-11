from requests import Response
import requests
from src.main.api.modules.get_admin_users_response import GetAdminUsersResponse
from src.main.api.requests.requester import Requester


class GetAdminUsersRequester(Requester):
    def get(self,user_id = None) -> GetAdminUsersResponse | Response:
        url = f"{self.base_url}/admin/users"
        response = requests.get(
            url = url,            
            headers=self.headers
        )
        self.response_spec(response)
        return GetAdminUsersResponse(**response.json())