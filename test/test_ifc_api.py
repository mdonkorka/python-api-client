# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.ifc_api import IfcApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestIfcApi(unittest.TestCase):
    """IfcApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.ifc_api.IfcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_delete_ifc_classifications(self):
        """Test case for bulk_delete_ifc_classifications

        Remove all classifications from model's elements  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_properties(self):
        """Test case for bulk_delete_ifc_properties

        Delete many Property of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_property_definitions(self):
        """Test case for bulk_delete_ifc_property_definitions

        Delete many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_units(self):
        """Test case for bulk_delete_ifc_units

        Delete many Units of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_property_set(self):
        """Test case for bulk_delete_property_set

        Delete many PropertySet of a model  # noqa: E501
        """
        pass

    def test_bulk_full_update_elements(self):
        """Test case for bulk_full_update_elements

        Update many elements at once (only changing fields may be defined)  # noqa: E501
        """
        pass

    def test_bulk_full_update_ifc_property(self):
        """Test case for bulk_full_update_ifc_property

        Update some fields of many properties of a model  # noqa: E501
        """
        pass

    def test_bulk_remove_classifications_of_element(self):
        """Test case for bulk_remove_classifications_of_element

        Remove many classifications from an element  # noqa: E501
        """
        pass

    def test_bulk_remove_elements_from_classification(self):
        """Test case for bulk_remove_elements_from_classification

        Remove the classifications from all elements  # noqa: E501
        """
        pass

    def test_bulk_update_elements(self):
        """Test case for bulk_update_elements

        Update many elements at once (all field must be defined)  # noqa: E501
        """
        pass

    def test_bulk_update_ifc_property(self):
        """Test case for bulk_update_ifc_property

        Update all fields of many properties of a model  # noqa: E501
        """
        pass

    def test_cloud_project_ifc_processorhandler_partial_update(self):
        """Test case for cloud_project_ifc_processorhandler_partial_update

        """
        pass

    def test_create_access_token(self):
        """Test case for create_access_token

        Create a token for this model  # noqa: E501
        """
        pass

    def test_create_classification_element_relations(self):
        """Test case for create_classification_element_relations

        Create association between existing classification and existing element  # noqa: E501
        """
        pass

    def test_create_classifications_of_element(self):
        """Test case for create_classifications_of_element

        Create one or many classifications to an element  # noqa: E501
        """
        pass

    def test_create_element(self):
        """Test case for create_element

        Create an element in the model  # noqa: E501
        """
        pass

    def test_create_element_property_set(self):
        """Test case for create_element_property_set

        Create a PropertySets to an element  # noqa: E501
        """
        pass

    def test_create_element_property_set_property(self):
        """Test case for create_element_property_set_property

        Create a property to a PropertySet  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition(self):
        """Test case for create_element_property_set_property_definition

        Create a Definition to a Property  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition_unit(self):
        """Test case for create_element_property_set_property_definition_unit

        Create a Unit to a Definition  # noqa: E501
        """
        pass

    def test_create_ifc_property_definition(self):
        """Test case for create_ifc_property_definition

        Create a PropertyDefinition on the model  # noqa: E501
        """
        pass

    def test_create_ifc_unit(self):
        """Test case for create_ifc_unit

        Create a Unit on a model  # noqa: E501
        """
        pass

    def test_create_property_set(self):
        """Test case for create_property_set

        Create a PropertySet  # noqa: E501
        """
        pass

    def test_create_property_set_element_relations(self):
        """Test case for create_property_set_element_relations

        Create association between PropertySet and element  # noqa: E501
        """
        pass

    def test_create_raw_elements(self):
        """Test case for create_raw_elements

        Create elements in an optimized format  # noqa: E501
        """
        pass

    def test_create_space(self):
        """Test case for create_space

        Create a space in the model  # noqa: E501
        """
        pass

    def test_create_zone(self):
        """Test case for create_zone

        Create a zone in the model  # noqa: E501
        """
        pass

    def test_create_zone_space(self):
        """Test case for create_zone_space

        Create a space in a zone  # noqa: E501
        """
        pass

    def test_delete_access_token(self):
        """Test case for delete_access_token

        Delete a token  # noqa: E501
        """
        pass

    def test_delete_element(self):
        """Test case for delete_element

        Delete a zone of a model  # noqa: E501
        """
        pass

    def test_delete_ifc(self):
        """Test case for delete_ifc

        Delete a model  # noqa: E501
        """
        pass

    def test_delete_ifc_property(self):
        """Test case for delete_ifc_property

        Delete a Property of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_property_definition(self):
        """Test case for delete_ifc_property_definition

        Delete a PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_unit(self):
        """Test case for delete_ifc_unit

        Delete a Unit of a model  # noqa: E501
        """
        pass

    def test_delete_property_set(self):
        """Test case for delete_property_set

        Delete a PropertySet of a model  # noqa: E501
        """
        pass

    def test_delete_space(self):
        """Test case for delete_space

        Delete a space  # noqa: E501
        """
        pass

    def test_delete_zone(self):
        """Test case for delete_zone

        Delete a zone of a model  # noqa: E501
        """
        pass

    def test_delete_zone_space(self):
        """Test case for delete_zone_space

        Delete a space of a zone  # noqa: E501
        """
        pass

    def test_export_ifc(self):
        """Test case for export_ifc

        Export IFC  # noqa: E501
        """
        pass

    def test_full_update_access_token(self):
        """Test case for full_update_access_token

        Update all fields of a token  # noqa: E501
        """
        pass

    def test_full_update_element(self):
        """Test case for full_update_element

        Update all fields of an element  # noqa: E501
        """
        pass

    def test_full_update_ifc(self):
        """Test case for full_update_ifc

        Update all fields of a model  # noqa: E501
        """
        pass

    def test_full_update_ifc_property(self):
        """Test case for full_update_ifc_property

        Update some fields of a Property  # noqa: E501
        """
        pass

    def test_full_update_ifc_property_definition(self):
        """Test case for full_update_ifc_property_definition

        Update all fields of many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_full_update_ifc_unit(self):
        """Test case for full_update_ifc_unit

        Update all fields of a Unit of a model  # noqa: E501
        """
        pass

    def test_full_update_property_set(self):
        """Test case for full_update_property_set

        Update all fields of a PropertySet  # noqa: E501
        """
        pass

    def test_full_update_space(self):
        """Test case for full_update_space

        Update all fields of a space  # noqa: E501
        """
        pass

    def test_full_update_zone(self):
        """Test case for full_update_zone

        Update all fields of a zone  # noqa: E501
        """
        pass

    def test_full_update_zone_space(self):
        """Test case for full_update_zone_space

        Update all fields of a space  # noqa: E501
        """
        pass

    def test_get_access_token(self):
        """Test case for get_access_token

        Retrieve one token created for this model  # noqa: E501
        """
        pass

    def test_get_access_tokens(self):
        """Test case for get_access_tokens

        Retrieve all tokens created for this model  # noqa: E501
        """
        pass

    def test_get_classifications_of_element(self):
        """Test case for get_classifications_of_element

        Retrieve all classifications of an element  # noqa: E501
        """
        pass

    def test_get_element(self):
        """Test case for get_element

        Retrieve an element of a model  # noqa: E501
        """
        pass

    def test_get_element_property_set(self):
        """Test case for get_element_property_set

        Retrieve a PropertySet of an element  # noqa: E501
        """
        pass

    def test_get_element_property_set_properties(self):
        """Test case for get_element_property_set_properties

        Retrieve all Properties of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property(self):
        """Test case for get_element_property_set_property

        Retrieve a Property of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition(self):
        """Test case for get_element_property_set_property_definition

        Retrieve a Definition of a Property  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_unit(self):
        """Test case for get_element_property_set_property_definition_unit

        Retrieve a Unit of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_units(self):
        """Test case for get_element_property_set_property_definition_units

        Retrieve all Units of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definitions(self):
        """Test case for get_element_property_set_property_definitions

        Retrieve all Definitions of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_sets(self):
        """Test case for get_element_property_sets

        Retrieve all PropertySets of an element  # noqa: E501
        """
        pass

    def test_get_elements(self):
        """Test case for get_elements

        Retrieve all elements of a model  # noqa: E501
        """
        pass

    def test_get_elements_from_classification(self):
        """Test case for get_elements_from_classification

        Retrieve all elements with the classification  # noqa: E501
        """
        pass

    def test_get_ifc(self):
        """Test case for get_ifc

        Retrieve one model  # noqa: E501
        """
        pass

    def test_get_ifc_bvh(self):
        """Test case for get_ifc_bvh

        Get svg file  # noqa: E501
        """
        pass

    def test_get_ifc_classifications(self):
        """Test case for get_ifc_classifications

        Retrieve all classifications in a model  # noqa: E501
        """
        pass

    def test_get_ifc_gltf(self):
        """Test case for get_ifc_gltf

        Get gltf file  # noqa: E501
        """
        pass

    def test_get_ifc_map(self):
        """Test case for get_ifc_map

        Get bvh file  # noqa: E501
        """
        pass

    def test_get_ifc_properties(self):
        """Test case for get_ifc_properties

        Retrieve all Properties of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property(self):
        """Test case for get_ifc_property

        Retrieve a Property of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property_definition(self):
        """Test case for get_ifc_property_definition

        Retrieve a PropertyDefinition of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property_definitions(self):
        """Test case for get_ifc_property_definitions

        Retrieve all PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_get_ifc_structure(self):
        """Test case for get_ifc_structure

        Get structure file  # noqa: E501
        """
        pass

    def test_get_ifc_systems(self):
        """Test case for get_ifc_systems

        Get systems file  # noqa: E501
        """
        pass

    def test_get_ifc_unit(self):
        """Test case for get_ifc_unit

        Retrieve a Unit of a model  # noqa: E501
        """
        pass

    def test_get_ifc_units(self):
        """Test case for get_ifc_units

        Retrieve all Units of a model  # noqa: E501
        """
        pass

    def test_get_ifcs(self):
        """Test case for get_ifcs

        Retrieve all models  # noqa: E501
        """
        pass

    def test_get_processor_handler(self):
        """Test case for get_processor_handler

        Retrieve a processor handler  # noqa: E501
        """
        pass

    def test_get_processor_handlers(self):
        """Test case for get_processor_handlers

        Get all processor handlers  # noqa: E501
        """
        pass

    def test_get_property_set(self):
        """Test case for get_property_set

        Retrieve a PropertySet of a model  # noqa: E501
        """
        pass

    def test_get_property_sets(self):
        """Test case for get_property_sets

        Retrieve all PropertySets of a model  # noqa: E501
        """
        pass

    def test_get_raw_elements(self):
        """Test case for get_raw_elements

        Retrieve all elements in a optimized format  # noqa: E501
        """
        pass

    def test_get_space(self):
        """Test case for get_space

        Retrieve one space of the model  # noqa: E501
        """
        pass

    def test_get_spaces(self):
        """Test case for get_spaces

        Retrieve all spaces of the model  # noqa: E501
        """
        pass

    def test_get_zone(self):
        """Test case for get_zone

        Retrieve one zone of a model  # noqa: E501
        """
        pass

    def test_get_zone_space(self):
        """Test case for get_zone_space

        Retrieve one space of a zone  # noqa: E501
        """
        pass

    def test_get_zone_spaces(self):
        """Test case for get_zone_spaces

        Retrieve all spaces of a zone  # noqa: E501
        """
        pass

    def test_get_zones(self):
        """Test case for get_zones

        Retrieve zones of a model  # noqa: E501
        """
        pass

    def test_list_classification_element_relations(self):
        """Test case for list_classification_element_relations

        List all associations between classifications and elements  # noqa: E501
        """
        pass

    def test_remove_classification_of_element(self):
        """Test case for remove_classification_of_element

        Remove a classification from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set(self):
        """Test case for remove_element_property_set

        Remove a PropertySet from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property(self):
        """Test case for remove_element_property_set_property

        Remove a property from a PropertySet  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition(self):
        """Test case for remove_element_property_set_property_definition

        Remove a Definition from a Property  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition_unit(self):
        """Test case for remove_element_property_set_property_definition_unit

        Remove a Unit from a Definition  # noqa: E501
        """
        pass

    def test_remove_elements_from_classification(self):
        """Test case for remove_elements_from_classification

        Remove the classification from all elements  # noqa: E501
        """
        pass

    def test_update_access_token(self):
        """Test case for update_access_token

        Update some fields of a token  # noqa: E501
        """
        pass

    def test_update_element(self):
        """Test case for update_element

        Update some fields of a zone  # noqa: E501
        """
        pass

    def test_update_ifc(self):
        """Test case for update_ifc

        Update some fields of a model  # noqa: E501
        """
        pass

    def test_update_ifc_files(self):
        """Test case for update_ifc_files

        Update models file (gltf, svg, structure, etc)  # noqa: E501
        """
        pass

    def test_update_ifc_property(self):
        """Test case for update_ifc_property

        Update some fields of a Property  # noqa: E501
        """
        pass

    def test_update_ifc_property_definition(self):
        """Test case for update_ifc_property_definition

        Update some fields of many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_update_ifc_unit(self):
        """Test case for update_ifc_unit

        Update some fields of a Unit of a model  # noqa: E501
        """
        pass

    def test_update_processor_handler(self):
        """Test case for update_processor_handler

        Update the status of a processor handler  # noqa: E501
        """
        pass

    def test_update_property_set(self):
        """Test case for update_property_set

        Update some fields of a PropertySet  # noqa: E501
        """
        pass

    def test_update_space(self):
        """Test case for update_space

        Update some fields of a space  # noqa: E501
        """
        pass

    def test_update_zone(self):
        """Test case for update_zone

        Update some fields of a zone  # noqa: E501
        """
        pass

    def test_update_zone_space(self):
        """Test case for update_zone_space

        Update some fields of a space  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
