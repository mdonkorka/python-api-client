# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ElementClassificationRelation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'element_uuid': 'str',
        'classification_id': 'int'
    }

    attribute_map = {
        'element_uuid': 'element_uuid',
        'classification_id': 'classification_id'
    }

    def __init__(self, element_uuid=None, classification_id=None):  # noqa: E501
        """ElementClassificationRelation - a model defined in Swagger"""  # noqa: E501

        self._element_uuid = None
        self._classification_id = None
        self.discriminator = None

        self.element_uuid = element_uuid
        self.classification_id = classification_id

    @property
    def element_uuid(self):
        """Gets the element_uuid of this ElementClassificationRelation.  # noqa: E501


        :return: The element_uuid of this ElementClassificationRelation.  # noqa: E501
        :rtype: str
        """
        return self._element_uuid

    @element_uuid.setter
    def element_uuid(self, element_uuid):
        """Sets the element_uuid of this ElementClassificationRelation.


        :param element_uuid: The element_uuid of this ElementClassificationRelation.  # noqa: E501
        :type: str
        """
        if element_uuid is None:
            raise ValueError("Invalid value for `element_uuid`, must not be `None`")  # noqa: E501
        if element_uuid is not None and len(element_uuid) < 1:
            raise ValueError("Invalid value for `element_uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._element_uuid = element_uuid

    @property
    def classification_id(self):
        """Gets the classification_id of this ElementClassificationRelation.  # noqa: E501


        :return: The classification_id of this ElementClassificationRelation.  # noqa: E501
        :rtype: int
        """
        return self._classification_id

    @classification_id.setter
    def classification_id(self, classification_id):
        """Sets the classification_id of this ElementClassificationRelation.


        :param classification_id: The classification_id of this ElementClassificationRelation.  # noqa: E501
        :type: int
        """
        if classification_id is None:
            raise ValueError("Invalid value for `classification_id`, must not be `None`")  # noqa: E501

        self._classification_id = classification_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ElementClassificationRelation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ElementClassificationRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
