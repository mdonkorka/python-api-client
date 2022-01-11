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


class Visa(object):
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
        'validations': 'list[VisaValidation]',
        'validations_in_error': 'list[int]',
        'creator': 'UserProject',
        'creator_id': 'int',
        'status': 'str',
        'description': 'str',
        'document': 'Document',
        'comments': 'list[VisaComment]',
        'deadline': 'date',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'validations': 'validations',
        'validations_in_error': 'validations_in_error',
        'creator': 'creator',
        'creator_id': 'creator_id',
        'status': 'status',
        'description': 'description',
        'document': 'document',
        'comments': 'comments',
        'deadline': 'deadline',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, validations=None, validations_in_error=None, creator=None, creator_id=None, status=None, description=None, document=None, comments=None, deadline=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Visa - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._validations = None
        self._validations_in_error = None
        self._creator = None
        self._creator_id = None
        self._status = None
        self._description = None
        self._document = None
        self._comments = None
        self._deadline = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if validations is not None:
            self.validations = validations
        if validations_in_error is not None:
            self.validations_in_error = validations_in_error
        if creator is not None:
            self.creator = creator
        if creator_id is not None:
            self.creator_id = creator_id
        if status is not None:
            self.status = status
        self.description = description
        if document is not None:
            self.document = document
        if comments is not None:
            self.comments = comments
        self.deadline = deadline
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Visa.  # noqa: E501


        :return: The id of this Visa.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Visa.


        :param id: The id of this Visa.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def validations(self):
        """Gets the validations of this Visa.  # noqa: E501


        :return: The validations of this Visa.  # noqa: E501
        :rtype: list[VisaValidation]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this Visa.


        :param validations: The validations of this Visa.  # noqa: E501
        :type: list[VisaValidation]
        """

        self._validations = validations

    @property
    def validations_in_error(self):
        """Gets the validations_in_error of this Visa.  # noqa: E501

        Validation IDs where one or more validators have no longer access to the visa document.  # noqa: E501

        :return: The validations_in_error of this Visa.  # noqa: E501
        :rtype: list[int]
        """
        return self._validations_in_error

    @validations_in_error.setter
    def validations_in_error(self, validations_in_error):
        """Sets the validations_in_error of this Visa.

        Validation IDs where one or more validators have no longer access to the visa document.  # noqa: E501

        :param validations_in_error: The validations_in_error of this Visa.  # noqa: E501
        :type: list[int]
        """

        self._validations_in_error = validations_in_error

    @property
    def creator(self):
        """Gets the creator of this Visa.  # noqa: E501


        :return: The creator of this Visa.  # noqa: E501
        :rtype: UserProject
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Visa.


        :param creator: The creator of this Visa.  # noqa: E501
        :type: UserProject
        """

        self._creator = creator

    @property
    def creator_id(self):
        """Gets the creator_id of this Visa.  # noqa: E501

        This is the userproject_id. This field is only used if the call is made from an App  # noqa: E501

        :return: The creator_id of this Visa.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Visa.

        This is the userproject_id. This field is only used if the call is made from an App  # noqa: E501

        :param creator_id: The creator_id of this Visa.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def status(self):
        """Gets the status of this Visa.  # noqa: E501


        :return: The status of this Visa.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Visa.


        :param status: The status of this Visa.  # noqa: E501
        :type: str
        """
        allowed_values = ["O", "A", "C"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def description(self):
        """Gets the description of this Visa.  # noqa: E501

        Description of the visa  # noqa: E501

        :return: The description of this Visa.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Visa.

        Description of the visa  # noqa: E501

        :param description: The description of this Visa.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def document(self):
        """Gets the document of this Visa.  # noqa: E501


        :return: The document of this Visa.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Visa.


        :param document: The document of this Visa.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def comments(self):
        """Gets the comments of this Visa.  # noqa: E501


        :return: The comments of this Visa.  # noqa: E501
        :rtype: list[VisaComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Visa.


        :param comments: The comments of this Visa.  # noqa: E501
        :type: list[VisaComment]
        """

        self._comments = comments

    @property
    def deadline(self):
        """Gets the deadline of this Visa.  # noqa: E501


        :return: The deadline of this Visa.  # noqa: E501
        :rtype: date
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this Visa.


        :param deadline: The deadline of this Visa.  # noqa: E501
        :type: date
        """

        self._deadline = deadline

    @property
    def created_at(self):
        """Gets the created_at of this Visa.  # noqa: E501


        :return: The created_at of this Visa.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Visa.


        :param created_at: The created_at of this Visa.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Visa.  # noqa: E501


        :return: The updated_at of this Visa.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Visa.


        :param updated_at: The updated_at of this Visa.  # noqa: E501
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
        if not isinstance(other, Visa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Visa):
            return True

        return self.to_dict() != other.to_dict()
