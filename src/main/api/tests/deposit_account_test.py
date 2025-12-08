import json
import pytest
import requests
from src.main.api.modules.deposit_account_response import DepositAccountResponse
from src.main.api.modules.deposit_account_request import DepositAccountRequest
from src.main.api.modules.create_account_response import CreateAccountResponse
from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.modules.create_user_request import CreateUserRequest


@pytest.mark.api
class TestDepositAccount:    
    admin:str = "admin"
    password_admin:str ="123456"
    user_name:str = "Max16"
    password_user:str = "Pas!sw0rd"

    @staticmethod
    def auth_user(user_name:str,passwrod:str)->json:
      response=requests.post(
         url="http://localhost:4111/api/auth/token/login",
         json={
              "username": user_name,
              "password": passwrod
         },
         headers={
            "accept":"application/json",
            "Content-Type":"application/json"
         }
      )
      assert response.status_code == 200
      return response.json()

    @staticmethod
    def create_user(username:str, password:str, token:str)->json:
       response = requests.post(
         url="http://localhost:4111/api/admin/create",
         json={
              "username": username,
              "password": password,
              "role": "ROLE_CREDIT_SECRET"
         },
         headers={
            "accept":"application/json",
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json"            
         }
          )
       assert response.status_code == 200
       return response.json() 
    
    @staticmethod
    def acount_create(token:str)->json:
       response = requests.post(
          url="http://localhost:4111/api/account/create",
          headers={
             "accept":"application/json",
             "Authorization":f"Bearer {token}"
          }
       )
       assert response.status_code == 201
       return response.json()
    
    @staticmethod
    def account_deposit(id:int,amount:float, token:str)->json:
       response = requests.post(
          url="http://localhost:4111/api/account/deposit",
          json={
             "accountId":id,
             "amount":amount
          },
          headers={
             "accept":"application/json",
             "Authorization":f"Bearer {token}",
             "Content-Type":"application/json"
          }          
       )
       assert response.status_code == 200
       return response.json()
    
    @staticmethod
    def account_transfer(fromAccountId:int, toAccountId:int, amount:float, token:str )->json:
       response = requests.post(
          url="http://localhost:4111/api/account/transfer",
          json={
             "fromAccountId":fromAccountId,
             "toAccountId":toAccountId,
             "amount":amount
           },
           headers={
              "accept":"application/json",
              "Authorization":f"Bearer {token}",
              "Content-Type":"application/json"
           }
       )
       assert response.status_code == 200
       return response.json()
    
    @staticmethod
    def credit_request(id:int, amount:float, termMonths:int, token:str)->json:
       response = requests.post(
          url="http://localhost:4111/api/credit/request",
          json={
             "accountId":id,
             "amount":amount,
             "termMonths":termMonths
          },
          headers={
             "accept":"application/json",
             "Authorization":f"Bearer {token}",
             "Content-Type":"application/json"
          }
       )
       assert response.status_code == 201
       return response.json()

    @staticmethod
    def credit_repay(creditId:int, accountId:int, amount:float, token:str)->json:
       response = requests.post(
          url="http://localhost:4111/api/credit/repay",
          json={
             "creditId":creditId,
             "accountId":accountId,
             "amount":amount
          },
          headers={
             "accept":"application/json",
             "Authorization":f"Bearer {token}",
             "Content-Type":"application/json"
          }
       )
       assert response.status_code == 200
       return response.json()
    
    @staticmethod
    def delete_user(id:int, token:str)->json:
       response = requests.delete(
          url=f"http://localhost:4111/api/admin/users/{id}",
          headers={
             "accept":"application/json",
             "Authorization":f"Bearer {token}"
          }
       )
       assert response.status_code == 200
       return response.json() 

    def test_deposit_account(self):     
      response_auth = self.auth_user(self.admin, self.password_admin)
      token = response_auth.get("token")
      response_create_user = self.create_user(self.user_name, self.password_user, token)      
      user_id = response_create_user.get("id")
      user_username = response_create_user.get("username")
      user_password = "Pas!sw0rd"
      user_role =response_create_user.get("role")
      assert user_username == self.user_name and user_role=="ROLE_CREDIT_SECRET"

      response_auth = self.auth_user(self.user_name, self.password_user)
      token_user = response_auth.get("token")

      response_acount_create = self.acount_create(token_user)
      account_create_id = response_acount_create.get("id")
      account_create_number = response_acount_create.get("number")
      account_create_balance = response_acount_create.get("balance")
      assert account_create_balance == 0

      response_acount_create_1 = self.acount_create(token_user)
      account_create_id_1 = response_acount_create_1.get("id")
      account_create_number_1 = response_acount_create_1.get("number")
      account_create_balance_1 = response_acount_create_1.get("balance")
      assert account_create_balance_1 == 0

      response_account_deposit = self.account_deposit(account_create_id, 1500, token_user)
      account_deposit_id = response_account_deposit.get("id")
      account_deposit_balance = response_account_deposit.get("balance")
      assert account_create_id == account_deposit_id and account_deposit_balance == 1500

      response_account_transfer = self.account_transfer(account_create_id,account_create_id_1,500, token_user)
      account_transfer_fromAccountId = response_account_transfer.get("fromAccountId")
      account_transfer_toAccountId = response_account_transfer.get("toAccountId")
      account_transfer_fromAccountIdBalance = response_account_transfer.get("fromAccountIdBalance")
      account_deposit_balance -= 500
      assert account_deposit_balance==account_transfer_fromAccountIdBalance

      response_credit_request = self.credit_request(account_create_id, 6000, 12, token_user)
      credit_request_accountId = response_credit_request.get("id")
      credit_request_amount = response_credit_request.get("amount")
      credit_request_termMonths = response_credit_request.get("termMonths")
      credit_request_balance = response_credit_request.get("balance")
      credit_request_creditId = response_credit_request.get("creditId")
      assert (credit_request_amount+account_deposit_balance)==credit_request_balance

      response_credit_repay = self.credit_repay(credit_request_creditId,credit_request_accountId,6000, token_user)
      credit_repay_creditId = response_credit_repay.get("creditId")
      credit_repay_amountDeposited = response_credit_repay.get("amountDeposited")
      assert credit_repay_amountDeposited == credit_request_amount   

      # response_delete_user =  self.delete_user(user_id, token)
      # assert response_delete_user.get("message") == "User deleted successfully"

    
    def test_deposit_account1(self,api_manager:ApiManager, create_user_request:CreateUserRequest):     
       response:CreateAccountResponse = api_manager.deposit_steps.create_account(create_user_request) 
       assert response.balance == 0
       deposit_account_request = DepositAccountRequest(accountId=response.id, amount=1500)
       response_deposit:DepositAccountResponse = api_manager.deposit_steps.deposit_account(create_user_request,deposit_account_request)
       assert response.id == response_deposit.id



    



      


