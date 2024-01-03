import pytest
import softest

from page_pbject.login_page import LoginPage
from test_data.data_set import DataTest


@pytest.mark.usefixtures("tc_setup")
class TestLoginApplication(softest.TestCase):

    def test_go_login_tab(self):
        login = LoginPage(self.driver)
        login.go_login_tab()

    def test_title_of_page(self):
        expected_title = " Dashboardsdsf | ellen4all"
        actual_title = self.driver.title
        self.soft_assert.assertEqual(expected_title, actual_title, "Title were not matched")

    def test_login_to_application(self):
        login = LoginPage(self.driver)
        login.go_to_login_to_application(DataTest.uname, DataTest.pwd)

    def test_logout(self):
        login = LoginPage(self.driver)
        login.logout_from_application()

