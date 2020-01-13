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


class RawElement(object):
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
        'uuid': 'str',
        'type': 'str',
        'attributes': 'int',
        'psets': 'list[int]',
        'classifications': 'list[int]',
        'layers': 'list[int]',
        'systems': 'list[int]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'type': 'type',
        'attributes': 'attributes',
        'psets': 'psets',
        'classifications': 'classifications',
        'layers': 'layers',
        'systems': 'systems'
    }

    def __init__(self, uuid=None, type=None, attributes=None, psets=None, classifications=None, layers=None, systems=None, local_vars_configuration=None):  # noqa: E501
        """RawElement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._type = None
        self._attributes = None
        self._psets = None
        self._classifications = None
        self._layers = None
        self._systems = None
        self.discriminator = None

        self.uuid = uuid
        self.type = type
        self.attributes = attributes
        self.psets = psets
        self.classifications = classifications
        self.layers = layers
        self.systems = systems

    @property
    def uuid(self):
        """Gets the uuid of this RawElement.  # noqa: E501


        :return: The uuid of this RawElement.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RawElement.


        :param uuid: The uuid of this RawElement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) < 1):
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this RawElement.  # noqa: E501


        :return: The type of this RawElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RawElement.


        :param type: The type of this RawElement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this RawElement.  # noqa: E501


        :return: The attributes of this RawElement.  # noqa: E501
        :rtype: int
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this RawElement.


        :param attributes: The attributes of this RawElement.  # noqa: E501
        :type: int
        """

        self._attributes = attributes

    @property
    def psets(self):
        """Gets the psets of this RawElement.  # noqa: E501


        :return: The psets of this RawElement.  # noqa: E501
        :rtype: list[int]
        """
        return self._psets

    @psets.setter
    def psets(self, psets):
        """Sets the psets of this RawElement.


        :param psets: The psets of this RawElement.  # noqa: E501
        :type: list[int]
        """

        self._psets = psets

    @property
    def classifications(self):
        """Gets the classifications of this RawElement.  # noqa: E501


        :return: The classifications of this RawElement.  # noqa: E501
        :rtype: list[int]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this RawElement.


        :param classifications: The classifications of this RawElement.  # noqa: E501
        :type: list[int]
        """

        self._classifications = classifications

    @property
    def layers(self):
        """Gets the layers of this RawElement.  # noqa: E501


        :return: The layers of this RawElement.  # noqa: E501
        :rtype: list[int]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this RawElement.


        :param layers: The layers of this RawElement.  # noqa: E501
        :type: list[int]
        """

        self._layers = layers

    @property
    def systems(self):
        """Gets the systems of this RawElement.  # noqa: E501


        :return: The systems of this RawElement.  # noqa: E501
        :rtype: list[int]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this RawElement.


        :param systems: The systems of this RawElement.  # noqa: E501
        :type: list[int]
        """

        self._systems = systems

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
        if not isinstance(other, RawElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawElement):
            return True

        return self.to_dict() != other.to_dict()
