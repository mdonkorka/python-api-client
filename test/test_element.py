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
from bimdata_api_client.model.classification import Classification
from bimdata_api_client.model.layer_element import LayerElement
from bimdata_api_client.model.material_list_component import MaterialListComponent
from bimdata_api_client.model.property_set import PropertySet
globals()['Classification'] = Classification
globals()['LayerElement'] = LayerElement
globals()['MaterialListComponent'] = MaterialListComponent
globals()['PropertySet'] = PropertySet
from bimdata_api_client.model.element import Element


class TestElement(unittest.TestCase):
    """Element unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testElement(self):
        """Test Element"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Element()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
