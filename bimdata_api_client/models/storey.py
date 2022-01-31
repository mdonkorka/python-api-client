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


class Storey(object):
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
        'ifc_id': 'str',
        'name': 'str',
        'elevation': 'float',
        'order': 'int',
        'models': 'list[Ifc]',
        'models_unreachable_count': 'int',
        'is_site': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ifc_id': 'ifc_id',
        'name': 'name',
        'elevation': 'elevation',
        'order': 'order',
        'models': 'models',
        'models_unreachable_count': 'models_unreachable_count',
        'is_site': 'is_site'
    }

    def __init__(self, id=None, ifc_id=None, name=None, elevation=None, order=None, models=None, models_unreachable_count=None, is_site=None, local_vars_configuration=None):  # noqa: E501
        """Storey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._ifc_id = None
        self._name = None
        self._elevation = None
        self._order = None
        self._models = None
        self._models_unreachable_count = None
        self._is_site = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ifc_id is not None:
            self.ifc_id = ifc_id
        self.name = name
        self.elevation = elevation
        if order is not None:
            self.order = order
        if models is not None:
            self.models = models
        if models_unreachable_count is not None:
            self.models_unreachable_count = models_unreachable_count
        if is_site is not None:
            self.is_site = is_site

    @property
    def id(self):
        """Gets the id of this Storey.  # noqa: E501


        :return: The id of this Storey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Storey.


        :param id: The id of this Storey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ifc_id(self):
        """Gets the ifc_id of this Storey.  # noqa: E501


        :return: The ifc_id of this Storey.  # noqa: E501
        :rtype: str
        """
        return self._ifc_id

    @ifc_id.setter
    def ifc_id(self, ifc_id):
        """Sets the ifc_id of this Storey.


        :param ifc_id: The ifc_id of this Storey.  # noqa: E501
        :type: str
        """

        self._ifc_id = ifc_id

    @property
    def name(self):
        """Gets the name of this Storey.  # noqa: E501


        :return: The name of this Storey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Storey.


        :param name: The name of this Storey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def elevation(self):
        """Gets the elevation of this Storey.  # noqa: E501


        :return: The elevation of this Storey.  # noqa: E501
        :rtype: float
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this Storey.


        :param elevation: The elevation of this Storey.  # noqa: E501
        :type: float
        """

        self._elevation = elevation

    @property
    def order(self):
        """Gets the order of this Storey.  # noqa: E501


        :return: The order of this Storey.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Storey.


        :param order: The order of this Storey.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def models(self):
        """Gets the models of this Storey.  # noqa: E501


        :return: The models of this Storey.  # noqa: E501
        :rtype: list[Ifc]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this Storey.


        :param models: The models of this Storey.  # noqa: E501
        :type: list[Ifc]
        """

        self._models = models

    @property
    def models_unreachable_count(self):
        """Gets the models_unreachable_count of this Storey.  # noqa: E501


        :return: The models_unreachable_count of this Storey.  # noqa: E501
        :rtype: int
        """
        return self._models_unreachable_count

    @models_unreachable_count.setter
    def models_unreachable_count(self, models_unreachable_count):
        """Sets the models_unreachable_count of this Storey.


        :param models_unreachable_count: The models_unreachable_count of this Storey.  # noqa: E501
        :type: int
        """

        self._models_unreachable_count = models_unreachable_count

    @property
    def is_site(self):
        """Gets the is_site of this Storey.  # noqa: E501


        :return: The is_site of this Storey.  # noqa: E501
        :rtype: bool
        """
        return self._is_site

    @is_site.setter
    def is_site(self, is_site):
        """Sets the is_site of this Storey.


        :param is_site: The is_site of this Storey.  # noqa: E501
        :type: bool
        """

        self._is_site = is_site

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
        if not isinstance(other, Storey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Storey):
            return True

        return self.to_dict() != other.to_dict()
