"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bimdata_api_client
from bimdata_api_client.model.check_plan import CheckPlan
from bimdata_api_client.model.checker_result import CheckerResult
from bimdata_api_client.model.model import Model
from bimdata_api_client.model.user import User
globals()['CheckPlan'] = CheckPlan
globals()['CheckerResult'] = CheckerResult
globals()['Model'] = Model
globals()['User'] = User
from bimdata_api_client.model.ifc_checker import IfcChecker


class TestIfcChecker(unittest.TestCase):
    """IfcChecker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIfcChecker(self):
        """Test IfcChecker"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IfcChecker()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
