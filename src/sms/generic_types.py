class Attribute:
    def get_name(self):
        pass

    def get_value(self):
        pass

    def get_getter_value(self):
        pass


class SchemaElement:

    @classmethod
    def values(cls):
        return list(cls._attribute_values.values())

    @classmethod
    def set_values(cls, values: dict):
        cls._attribute_values = values


class Node:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Schema:
    name = None  # type: str
    file = None  # type: str


class Nodes(SchemaElement):
    @classmethod
    def get_node(cls, key: str):
        return cls._attribute_values[key]


class Schemas(SchemaElement):
    ...
