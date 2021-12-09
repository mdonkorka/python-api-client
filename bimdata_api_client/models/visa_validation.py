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


class VisaValidation(object):
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
        'visa_id': 'str',
        'validator': 'UserProject',
        'validator_id': 'int',
        'status': 'str',
        'has_commented': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'visa_id': 'visa_id',
        'validator': 'validator',
        'validator_id': 'validator_id',
        'status': 'status',
        'has_commented': 'has_commented',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, visa_id=None, validator=None, validator_id=None, status=None, has_commented=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """VisaValidation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._visa_id = None
        self._validator = None
        self._validator_id = None
        self._status = None
        self._has_commented = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if visa_id is not None:
            self.visa_id = visa_id
        if validator is not None:
            self.validator = validator
        if validator_id is not None:
            self.validator_id = validator_id
        if status is not None:
            self.status = status
        if has_commented is not None:
            self.has_commented = has_commented
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this VisaValidation.  # noqa: E501


        :return: The id of this VisaValidation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VisaValidation.


        :param id: The id of this VisaValidation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def visa_id(self):
        """Gets the visa_id of this VisaValidation.  # noqa: E501


        :return: The visa_id of this VisaValidation.  # noqa: E501
        :rtype: str
        """
        return self._visa_id

    @visa_id.setter
    def visa_id(self, visa_id):
        """Sets the visa_id of this VisaValidation.


        :param visa_id: The visa_id of this VisaValidation.  # noqa: E501
        :type: str
        """

        self._visa_id = visa_id

    @property
    def validator(self):
        """Gets the validator of this VisaValidation.  # noqa: E501


        :return: The validator of this VisaValidation.  # noqa: E501
        :rtype: UserProject
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this VisaValidation.


        :param validator: The validator of this VisaValidation.  # noqa: E501
        :type: UserProject
        """

        self._validator = validator

    @property
    def validator_id(self):
        """Gets the validator_id of this VisaValidation.  # noqa: E501

        This is the userproject_id  # noqa: E501

        :return: The validator_id of this VisaValidation.  # noqa: E501
        :rtype: int
        """
        return self._validator_id

    @validator_id.setter
    def validator_id(self, validator_id):
        """Sets the validator_id of this VisaValidation.

        This is the userproject_id  # noqa: E501

        :param validator_id: The validator_id of this VisaValidation.  # noqa: E501
        :type: int
        """

        self._validator_id = validator_id

    @property
    def status(self):
        """Gets the status of this VisaValidation.  # noqa: E501


        :return: The status of this VisaValidation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VisaValidation.


        :param status: The status of this VisaValidation.  # noqa: E501
        :type: str
        """
        allowed_values = ["P", "A", "D"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def has_commented(self):
        """Gets the has_commented of this VisaValidation.  # noqa: E501

        Return True if validator has commented the visa  # noqa: E501

        :return: The has_commented of this VisaValidation.  # noqa: E501
        :rtype: bool
        """
        return self._has_commented

    @has_commented.setter
    def has_commented(self, has_commented):
        """Sets the has_commented of this VisaValidation.

        Return True if validator has commented the visa  # noqa: E501

        :param has_commented: The has_commented of this VisaValidation.  # noqa: E501
        :type: bool
        """

        self._has_commented = has_commented

    @property
    def created_at(self):
        """Gets the created_at of this VisaValidation.  # noqa: E501


        :return: The created_at of this VisaValidation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VisaValidation.


        :param created_at: The created_at of this VisaValidation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VisaValidation.  # noqa: E501


        :return: The updated_at of this VisaValidation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VisaValidation.


        :param updated_at: The updated_at of this VisaValidation.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, VisaValidation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VisaValidation):
            return True

        return self.to_dict() != other.to_dict()
