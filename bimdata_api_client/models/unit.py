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


class Unit(object):
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
        'type': 'str',
        'name': 'str',
        'unit_type': 'str',
        'prefix': 'str',
        'dimensions': 'list[float]',
        'conversion_factor': 'float',
        'conversion_baseunit': 'Unit',
        'elements': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'unit_type': 'unit_type',
        'prefix': 'prefix',
        'dimensions': 'dimensions',
        'conversion_factor': 'conversion_factor',
        'conversion_baseunit': 'conversion_baseunit',
        'elements': 'elements'
    }

    def __init__(self, id=None, type=None, name=None, unit_type=None, prefix=None, dimensions=None, conversion_factor=None, conversion_baseunit=None, elements=None, local_vars_configuration=None):  # noqa: E501
        """Unit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._name = None
        self._unit_type = None
        self._prefix = None
        self._dimensions = None
        self._conversion_factor = None
        self._conversion_baseunit = None
        self._elements = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.name = name
        self.unit_type = unit_type
        self.prefix = prefix
        self.dimensions = dimensions
        self.conversion_factor = conversion_factor
        if conversion_baseunit is not None:
            self.conversion_baseunit = conversion_baseunit
        self.elements = elements

    @property
    def id(self):
        """Gets the id of this Unit.  # noqa: E501


        :return: The id of this Unit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Unit.


        :param id: The id of this Unit.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Unit.  # noqa: E501

        IfcDerivedUnit, IfcContextDependentUnit, IfcConversionBasedUnit, IfcSIUnit or IfcMonetaryUnit  # noqa: E501

        :return: The type of this Unit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Unit.

        IfcDerivedUnit, IfcContextDependentUnit, IfcConversionBasedUnit, IfcSIUnit or IfcMonetaryUnit  # noqa: E501

        :param type: The type of this Unit.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this Unit.  # noqa: E501

        Name of the unit (ex: DEGREE)  # noqa: E501

        :return: The name of this Unit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Unit.

        Name of the unit (ex: DEGREE)  # noqa: E501

        :param name: The name of this Unit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unit_type(self):
        """Gets the unit_type of this Unit.  # noqa: E501

        IFC type of the unit or user defined type (ex: PLANEANGLEUNIT for DEGREE and RADIAN)  # noqa: E501

        :return: The unit_type of this Unit.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this Unit.

        IFC type of the unit or user defined type (ex: PLANEANGLEUNIT for DEGREE and RADIAN)  # noqa: E501

        :param unit_type: The unit_type of this Unit.  # noqa: E501
        :type: str
        """

        self._unit_type = unit_type

    @property
    def prefix(self):
        """Gets the prefix of this Unit.  # noqa: E501

        Litteral prefix for scale (ex: MILLI, KILO, etc..)  # noqa: E501

        :return: The prefix of this Unit.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Unit.

        Litteral prefix for scale (ex: MILLI, KILO, etc..)  # noqa: E501

        :param prefix: The prefix of this Unit.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def dimensions(self):
        """Gets the dimensions of this Unit.  # noqa: E501

        List of 7 units dimensions  # noqa: E501

        :return: The dimensions of this Unit.  # noqa: E501
        :rtype: list[float]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Unit.

        List of 7 units dimensions  # noqa: E501

        :param dimensions: The dimensions of this Unit.  # noqa: E501
        :type: list[float]
        """

        self._dimensions = dimensions

    @property
    def conversion_factor(self):
        """Gets the conversion_factor of this Unit.  # noqa: E501

        Factor of conversion and base unit id (ex: DEGREE from RADIAN with factor 0.0174532925199433)  # noqa: E501

        :return: The conversion_factor of this Unit.  # noqa: E501
        :rtype: float
        """
        return self._conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, conversion_factor):
        """Sets the conversion_factor of this Unit.

        Factor of conversion and base unit id (ex: DEGREE from RADIAN with factor 0.0174532925199433)  # noqa: E501

        :param conversion_factor: The conversion_factor of this Unit.  # noqa: E501
        :type: float
        """

        self._conversion_factor = conversion_factor

    @property
    def conversion_baseunit(self):
        """Gets the conversion_baseunit of this Unit.  # noqa: E501


        :return: The conversion_baseunit of this Unit.  # noqa: E501
        :rtype: Unit
        """
        return self._conversion_baseunit

    @conversion_baseunit.setter
    def conversion_baseunit(self, conversion_baseunit):
        """Sets the conversion_baseunit of this Unit.


        :param conversion_baseunit: The conversion_baseunit of this Unit.  # noqa: E501
        :type: Unit
        """

        self._conversion_baseunit = conversion_baseunit

    @property
    def elements(self):
        """Gets the elements of this Unit.  # noqa: E501

        List of constitutive unit elements by id with corresponding exponent (ex: [meterID/1, secondID/-1] for velocity)  # noqa: E501

        :return: The elements of this Unit.  # noqa: E501
        :rtype: object
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this Unit.

        List of constitutive unit elements by id with corresponding exponent (ex: [meterID/1, secondID/-1] for velocity)  # noqa: E501

        :param elements: The elements of this Unit.  # noqa: E501
        :type: object
        """

        self._elements = elements

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
        if not isinstance(other, Unit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Unit):
            return True

        return self.to_dict() != other.to_dict()
