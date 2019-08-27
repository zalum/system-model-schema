class Node:
    def __init__(self, name):
        self.name = name

class Nodes: 
    table = ... # type: str
    column = ... # type: str
    database_user = ... # type: str
    system_node = ... # type: str
    bounded_context = ... # type: str
    software_system = ... # type: str
    container = ... # type: str
    component = ... # type: str
    def get_node(key:str)->Node

class SystemModelSchema:
    nodes = ... #type: Nodes

system_model_schema = ... # type: SystemModelSchema
nodes = ... # type: Nodes
schemas = ...# type: Schemas