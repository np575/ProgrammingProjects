'''mocked_unit_tests'''
# pylint: disable=W0611
# pylint: disable=C0413
# pylint: disable=C0114

import unittest
import unittest.mock as mock
from os.path import dirname, join
import sys
from flask import request
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from nose.tools import assert_true
import requests


sys.path.insert(1, join(dirname(__file__), "../"))
import app



if __name__ == "__main__":
    unittest.main()
    