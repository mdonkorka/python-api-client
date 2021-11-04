# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from bimdata_api_client.configuration import Configuration


class InlineObject4(object):
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
        'id': 'int',
        'name': 'str',
        'color': 'str',
        'members': 'list[UserProject]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'color': 'color',
        'members': 'members'
    }

    def __init__(self, id=None, name=None, color=None, members=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject4 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._color = None
        self._members = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.color = color
        if members is not None:
            self.members = members

    @property
    def id(self):
        """Gets the id of this InlineObject4.  # noqa: E501


        :return: The id of this InlineObject4.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineObject4.


        :param id: The id of this InlineObject4.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineObject4.  # noqa: E501

        Full name of the group  # noqa: E501

        :return: The name of this InlineObject4.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject4.

        Full name of the group  # noqa: E501

        :param name: The name of this InlineObject4.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def color(self):
        """Gets the color of this InlineObject4.  # noqa: E501


        :return: The color of this InlineObject4.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this InlineObject4.


        :param color: The color of this InlineObject4.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                color is not None and len(color) > 255):
            raise ValueError("Invalid value for `color`, length must be less than or equal to `255`")  # noqa: E501

        self._color = color

    @property
    def members(self):
        """Gets the members of this InlineObject4.  # noqa: E501


        :return: The members of this InlineObject4.  # noqa: E501
        :rtype: list[UserProject]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this InlineObject4.


        :param members: The members of this InlineObject4.  # noqa: E501
        :type: list[UserProject]
        """

        self._members = members

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
        if not isinstance(other, InlineObject4):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject4):
            return True

        return self.to_dict() != other.to_dict()
