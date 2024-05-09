from typing import Any
from ben_exam.login.part_3 import Login


def test_username(driver: Any) -> None:
    """launch fill the form"""
    login = Login(driver)
    login.username_case('mike', False)

def test_username2(driver: Any) -> None:
    """launch fill the form"""
    login = Login(driver)
    login.username_case('christoper', True)
