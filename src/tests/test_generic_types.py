import unittest

from sms.generic_types import Node, Relation


class GenericTypesTest(unittest.TestCase):

    def test_type_identity(self):
        table = Node("table")
        self.assertEquals(table, "table")

    def test_type_in_set(self):
        table = Node("table")
        a_set = ("table", "column")
        self.assertTrue(table in a_set)

    def test_type_map(self):
        table = Node("table")
        a_dict = dict()
        a_dict[table] = "table"
        self.assertEquals(a_dict["table"], "table")

    def test_relation(self):
        # given
        component = Node("component")
        container = Node("container")
        product = Node("product")

        relation = Relation("contains")
        relation.add_pair(component, container)
        relation.add_pair(product, component)
        relation.add_pair(product, container)

        # when
        self.assertTrue(relation.supports(component, container))
        self.assertTrue(relation.supports(component, "container"))
        self.assertTrue(relation.supports(product, container))
