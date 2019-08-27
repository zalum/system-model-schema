from sms.loader import get_schemas


class Attribute:
    def get_name(self):
        pass

    def get_value(self):
        pass

    def get_getter_value(self):
        pass


class DynamicAttributesObject:
    def __init__(self, attributes: [Attribute]):
        self._attribute_values = dict()
        self._save_attribute_values(attributes)
        self._update_getters(attributes)

    def _save_attribute_values(self, attributes: [Attribute]):
        for attribute in attributes:
            name = attribute.get_name()
            self._attribute_values[name] = attribute.get_value()

    def _update_getters(self, attributes: [Attribute]):
        for a in attributes:
            attribute_name = a.get_name()
            getter_value = a.get_getter_value()
            self.__dict__.update({attribute_name: getter_value})

    def values(self):
        return self._attribute_values.values()


class Node(Attribute):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_value(self):
        return self

    def get_getter_value(self):
        return self.get_name()


class Schema(Attribute):

    @staticmethod
    def create_schema(name, file, nodes_list):
        nodes = list(map(lambda n: Node(n), nodes_list))
        properties = dict(name=name, file=file, nodes=Nodes(nodes))
        Schema.__update_properties(properties, nodes_list)
        schema_type = type(name, (Schema,), properties)
        __this_module = globals()
        __this_module[name] = schema_type
        return schema_type()

    def get_name(self):
        return self.name

    def get_value(self):
        return self

    def get_getter_value(self):
        return self

    @staticmethod
    def __update_properties(properties, nodes_list):
        for node in nodes_list:
            properties[node] = node


class Nodes(DynamicAttributesObject):
    def __init__(self, nodes_list: [Node] = []):
        super().__init__(nodes_list)

    def get_node(self, key: str):
        return self._attribute_values[key]

    def add(self, nodes_to_append: 'Nodes'):
        nodes_list = nodes_to_append.values()
        self._save_attribute_values(nodes_list)
        self._update_getters(nodes_list)

    def list(self):
        return list(self._attribute_values.values())


class Schemas(DynamicAttributesObject):
    def __init__(self, schemas_list: [Schema]):
        super().__init__(schemas_list)


def __init_schema():
    global schemas
    global nodes
    schemas_list = list(map(lambda s: Schema.create_schema(*s), get_schemas()))
    schemas = Schemas(schemas_list)
    nodes = Nodes()
    for schema_nodes in map(lambda s: s.nodes, schemas_list):
        nodes.add(schema_nodes)


__init_schema()
