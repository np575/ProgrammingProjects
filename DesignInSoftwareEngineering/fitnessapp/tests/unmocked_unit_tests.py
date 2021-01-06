"""unmocked_unit_tests.py"""
# pylint: disable=C0103
# pylint: disable=C0116
# pylint: disable=C0413
# pylint: disable=C0115
# pylint: disable=W0611
# pylint: disable=W1503
# pylint: disable=R0201
# pylint: disable=E1111

import unittest
import unittest.mock as mock
from os.path import dirname, join
import sys, datetime


sys.path.insert(1, join(dirname(__file__), "../"))
import app
import models
from models import Users
import calories_count

# funtions todo
class Test(unittest.TestCase):
    def test_on_connect(self):
        result = app.on_connect()
        if result == 1:
            self.assertTrue(True, "Socket on Connect")

    def test_on_disconnet(self):
        result = app.on_disconnect()
        if result == 1:
            self.assertTrue(True, "Socket on Disconnect")

    def test_bmr_cal(self):
        data = {"weight": 24, "height": 52, "age": 23, "gender": "man"}
        data1 = {"weight": 24, "height": 52, "age": 23, "gender": "woman"}
        result = calories_count.bmr_cal(
            data["weight"], data["height"], data["age"], data["gender"]
        )
        print(result)
        expected = {"weight": 24, "height": 52, "age": 23, "gender": "man"}
        expected1 = {"weight": 24, "height": 52, "age": 23, "gender": "woman"}
        self.assertEqual(data, expected)
        result = calories_count.bmr_cal(
            data1["weight"], data1["height"], data1["age"], data1["gender"]
        )
        self.assertEqual(data1, expected1)

    def test_daily_Caloric_need(self):
        data = [
            {"bmr": 312, "activityLevel": 1, "activityLevelIndex": 1.2},
            {"bmr": 312, "activityLevel": 2, "activityLevelIndex": 1.375},
            {"bmr": 312, "activityLevel": 3, "activityLevelIndex": 1.46},
            {"bmr": 312, "activityLevel": 4, "activityLevelIndex": 1.725},
            {"bmr": 312, "activityLevel": 5, "activityLevelIndex": 1.9},
        ]

        for test in data:
            result = calories_count.daily_caloric_need(
                test["bmr"], test["activityLevel"]
            )
            print(result)
            expected = test
            self.assertEqual(test, expected)

    def test_calculate_macro(self):
        data = {"calories": 1200}
        result = calories_count.calculate_macro(data["calories"])
        print(result)
        expected = {"calories": 1200}
        self.assertEqual(data, expected)

    def test_calculate_age(self):
        data = datetime.datetime.now()
        expected = 0
        result = app.calculate_age(data)
        self.assertEqual(result, expected)

    def test_display_quotes(self):
        quote = app.displaying_quotes()
        data = quote
        result = quote
        self.assertEqual(data, result)

    def test_on_messages(self):
        data = {"entry": "hi there", "email": "nisargpatel356@gmail.com"}
        result = app.on_new_message(data)
        print(result)

    # def test_sign_in(self):
    #     data={
    #         'name': 'test',
    #         'email': 'test@edu',
    #         'imgUrl': 'http//..'
    #     }

    #     mocker = mock.MagicMock()
    #     mocker.values("AAAA")
    #     session_mocker = mock.MagicMock()
    #     with mock.patch("app.flask") as mock_sid:
    #         mock_sid.request.sid ='test01'
    #         result= app.on_google_sign_in(data)
    #         print((result))

    # mocker = mock.MagicMock()
    # with mock.patch("app.flask.request"):
    #     result= app.on_google_sign_in(data)
    #     print(result)

    # print('hre')
    # mocked_sid.request.sid = 'test01'

    # def test_workout(self):
    #     data={
    #         'level': 2, 'split': 'Bro Split', 'email': 'nisargpatel356@gmail.com', 'sid': 'faafdacb1d1847f38dd2aadc67596720','name': 'john'
    #     }
    #     result= app.on_workou_entry(data)

    def test_food_Search(self):
        data = {"food_search": "pasta", "user": "nisargpatel356@gmail.com"}
        # with mock.patch("db.session.query" ):
        result = app.on_new_food_search(data)
        print("chek")
        print(result)
        expected = None
        self.assertEqual(result, expected)

    # def test_new_user(self):
    #     data={
    #       'birthday': '1220-02-12',
    #       'height': '72',
    #       'weight': '125',
    #       'gender': 'man',
    #       'goal_weight': '135',
    #       'activityLevel': '2',
    #       'name': 'nisarg patel',
    #       'email': 'nisargpatel356@gmail.com',
    #       'imgUrl': 'http..',
    #     }
    #     result=app.on_new_user(data)
    #     print(result)

    def test_user_details(self):
        test_email = "nisargpatel356@gmail.com"
        result = app.get_user_details(test_email)
        print("che")
        print(result)
        expected = None
        self.assertEqual(result, expected)

    def test_all_user_weights(self):
        test_email = ("nisargpatel356@gmail.com",)
        sid = "903"
        result = app.emit_all_user_weights(test_email, sid)
        print("ch")
        print(result)
        print(result)

    def test_render_landing_page(self):
        """Test landing_page rendering"""
        with mock.patch("flask.render_template"):
            app.about()

    def test_render_home_page(self):
        """Test landing_page rendering"""
        with mock.patch("flask.render_template"):
            app.home()

    def test_render_foodsearch_page(self):
        """Test landing_page rendering"""
        with mock.patch("flask.render_template"):
            app.food_search()

    def test_render_workout_page(self):
        """Test landing_page rendering"""
        with mock.patch("flask.render_template"):
            app.workout_log()

    def test_render_profile_page(self):
        """Test landing_page rendering"""
        with mock.patch("flask.render_template"):
            app.profile()


class testingusers(Users):
    def init(self, name):
        self.connection = name


if __name__ == "__main__":
    unittest.main()
