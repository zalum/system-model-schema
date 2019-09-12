import unittest

from sms.schema import datamodel, schemas, nodes, relations


class ModelSchemaTest(unittest.TestCase):

    def test_schemas(self):
        self.assertEquals(len(schemas.values()), 4)
        self.assertEquals(schemas.datamodel.name, "datamodel")

    def test_schema_nodes(self):
        self.assertEquals(len(datamodel.nodes.values()), 3)
        self.assertEquals(datamodel.nodes.table, "table")
        self.assertIsNotNone(datamodel.file)

    def test_node_property(self):
        self.assertEqual(nodes.database_user, "database_user")
        self.assertEqual(nodes.get_node(nodes.database_user).name, "database_user")

    def test_relations(self):
        self.assertEquals(relations.foreign_key, "foreign_key")

    def test_relations_supports(self):
        contains = relations.get_value(relations.contains)
        self.assertTrue(contains.supports(from_type=nodes.container, to_type=nodes.component))
