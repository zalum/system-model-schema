import unittest
from sms import nodes
from sms import schemas

'''
# not1
system_model_schema.schemas.datamodel.nodes.table
system_model_schema.schemas.datamodel.relations.contains
system_model_schema.nodes.table
system_model_schema.relations.contains

# yes1
schemas.datamodel.nodes.table
nodes.table
relations.contains

# yes2
from sms.schema import datamodel
datamodel.nodes.table

'''
class ModelSchemaTest(unittest.TestCase):

    def test_names_of_nodes(self):
        self.assertEquals(nodes.system_node, "system_node")

    def test_nodes_of_schema(self):
        self.assertEqual(schemas.datamodel.nodes.table, "table")
        self.assertEqual(schemas.bounded_context.nodes.bounded_context, "bounded_context")

    def test_call_schema(self):
        from sms.schema import datamodel
        self.assertEqual(datamodel.nodes.table, "table")

    def test_node_property(self):
        self.assertEqual(nodes.get_node(nodes.system_node).name, "system_node")



