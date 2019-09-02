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


class CheckerResult(object):
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
        'status': 'str',
        'result': 'str',
        'collisions': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'error_detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'result': 'result',
        'collisions': 'collisions',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'error_detail': 'error_detail'
    }

    def __init__(self, id=None, status=None, result=None, collisions=None, created_at=None, updated_at=None, error_detail=None):  # noqa: E501
        """CheckerResult - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._status = None
        self._result = None
        self._collisions = None
        self._created_at = None
        self._updated_at = None
        self._error_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        self.result = result
        self.collisions = collisions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if error_detail is not None:
            self.error_detail = error_detail

    @property
    def id(self):
        """Gets the id of this CheckerResult.  # noqa: E501


        :return: The id of this CheckerResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckerResult.


        :param id: The id of this CheckerResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this CheckerResult.  # noqa: E501


        :return: The status of this CheckerResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckerResult.


        :param status: The status of this CheckerResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["C", "P", "E"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def result(self):
        """Gets the result of this CheckerResult.  # noqa: E501


        :return: The result of this CheckerResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CheckerResult.


        :param result: The result of this CheckerResult.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def collisions(self):
        """Gets the collisions of this CheckerResult.  # noqa: E501


        :return: The collisions of this CheckerResult.  # noqa: E501
        :rtype: str
        """
        return self._collisions

    @collisions.setter
    def collisions(self, collisions):
        """Sets the collisions of this CheckerResult.


        :param collisions: The collisions of this CheckerResult.  # noqa: E501
        :type: str
        """

        self._collisions = collisions

    @property
    def created_at(self):
        """Gets the created_at of this CheckerResult.  # noqa: E501


        :return: The created_at of this CheckerResult.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CheckerResult.


        :param created_at: The created_at of this CheckerResult.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CheckerResult.  # noqa: E501


        :return: The updated_at of this CheckerResult.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CheckerResult.


        :param updated_at: The updated_at of this CheckerResult.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def error_detail(self):
        """Gets the error_detail of this CheckerResult.  # noqa: E501


        :return: The error_detail of this CheckerResult.  # noqa: E501
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """Sets the error_detail of this CheckerResult.


        :param error_detail: The error_detail of this CheckerResult.  # noqa: E501
        :type: str
        """
        if error_detail is not None and len(error_detail) < 1:
            raise ValueError("Invalid value for `error_detail`, length must be greater than or equal to `1`")  # noqa: E501

        self._error_detail = error_detail

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
        if not isinstance(other, CheckerResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other