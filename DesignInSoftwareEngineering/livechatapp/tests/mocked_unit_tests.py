
# pylint: disable=C0116
# pylint: disable=W0613
# pylint: disable=W0611
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


class Testmock(unittest.TestCase):
    @mock.patch("app.flask.request")
    def test_print_request_sid(self, mock_flask_request):
        mock_flask_request.sid = "mock_sid"
        result = app.print_request_sid()
        self.assertEqual(result, "mock_sid")

    @mock.patch("app.socketio")
    def test_send_on_connect(self, mocked_socket):
        count = 1
        mocked_socket = count
        result = app.on_connect()
        self.assertEqual(result, count)

    @mock.patch("app.socketio")
    def test_send_on_connect_fail(self, mocked_socket1):
        count = 0
        mocked_socket1 = count
        result = app.on_connect()
        self.assertNotEqual(result, count)

    @mock.patch("app.socketio")
    def test_send_on_disconnect(self, mocked_socket_disconnect):
        disconnect_count = None
        mocked_socket_disconnect = disconnect_count
        result = app.on_disconnect()
        self.assertEqual(result, disconnect_count)

    @mock.patch("app.socketio")
    def test_send_on_disconnect_fail(self, mocked_socket_disconnect1):
        disconnect_count = 0
        mocked_socket_disconnect1 = disconnect_count
        result = app.on_disconnect()
        self.assertNotEqual(result, disconnect_count)

    @mock.patch("app.socketio")
    def test_send_on_username(self, mocked_socket_username):
        name = {"name": "test_name", "picture": "img_jpg"}
        result = app.on_new_google_user(name)
        # print(result)
        test_name = {"name": "test_name", "picture": "img_jpg"}
        mocked_socket_username = test_name

        self.assertEqual(result, test_name)

    @mock.patch("app.socketio")
    def test_send_on_username_fail(self, mocked_socket_username):
        name = {"name": "test_name", "picture": "img_jpg"}
        result = app.on_new_google_user(name)

        test_name1 = {"name": "testname", "picture": "imgjpg"}
        mocked_socket_username = test_name1

        self.assertNotEqual(result, test_name1)

    @mock.patch("app.socketio")
    def test_on_new_address_time(self, mocked_socket_time):
        data = {"address": "!! time"}
        result = app.on_new_address(data)
        expected = "Jarvis(Bot)-> Hello Today's date and time: " + dt_time
        size = len(result)
        str1 = result[: size - 3]
        size1 = len(expected)
        str2 = expected[: size1 - 3]
        mocked_socket_time = str2

        # print(type(result.find()))
        self.assertEqual(str2, str1)


if __name__ == "__main__":
    unittest.main()
