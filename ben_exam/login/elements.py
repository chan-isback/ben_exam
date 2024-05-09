# pylint: disable=R0902, C0209

from typing import Any
from selenium.webdriver.common.by import By

from ben_exam.common import TestTools


class Elements(TestTools):
    """Elements for find_elements"""

    def __init__(self, driver: Any) -> None:
        """init params"""

        super().__init__(driver)

        # BEN exam site
        self.username = [By.ID, "username"]
        self.password = [By.ID, "password"]
        self.email = [By.ID, "email"]
        self.newsletter = [By.ID, "newsletter"]
        self.register = [By.XPATH, '//input[@value="Register"]']

        # BEN exam basic info
        self.input_username = "christoper"
        self.input_password = "Exam20240509!"
        self.input_email = "christoper@beninc.ai"
        self.input_is_newsletter = True
