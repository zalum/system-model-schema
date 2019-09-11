from sms.generic_types import Nodes, Schema, Node, SchemaElement



class base_nodes(Nodes):
    system_node = "system_node"  # type: str


base_nodes.set_values({ 
    "system_node": Node("system_node"),
})


class base(Schema):
    name = "base"
    file = "base-model.yaml"
    nodes = base_nodes



class bounded_context_nodes(Nodes):
    bounded_context = "bounded_context"  # type: str


bounded_context_nodes.set_values({ 
    "bounded_context": Node("bounded_context"),
})


class bounded_context(Schema):
    name = "bounded_context"
    file = "bounded-context.yaml"
    nodes = bounded_context_nodes



class c4_nodes(Nodes):
    software_system = "software_system"  # type: str
    container = "container"  # type: str
    component = "component"  # type: str


c4_nodes.set_values({ 
    "software_system": Node("software_system"),
    "container": Node("container"),
    "component": Node("component"),
})


class c4(Schema):
    name = "c4"
    file = "c4-model.yaml"
    nodes = c4_nodes



class datamodel_nodes(Nodes):
    table = "table"  # type: str
    column = "column"  # type: str
    database_user = "database_user"  # type: str


datamodel_nodes.set_values({ 
    "table": Node("table"),
    "column": Node("column"),
    "database_user": Node("database_user"),
})


class datamodel(Schema):
    name = "datamodel"
    file = "relational-datamodel.yaml"
    nodes = datamodel_nodes


class schemas(SchemaElement):
    base = base
    bounded_context = bounded_context
    c4 = c4
    datamodel = datamodel


schemas.set_values({  
    "base": base, 
    "bounded_context": bounded_context, 
    "c4": c4, 
    "datamodel": datamodel,
})


class nodes(Nodes): 
    system_node = "system_node"  # type: str     
    bounded_context = "bounded_context"  # type: str     
    software_system = "software_system"  # type: str    
    container = "container"  # type: str    
    component = "component"  # type: str     
    table = "table"  # type: str    
    column = "column"  # type: str    
    database_user = "database_user"  # type: str    


nodes.set_values({   
    "system_node": Node("system_node"),  
    "bounded_context": Node("bounded_context"),  
    "software_system": Node("software_system"),
    "container": Node("container"),
    "component": Node("component"),  
    "table": Node("table"),
    "column": Node("column"),
    "database_user": Node("database_user"),
})