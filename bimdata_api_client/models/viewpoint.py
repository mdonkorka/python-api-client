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


class Viewpoint(object):
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
        'index': 'int',
        'guid': 'str',
        'orthogonal_camera': 'OrthogonalCamera',
        'perspective_camera': 'PerspectiveCamera',
        'lines': 'list[Line]',
        'clipping_planes': 'list[ClippingPlane]',
        'snapshot': 'Snapshot',
        'components': 'ComponentsParent',
        'temp_id': 'int'
    }

    attribute_map = {
        'index': 'index',
        'guid': 'guid',
        'orthogonal_camera': 'orthogonal_camera',
        'perspective_camera': 'perspective_camera',
        'lines': 'lines',
        'clipping_planes': 'clipping_planes',
        'snapshot': 'snapshot',
        'components': 'components',
        'temp_id': 'temp_id'
    }

    def __init__(self, index=None, guid=None, orthogonal_camera=None, perspective_camera=None, lines=None, clipping_planes=None, snapshot=None, components=None, temp_id=None, local_vars_configuration=None):  # noqa: E501
        """Viewpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._guid = None
        self._orthogonal_camera = None
        self._perspective_camera = None
        self._lines = None
        self._clipping_planes = None
        self._snapshot = None
        self._components = None
        self._temp_id = None
        self.discriminator = None

        self.index = index
        if guid is not None:
            self.guid = guid
        self.orthogonal_camera = orthogonal_camera
        self.perspective_camera = perspective_camera
        self.lines = lines
        self.clipping_planes = clipping_planes
        self.snapshot = snapshot
        self.components = components
        self.temp_id = temp_id

    @property
    def index(self):
        """Gets the index of this Viewpoint.  # noqa: E501


        :return: The index of this Viewpoint.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Viewpoint.


        :param index: The index of this Viewpoint.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                index is not None and index > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                index is not None and index < 0):  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._index = index

    @property
    def guid(self):
        """Gets the guid of this Viewpoint.  # noqa: E501


        :return: The guid of this Viewpoint.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Viewpoint.


        :param guid: The guid of this Viewpoint.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def orthogonal_camera(self):
        """Gets the orthogonal_camera of this Viewpoint.  # noqa: E501


        :return: The orthogonal_camera of this Viewpoint.  # noqa: E501
        :rtype: OrthogonalCamera
        """
        return self._orthogonal_camera

    @orthogonal_camera.setter
    def orthogonal_camera(self, orthogonal_camera):
        """Sets the orthogonal_camera of this Viewpoint.


        :param orthogonal_camera: The orthogonal_camera of this Viewpoint.  # noqa: E501
        :type: OrthogonalCamera
        """

        self._orthogonal_camera = orthogonal_camera

    @property
    def perspective_camera(self):
        """Gets the perspective_camera of this Viewpoint.  # noqa: E501


        :return: The perspective_camera of this Viewpoint.  # noqa: E501
        :rtype: PerspectiveCamera
        """
        return self._perspective_camera

    @perspective_camera.setter
    def perspective_camera(self, perspective_camera):
        """Sets the perspective_camera of this Viewpoint.


        :param perspective_camera: The perspective_camera of this Viewpoint.  # noqa: E501
        :type: PerspectiveCamera
        """

        self._perspective_camera = perspective_camera

    @property
    def lines(self):
        """Gets the lines of this Viewpoint.  # noqa: E501


        :return: The lines of this Viewpoint.  # noqa: E501
        :rtype: list[Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this Viewpoint.


        :param lines: The lines of this Viewpoint.  # noqa: E501
        :type: list[Line]
        """

        self._lines = lines

    @property
    def clipping_planes(self):
        """Gets the clipping_planes of this Viewpoint.  # noqa: E501


        :return: The clipping_planes of this Viewpoint.  # noqa: E501
        :rtype: list[ClippingPlane]
        """
        return self._clipping_planes

    @clipping_planes.setter
    def clipping_planes(self, clipping_planes):
        """Sets the clipping_planes of this Viewpoint.


        :param clipping_planes: The clipping_planes of this Viewpoint.  # noqa: E501
        :type: list[ClippingPlane]
        """

        self._clipping_planes = clipping_planes

    @property
    def snapshot(self):
        """Gets the snapshot of this Viewpoint.  # noqa: E501


        :return: The snapshot of this Viewpoint.  # noqa: E501
        :rtype: Snapshot
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this Viewpoint.


        :param snapshot: The snapshot of this Viewpoint.  # noqa: E501
        :type: Snapshot
        """

        self._snapshot = snapshot

    @property
    def components(self):
        """Gets the components of this Viewpoint.  # noqa: E501


        :return: The components of this Viewpoint.  # noqa: E501
        :rtype: ComponentsParent
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Viewpoint.


        :param components: The components of this Viewpoint.  # noqa: E501
        :type: ComponentsParent
        """

        self._components = components

    @property
    def temp_id(self):
        """Gets the temp_id of this Viewpoint.  # noqa: E501

        Only used when using POST on the full-topic route to bind viewpoint with comment  # noqa: E501

        :return: The temp_id of this Viewpoint.  # noqa: E501
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this Viewpoint.

        Only used when using POST on the full-topic route to bind viewpoint with comment  # noqa: E501

        :param temp_id: The temp_id of this Viewpoint.  # noqa: E501
        :type: int
        """

        self._temp_id = temp_id

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
        if not isinstance(other, Viewpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Viewpoint):
            return True

        return self.to_dict() != other.to_dict()
