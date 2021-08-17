# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import bimdata_api_client
from bimdata_api_client.models.ifc import Ifc  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestIfc(unittest.TestCase):
    """Ifc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Ifc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.ifc.Ifc()  # noqa: E501
        if include_optional :
            return Ifc(
                id = 56, 
                name = '0', 
                creator = bimdata_api_client.models.user.User(
                    id = 56, 
                    email = '0', 
                    firstname = '0', 
                    lastname = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cloud_role = 56, 
                    project_role = 56, 
                    provider = '0', 
                    sub = '0', 
                    profile_picture = '0', ), 
                status = '0', 
                source = 'UPLOAD', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                document_id = '0', 
                document = bimdata_api_client.models.document.Document(
                    id = 56, 
                    parent = 56, 
                    parent_id = 56, 
                    creator = 56, 
                    project = 56, 
                    name = '0', 
                    file_name = '0', 
                    description = '0', 
                    file = '0', 
                    size = 0, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    ifc_source = 'UPLOAD', 
                    ifc_id = '0', 
                    user_permission = 56, ), 
                structure_file = '0', 
                systems_file = '0', 
                map_file = '0', 
                gltf_file = '0', 
                bvh_tree_file = '0', 
                viewer_360_file = '0', 
                xkt_file = '0', 
                project_id = '0', 
                world_position = [
                    1.337
                    ], 
                errors = [
                    '0'
                    ], 
                warnings = [
                    '0'
                    ], 
                archived = True, 
                version = '0', 
                north_vector = [
                    [
                        1.337
                        ]
                    ], 
                recommanded_2d_angle = 1.337
            )
        else :
            return Ifc(
        )

    def testIfc(self):
        """Test Ifc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
