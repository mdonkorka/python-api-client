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


class User(object):
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
        'email': 'str',
        'company': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_role': 'int',
        'project_role': 'int',
        'provider': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'company': 'company',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_role': 'cloud_role',
        'project_role': 'project_role',
        'provider': 'provider'
    }

    def __init__(self, id=None, email=None, company=None, firstname=None, lastname=None, created_at=None, updated_at=None, cloud_role=None, project_role=None, provider=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._company = None
        self._firstname = None
        self._lastname = None
        self._created_at = None
        self._updated_at = None
        self._cloud_role = None
        self._project_role = None
        self._provider = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if company is not None:
            self.company = company
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if cloud_role is not None:
            self.cloud_role = cloud_role
        if project_role is not None:
            self.project_role = project_role
        if provider is not None:
            self.provider = provider

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this User.  # noqa: E501


        :return: The company of this User.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this User.


        :param company: The company of this User.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def firstname(self):
        """Gets the firstname of this User.  # noqa: E501


        :return: The firstname of this User.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this User.


        :param firstname: The firstname of this User.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this User.  # noqa: E501


        :return: The lastname of this User.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this User.


        :param lastname: The lastname of this User.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501


        :return: The created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.


        :param created_at: The created_at of this User.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501


        :return: The updated_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.


        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def cloud_role(self):
        """Gets the cloud_role of this User.  # noqa: E501


        :return: The cloud_role of this User.  # noqa: E501
        :rtype: int
        """
        return self._cloud_role

    @cloud_role.setter
    def cloud_role(self, cloud_role):
        """Sets the cloud_role of this User.


        :param cloud_role: The cloud_role of this User.  # noqa: E501
        :type: int
        """

        self._cloud_role = cloud_role

    @property
    def project_role(self):
        """Gets the project_role of this User.  # noqa: E501


        :return: The project_role of this User.  # noqa: E501
        :rtype: int
        """
        return self._project_role

    @project_role.setter
    def project_role(self, project_role):
        """Sets the project_role of this User.


        :param project_role: The project_role of this User.  # noqa: E501
        :type: int
        """

        self._project_role = project_role

    @property
    def provider(self):
        """Gets the provider of this User.  # noqa: E501


        :return: The provider of this User.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this User.


        :param provider: The provider of this User.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                provider is not None and len(provider) < 1):
            raise ValueError("Invalid value for `provider`, length must be greater than or equal to `1`")  # noqa: E501

        self._provider = provider

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
