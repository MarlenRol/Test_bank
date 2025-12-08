from typing import Any, List

from src.main.api.steps.credit_steps import CreditSteps
from src.main.api.steps.transefer_steps import TransferSteps
from src.main.api.steps.deposit_steps import DepositSteps
from src.main.api.steps.user_steps import UserSteps
from src.main.api.steps.admin_steps import AdminSteps


class ApiManager:
    def __init__(self, created_obj: List[Any]):
        self.admin_steps = AdminSteps(created_obj)
        self.user_steps = UserSteps(created_obj)
        self.deposit_steps = DepositSteps(created_obj)
        self.transfer_steps = TransferSteps(created_obj)
        self.credit_steps = CreditSteps(created_obj)
        