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


class RawMaterial(object):
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
        'step_id': 'int',
        'name': 'str',
        'description': 'str',
        'category': 'str',
        'psets': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'step_id': 'step_id',
        'name': 'name',
        'description': 'description',
        'category': 'category',
        'psets': 'psets'
    }

    def __init__(self, id=None, step_id=None, name=None, description=None, category=None, psets=None, local_vars_configuration=None):  # noqa: E501
        """RawMaterial - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._step_id = None
        self._name = None
        self._description = None
        self._category = None
        self._psets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.step_id = step_id
        self.name = name
        self.description = description
        self.category = category
        self.psets = psets

    @property
    def id(self):
        """Gets the id of this RawMaterial.  # noqa: E501


        :return: The id of this RawMaterial.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RawMaterial.


        :param id: The id of this RawMaterial.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def step_id(self):
        """Gets the step_id of this RawMaterial.  # noqa: E501


        :return: The step_id of this RawMaterial.  # noqa: E501
        :rtype: int
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """Sets the step_id of this RawMaterial.


        :param step_id: The step_id of this RawMaterial.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and step_id is None:  # noqa: E501
            raise ValueError("Invalid value for `step_id`, must not be `None`")  # noqa: E501

        self._step_id = step_id

    @property
    def name(self):
        """Gets the name of this RawMaterial.  # noqa: E501


        :return: The name of this RawMaterial.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RawMaterial.


        :param name: The name of this RawMaterial.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RawMaterial.  # noqa: E501


        :return: The description of this RawMaterial.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RawMaterial.


        :param description: The description of this RawMaterial.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this RawMaterial.  # noqa: E501


        :return: The category of this RawMaterial.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RawMaterial.


        :param category: The category of this RawMaterial.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def psets(self):
        """Gets the psets of this RawMaterial.  # noqa: E501

          # noqa: E501

        :return: The psets of this RawMaterial.  # noqa: E501
        :rtype: list[int]
        """
        return self._psets

    @psets.setter
    def psets(self, psets):
        """Sets the psets of this RawMaterial.

          # noqa: E501

        :param psets: The psets of this RawMaterial.  # noqa: E501
        :type: list[int]
        """

        self._psets = psets

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
        if not isinstance(other, RawMaterial):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawMaterial):
            return True

        return self.to_dict() != other.to_dict()
