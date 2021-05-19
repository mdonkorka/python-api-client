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


class SelfUser(object):
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
        'organizations': 'list[Organization]',
        'clouds': 'list[CloudRole]',
        'projects': 'list[ProjectRole]',
        'provider': 'str',
        'provider_sub': 'str',
        'sub': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'company': 'company',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'organizations': 'organizations',
        'clouds': 'clouds',
        'projects': 'projects',
        'provider': 'provider',
        'provider_sub': 'provider_sub',
        'sub': 'sub'
    }

    def __init__(self, id=None, email=None, company=None, firstname=None, lastname=None, created_at=None, updated_at=None, organizations=None, clouds=None, projects=None, provider=None, provider_sub=None, sub=None, local_vars_configuration=None):  # noqa: E501
        """SelfUser - a model defined in OpenAPI"""  # noqa: E501
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
        self._organizations = None
        self._clouds = None
        self._projects = None
        self._provider = None
        self._provider_sub = None
        self._sub = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.email = email
        self.company = company
        self.firstname = firstname
        self.lastname = lastname
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if organizations is not None:
            self.organizations = organizations
        if clouds is not None:
            self.clouds = clouds
        if projects is not None:
            self.projects = projects
        if provider is not None:
            self.provider = provider
        self.provider_sub = provider_sub
        if sub is not None:
            self.sub = sub

    @property
    def id(self):
        """Gets the id of this SelfUser.  # noqa: E501


        :return: The id of this SelfUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SelfUser.


        :param id: The id of this SelfUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this SelfUser.  # noqa: E501


        :return: The email of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SelfUser.


        :param email: The email of this SelfUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this SelfUser.  # noqa: E501


        :return: The company of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SelfUser.


        :param company: The company of this SelfUser.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def firstname(self):
        """Gets the firstname of this SelfUser.  # noqa: E501


        :return: The firstname of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this SelfUser.


        :param firstname: The firstname of this SelfUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and firstname is None:  # noqa: E501
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                firstname is not None and len(firstname) < 1):
            raise ValueError("Invalid value for `firstname`, length must be greater than or equal to `1`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this SelfUser.  # noqa: E501


        :return: The lastname of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this SelfUser.


        :param lastname: The lastname of this SelfUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lastname is None:  # noqa: E501
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lastname is not None and len(lastname) < 1):
            raise ValueError("Invalid value for `lastname`, length must be greater than or equal to `1`")  # noqa: E501

        self._lastname = lastname

    @property
    def created_at(self):
        """Gets the created_at of this SelfUser.  # noqa: E501


        :return: The created_at of this SelfUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SelfUser.


        :param created_at: The created_at of this SelfUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SelfUser.  # noqa: E501


        :return: The updated_at of this SelfUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SelfUser.


        :param updated_at: The updated_at of this SelfUser.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def organizations(self):
        """Gets the organizations of this SelfUser.  # noqa: E501


        :return: The organizations of this SelfUser.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this SelfUser.


        :param organizations: The organizations of this SelfUser.  # noqa: E501
        :type: list[Organization]
        """

        self._organizations = organizations

    @property
    def clouds(self):
        """Gets the clouds of this SelfUser.  # noqa: E501


        :return: The clouds of this SelfUser.  # noqa: E501
        :rtype: list[CloudRole]
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        """Sets the clouds of this SelfUser.


        :param clouds: The clouds of this SelfUser.  # noqa: E501
        :type: list[CloudRole]
        """

        self._clouds = clouds

    @property
    def projects(self):
        """Gets the projects of this SelfUser.  # noqa: E501


        :return: The projects of this SelfUser.  # noqa: E501
        :rtype: list[ProjectRole]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this SelfUser.


        :param projects: The projects of this SelfUser.  # noqa: E501
        :type: list[ProjectRole]
        """

        self._projects = projects

    @property
    def provider(self):
        """Gets the provider of this SelfUser.  # noqa: E501


        :return: The provider of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this SelfUser.


        :param provider: The provider of this SelfUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                provider is not None and len(provider) < 1):
            raise ValueError("Invalid value for `provider`, length must be greater than or equal to `1`")  # noqa: E501

        self._provider = provider

    @property
    def provider_sub(self):
        """Gets the provider_sub of this SelfUser.  # noqa: E501

        sub from original identity provider  # noqa: E501

        :return: The provider_sub of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._provider_sub

    @provider_sub.setter
    def provider_sub(self, provider_sub):
        """Sets the provider_sub of this SelfUser.

        sub from original identity provider  # noqa: E501

        :param provider_sub: The provider_sub of this SelfUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                provider_sub is not None and len(provider_sub) > 255):
            raise ValueError("Invalid value for `provider_sub`, length must be less than or equal to `255`")  # noqa: E501

        self._provider_sub = provider_sub

    @property
    def sub(self):
        """Gets the sub of this SelfUser.  # noqa: E501

        sub from Keycloak  # noqa: E501

        :return: The sub of this SelfUser.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this SelfUser.

        sub from Keycloak  # noqa: E501

        :param sub: The sub of this SelfUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sub is not None and len(sub) < 1):
            raise ValueError("Invalid value for `sub`, length must be greater than or equal to `1`")  # noqa: E501

        self._sub = sub

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
        if not isinstance(other, SelfUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelfUser):
            return True

        return self.to_dict() != other.to_dict()
