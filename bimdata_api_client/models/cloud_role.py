# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from bimdata_api_client.configuration import Configuration


class CloudRole(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cloud': 'int',
        'role': 'int'
    }

    attribute_map = {
        'cloud': 'cloud',
        'role': 'role'
    }

    def __init__(self, cloud=None, role=None, local_vars_configuration=None):  # noqa: E501
        """CloudRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud = None
        self._role = None
        self.discriminator = None

        self.cloud = cloud
        if role is not None:
            self.role = role

    @property
    def cloud(self):
        """Gets the cloud of this CloudRole.  # noqa: E501


        :return: The cloud of this CloudRole.  # noqa: E501
        :rtype: int
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CloudRole.


        :param cloud: The cloud of this CloudRole.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cloud is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud`, must not be `None`")  # noqa: E501

        self._cloud = cloud

    @property
    def role(self):
        """Gets the role of this CloudRole.  # noqa: E501

        Role of the user in the cloud  # noqa: E501

        :return: The role of this CloudRole.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CloudRole.

        Role of the user in the cloud  # noqa: E501

        :param role: The role of this CloudRole.  # noqa: E501
        :type: int
        """

        self._role = role

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudRole):
            return True

        return self.to_dict() != other.to_dict()
