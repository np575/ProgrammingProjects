"""
    app.py
    This file tests all methods in app.py.
"""
# pylint: disable=C0116
# pylint: disable=C0301
# pylint: disable=W0611
# pylint: disable=W1503
import unittest
import unittest.mock as mock
from os.path import dirname, join
import sys

sys.path.insert(1, join(dirname(__file__), "../"))
import app
from app import KEY_IS_BOT, KEY_BOT_COMMAND, KEY_MESSAGE, INPUT
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
dt_time = now.strftime("%d/%m/%Y %H:%M:%S")


class Test(unittest.TestCase):
    def test_on_connect(self):
        result = app.on_connect()
        if result == 1:
            self.assertTrue(True, "Socket on Connect")

    def test_on_disconnet(self):
        result = app.on_disconnect()
        if result == -1:
            self.assertTrue(True, "Socket on Disconnect")

    def test_on_new_address_input(self):
        data = {"address": "Hi there"}
        result = app.on_new_address(data)
        expected = ": {}".format(data["address"])
        self.assertEqual(expected, result)

    def test_on_new_google_user(self):
        data = {
            "name": "nisarg_patel",
            "picture": "test_image_jpg",
        }
        result = app.on_new_google_user(data)
        expected = {
            "name": "nisarg_patel",
            "picture": "test_image_jpg",
        }
        self.assertEqual(expected, result)

    def test_on_new_google_user_input(self):
        data = {
            "name": "nisarg_patel",
            "picture": "test_image_jpg",
        }
        result = app.on_new_google_user(data)
        expected = {
            "name": "nisargpatel",
            "picture": "testimage_jpg",
        }
        self.assertNotEqual(expected, result)

    def test_on_new_address_time(self):
        data = {"address": "!! time"}
        result = app.on_new_address(data)
        expected = "Jarvis(Bot)-> Hello Today's date and time: " + dt_time
        size = len(result)
        str1 = result[: size - 3]
        # print(str1)
        # print(len(expected))
        size1 = len(expected)
        str2 = expected[: size1 - 3]
        # print(str2)

        # print(type(result.find()))
        self.assertEqual(str2, str1)

    def test_on_new_address_help(self):
        data = {"address": "!! help"}
        result = app.on_new_address(data)
        # print(result)
        expected = (
            "Jarvis(Bot)-> I can be used for any of these commands: !! about | !! help | !! translate | !! time "
            + dt_string
        )
        self.assertEqual(expected, result)

    def test_on_new_address_help_fail(self):
        data = {"address": "!! help"}
        result = app.on_new_address(data)
        expected = "Jarvis(Bot): Hii, I am a chat bot.I can translate text for you in minion language. write !! help to see what commands I can take."
        self.assertNotEqual(expected, result)

    def test_on_new_address_help_fail1(self):
        data = {"address": "!! hel"}
        result = app.on_new_address(data)
        expected = "Jarvis(Bot): Hii, I am a chat bot.I can translate text for you in minion language. write !! help to see what commands I can take."
        self.assertNotEqual(expected, result)

    def test_on_new_address_translate(self):
        data = {"address": "!! translate hello"}
        result = app.on_new_address(data)
        if result == "No response from the server please try again later !":
            expected = "No response from the server please try again later !"
        else:
            expected = "Jarvis(Bot)-> Ahoy"
        self.assertEqual(expected, result)

    def test_on_new_address_about(self):
        data = {"address": "!! about"}
        result = app.on_new_address(data)
        expected = (
            "Jarvis(Bot)-> I can translate text for you in pirate language.  write !! help  to see what commands I can take. "
            + dt_string
        )
        self.assertEqual(expected, result)

    # @mock.patch('app.flask.request')
    # def test_print_request_sid(self, mock_flask_request):
    #     mock_flask_request.sid='mock_sid'
    #     result = app.print_request_sid()
    #     self.assertEqual(result, 'mock_sid')


if __name__ == "__main__":
    unittest.main()
