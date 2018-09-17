# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.cloud_api import CloudApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestCloudApi(unittest.TestCase):
    """CloudApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.cloud_api.CloudApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cloud(self):
        """Test case for create_cloud

        """
        pass

    def test_create_cloud_user(self):
        """Test case for create_cloud_user

        """
        pass

    def test_create_demo(self):
        """Test case for create_demo

        """
        pass

    def test_delete_cloud_user(self):
        """Test case for delete_cloud_user

        """
        pass

    def test_full_update_cloud(self):
        """Test case for full_update_cloud

        """
        pass

    def test_full_update_cloud_user(self):
        """Test case for full_update_cloud_user

        """
        pass

    def test_get_cloud(self):
        """Test case for get_cloud

        """
        pass

    def test_get_cloud_size(self):
        """Test case for get_cloud_size

        """
        pass

    def test_get_cloud_user(self):
        """Test case for get_cloud_user

        """
        pass

    def test_get_cloud_users(self):
        """Test case for get_cloud_users

        """
        pass

    def test_get_clouds(self):
        """Test case for get_clouds

        """
        pass

    def test_update_cloud(self):
        """Test case for update_cloud

        """
        pass

    def test_update_cloud_user(self):
        """Test case for update_cloud_user

        """
        pass


if __name__ == '__main__':
    unittest.main()
