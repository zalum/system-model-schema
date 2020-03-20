class SchemaElement:
    _attribute_values = dict()

    @classmethod
    def values(cls):
        return list(cls._attribute_values.values())

    @classmethod
    def set_values(cls, values: dict):
        cls._attribute_values = values

    @classmethod
    def get_value(cls, key):
        if key in cls._attribute_values:
            return cls._attribute_values[key]
        return None

    @classmethod
    def add_value(cls, key, value):
        cls._attribute_values[key] = value


class Node:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class Relation:
    def __init__(self, name: str):
        self.name = name
        self.pairs = dict()

    def add_pair(self, from_type, to_type):
        if from_type not in self.pairs:
            self.pairs[from_type] = set()
        self.pairs[from_type].add(to_type)  # type: set

    def supports(self, from_type, to_type) -> bool:
        if from_type in self.pairs:
            if to_type in self.pairs[from_type]:
                return True
        if to_type in self.pairs:
            return from_type in self.pairs[to_type]
        return False


class Schema:
    name = None  # type: str
    file = None  # type: str
    nodes = None  # type: Nodes
    relations = None  # type: Relations


class Nodes(SchemaElement):
    @classmethod
    def get_node(cls, key: str):
        return cls._attribute_values[key]


class Relations(SchemaElement):
    @classmethod
    def add_relation_pair(cls, name, start_type, end_type):
        relation = cls.get_value(name)
        if relation is None:
            relation = Relation(name=name)
            cls.add_value(name, relation)
        relation.add_pair(start_type, end_type)


class Schemas(SchemaElement):
    ...
