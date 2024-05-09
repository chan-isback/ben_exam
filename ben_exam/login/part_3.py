# pylint: disable=W0107, R0903, W0106

from time import sleep
import pytest
from typing import Any, List

from ben_exam.login.elements import Elements


class CustomException(Exception):
    """Custom Exception Declare"""

    pass


class BasicRegisterInfo:
    """Bind essential Register values"""

    def __init__(
            self,
            username: str,
            password: str,
            email: str,
            is_newsletter: bool,
    ) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.is_newsletter = is_newsletter


class Login(Elements):
    """Create Data source Class"""

    def username_case(self, username: str, result: bool) -> None:
        info = BasicRegisterInfo(
            username=self.input_username,
            password=self.input_password,
            email=self.input_email,
            is_newsletter=self.input_is_newsletter,
        )
        # Change check value
        info.username = username

        elem = self.find_element_with_wait(self.username)
        elem.send_keys(info.username)
        elem = self.find_element_with_wait(self.password)
        elem.send_keys(info.password)
        elem = self.find_element_with_wait(self.email)
        elem.send_keys(info.email)
        elem = self.find_element_with_wait(self.newsletter)
        elem.click()
        elem = self.find_element_with_wait(self.register)
        elem.click()
        sleep(5)
        assert self.exist_alert() == result

