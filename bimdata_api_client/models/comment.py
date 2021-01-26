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


class Comment(object):
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
        'guid': 'str',
        'date': 'datetime',
        'author': 'str',
        'comment': 'str',
        'viewpoint_guid': 'str',
        'reply_to_comment_guid': 'str',
        'topic_guid': 'str',
        'modified_author': 'str',
        'modified_date': 'datetime',
        'viewpoint_temp_id': 'int'
    }

    attribute_map = {
        'guid': 'guid',
        'date': 'date',
        'author': 'author',
        'comment': 'comment',
        'viewpoint_guid': 'viewpoint_guid',
        'reply_to_comment_guid': 'reply_to_comment_guid',
        'topic_guid': 'topic_guid',
        'modified_author': 'modified_author',
        'modified_date': 'modified_date',
        'viewpoint_temp_id': 'viewpoint_temp_id'
    }

    def __init__(self, guid=None, date=None, author=None, comment=None, viewpoint_guid=None, reply_to_comment_guid=None, topic_guid=None, modified_author=None, modified_date=None, viewpoint_temp_id=None, local_vars_configuration=None):  # noqa: E501
        """Comment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._guid = None
        self._date = None
        self._author = None
        self._comment = None
        self._viewpoint_guid = None
        self._reply_to_comment_guid = None
        self._topic_guid = None
        self._modified_author = None
        self._modified_date = None
        self._viewpoint_temp_id = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if date is not None:
            self.date = date
        self.author = author
        if comment is not None:
            self.comment = comment
        self.viewpoint_guid = viewpoint_guid
        self.reply_to_comment_guid = reply_to_comment_guid
        if topic_guid is not None:
            self.topic_guid = topic_guid
        self.modified_author = modified_author
        if modified_date is not None:
            self.modified_date = modified_date
        if viewpoint_temp_id is not None:
            self.viewpoint_temp_id = viewpoint_temp_id

    @property
    def guid(self):
        """Gets the guid of this Comment.  # noqa: E501


        :return: The guid of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Comment.


        :param guid: The guid of this Comment.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def date(self):
        """Gets the date of this Comment.  # noqa: E501


        :return: The date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Comment.


        :param date: The date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def author(self):
        """Gets the author of this Comment.  # noqa: E501


        :return: The author of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Comment.


        :param author: The author of this Comment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                author is not None and len(author) > 254):
            raise ValueError("Invalid value for `author`, length must be less than or equal to `254`")  # noqa: E501

        self._author = author

    @property
    def comment(self):
        """Gets the comment of this Comment.  # noqa: E501


        :return: The comment of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Comment.


        :param comment: The comment of this Comment.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def viewpoint_guid(self):
        """Gets the viewpoint_guid of this Comment.  # noqa: E501


        :return: The viewpoint_guid of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._viewpoint_guid

    @viewpoint_guid.setter
    def viewpoint_guid(self, viewpoint_guid):
        """Sets the viewpoint_guid of this Comment.


        :param viewpoint_guid: The viewpoint_guid of this Comment.  # noqa: E501
        :type: str
        """

        self._viewpoint_guid = viewpoint_guid

    @property
    def reply_to_comment_guid(self):
        """Gets the reply_to_comment_guid of this Comment.  # noqa: E501


        :return: The reply_to_comment_guid of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_comment_guid

    @reply_to_comment_guid.setter
    def reply_to_comment_guid(self, reply_to_comment_guid):
        """Sets the reply_to_comment_guid of this Comment.


        :param reply_to_comment_guid: The reply_to_comment_guid of this Comment.  # noqa: E501
        :type: str
        """

        self._reply_to_comment_guid = reply_to_comment_guid

    @property
    def topic_guid(self):
        """Gets the topic_guid of this Comment.  # noqa: E501


        :return: The topic_guid of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._topic_guid

    @topic_guid.setter
    def topic_guid(self, topic_guid):
        """Sets the topic_guid of this Comment.


        :param topic_guid: The topic_guid of this Comment.  # noqa: E501
        :type: str
        """

        self._topic_guid = topic_guid

    @property
    def modified_author(self):
        """Gets the modified_author of this Comment.  # noqa: E501


        :return: The modified_author of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._modified_author

    @modified_author.setter
    def modified_author(self, modified_author):
        """Sets the modified_author of this Comment.


        :param modified_author: The modified_author of this Comment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                modified_author is not None and len(modified_author) > 254):
            raise ValueError("Invalid value for `modified_author`, length must be less than or equal to `254`")  # noqa: E501

        self._modified_author = modified_author

    @property
    def modified_date(self):
        """Gets the modified_date of this Comment.  # noqa: E501


        :return: The modified_date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this Comment.


        :param modified_date: The modified_date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def viewpoint_temp_id(self):
        """Gets the viewpoint_temp_id of this Comment.  # noqa: E501

        Only used when using POST on the full-topic route to bind viewpoint with comment  # noqa: E501

        :return: The viewpoint_temp_id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._viewpoint_temp_id

    @viewpoint_temp_id.setter
    def viewpoint_temp_id(self, viewpoint_temp_id):
        """Sets the viewpoint_temp_id of this Comment.

        Only used when using POST on the full-topic route to bind viewpoint with comment  # noqa: E501

        :param viewpoint_temp_id: The viewpoint_temp_id of this Comment.  # noqa: E501
        :type: int
        """

        self._viewpoint_temp_id = viewpoint_temp_id

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
        if not isinstance(other, Comment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Comment):
            return True

        return self.to_dict() != other.to_dict()
