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
from bimdata_api_client.model.property_set_request import PropertySetRequest
globals()['PropertySetRequest'] = PropertySetRequest
from bimdata_api_client.model.material_request import MaterialRequest


class TestMaterialRequest(unittest.TestCase):
    """MaterialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMaterialRequest(self):
        """Test MaterialRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MaterialRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
