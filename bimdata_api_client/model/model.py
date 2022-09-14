"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from bimdata_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from bimdata_api_client.exceptions import ApiAttributeError


def lazy_import():
    from bimdata_api_client.model.document import Document
    from bimdata_api_client.model.user import User
    globals()['Document'] = Document
    globals()['User'] = User


class Model(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('type',): {
            'IFC': "IFC",
            'DWG': "DWG",
            'DXF': "DXF",
            'GLTF': "GLTF",
            'PDF': "PDF",
            'JPEG': "JPEG",
            'PNG': "PNG",
            'OBJ': "OBJ",
            'DAE': "DAE",
            'BFX': "BFX",
            'POINT_CLOUD': "POINT_CLOUD",
            'METABUILDING': "METABUILDING",
        },
        ('source',): {
            'UPLOAD': "UPLOAD",
            'SPLIT': "SPLIT",
            'MERGE': "MERGE",
            'EXPORT': "EXPORT",
            'OPTIMIZED': "OPTIMIZED",
        },
    }

    validations = {
        ('name',): {
            'max_length': 512,
        },
        ('world_position',): {
            'max_items': 3,
        },
        ('version',): {
            'max_length': 256,
        },
        ('north_vector',): {
            'max_items': 2,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'creator': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'document_id': (int, none_type,),  # noqa: E501
            'document': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'structure_file': (str, none_type,),  # noqa: E501
            'systems_file': (str, none_type,),  # noqa: E501
            'map_file': (str, none_type,),  # noqa: E501
            'gltf_file': (str, none_type,),  # noqa: E501
            'bvh_tree_file': (str, none_type,),  # noqa: E501
            'viewer_360_file': (str, none_type,),  # noqa: E501
            'xkt_file': (str, none_type,),  # noqa: E501
            'project_id': (int, none_type,),  # noqa: E501
            'errors': ([str], none_type,),  # noqa: E501
            'warnings': ([str], none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'world_position': ([float], none_type,),  # noqa: E501
            'size_ratio': (float, none_type,),  # noqa: E501
            'archived': (bool,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
            'north_vector': ([[float]], none_type,),  # noqa: E501
            'recommanded_2d_angle': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'status': 'status',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'document_id': 'document_id',  # noqa: E501
        'document': 'document',  # noqa: E501
        'structure_file': 'structure_file',  # noqa: E501
        'systems_file': 'systems_file',  # noqa: E501
        'map_file': 'map_file',  # noqa: E501
        'gltf_file': 'gltf_file',  # noqa: E501
        'bvh_tree_file': 'bvh_tree_file',  # noqa: E501
        'viewer_360_file': 'viewer_360_file',  # noqa: E501
        'xkt_file': 'xkt_file',  # noqa: E501
        'project_id': 'project_id',  # noqa: E501
        'errors': 'errors',  # noqa: E501
        'warnings': 'warnings',  # noqa: E501
        'name': 'name',  # noqa: E501
        'source': 'source',  # noqa: E501
        'world_position': 'world_position',  # noqa: E501
        'size_ratio': 'size_ratio',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'version': 'version',  # noqa: E501
        'north_vector': 'north_vector',  # noqa: E501
        'recommanded_2d_angle': 'recommanded_2d_angle',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'type',  # noqa: E501
        'creator',  # noqa: E501
        'status',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
        'document_id',  # noqa: E501
        'document',  # noqa: E501
        'structure_file',  # noqa: E501
        'systems_file',  # noqa: E501
        'map_file',  # noqa: E501
        'gltf_file',  # noqa: E501
        'bvh_tree_file',  # noqa: E501
        'viewer_360_file',  # noqa: E501
        'xkt_file',  # noqa: E501
        'project_id',  # noqa: E501
        'errors',  # noqa: E501
        'warnings',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, type, creator, status, created_at, updated_at, document_id, document, structure_file, systems_file, map_file, gltf_file, bvh_tree_file, viewer_360_file, xkt_file, project_id, errors, warnings, *args, **kwargs):  # noqa: E501
        """Model - a model defined in OpenAPI

        Args:
            id (int):
            type (str):
            creator (bool, date, datetime, dict, float, int, list, str, none_type):
            status (str):
            created_at (datetime):
            updated_at (datetime):
            document_id (int, none_type):
            document (bool, date, datetime, dict, float, int, list, str, none_type):
            structure_file (str, none_type):
            systems_file (str, none_type):
            map_file (str, none_type):
            gltf_file (str, none_type):
            bvh_tree_file (str, none_type):
            viewer_360_file (str, none_type):
            xkt_file (str, none_type):
            project_id (int, none_type):
            errors ([str], none_type): List of errors that happened during IFC processing
            warnings ([str], none_type): List of warnings that happened during IFC processing

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str, none_type): [optional]  # noqa: E501
            source (str): [optional]  # noqa: E501
            world_position ([float], none_type): [x,y,z] array of the position of the local_placement in world coordinates. [optional]  # noqa: E501
            size_ratio (float, none_type): How many meters a unit represents. [optional]  # noqa: E501
            archived (bool): [optional]  # noqa: E501
            version (str, none_type): This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
            north_vector ([[float]], none_type): This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
            recommanded_2d_angle (float, none_type): This is the angle in clockwise degree to apply on the 2D to optimise the horizontality of objects. This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.type = type
        self.creator = creator
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.document_id = document_id
        self.document = document
        self.structure_file = structure_file
        self.systems_file = systems_file
        self.map_file = map_file
        self.gltf_file = gltf_file
        self.bvh_tree_file = bvh_tree_file
        self.viewer_360_file = viewer_360_file
        self.xkt_file = xkt_file
        self.project_id = project_id
        self.errors = errors
        self.warnings = warnings
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Model - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str, none_type): [optional]  # noqa: E501
            source (str): [optional]  # noqa: E501
            world_position ([float], none_type): [x,y,z] array of the position of the local_placement in world coordinates. [optional]  # noqa: E501
            size_ratio (float, none_type): How many meters a unit represents. [optional]  # noqa: E501
            archived (bool): [optional]  # noqa: E501
            version (str, none_type): This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
            north_vector ([[float]], none_type): This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
            recommanded_2d_angle (float, none_type): This is the angle in clockwise degree to apply on the 2D to optimise the horizontality of objects. This field is only for information. Updating it won't impact the export.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
