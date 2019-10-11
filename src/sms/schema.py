from sms.generic_types import Nodes, Schema, Node, Relations, SchemaElement



class base_nodes(Nodes):
    system_node = "system_node"  # type: str


base_nodes.set_values({ 
    "system_node": Node("system_node"),
})

class base(Schema):
    name = "base"
    file = "base-model.yaml"
    nodes = base_nodes



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
    file = "datamodel.yaml"
    nodes = datamodel_nodes



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



class relations(Relations):
    relation = "relation"
    operation = "operation"
    contains = "contains"
    contains = "contains"
    foreign_key = "foreign_key"
    composition = "composition"
    reads = "reads"
    writes = "writes"
    deletes = "deletes"
    owns = "owns"
    owns = "owns"
    reads = "reads"
    writes = "writes"
    contains = "contains"
    contains = "contains"
    operation = "operation"
    operation = "operation"
    operation = "operation"
    operation = "operation"


relations.add_relation_pair("relation", "", "") 
relations.add_relation_pair("operation", "", "") 
relations.add_relation_pair("contains", "database_user", "table") 
relations.add_relation_pair("contains", "table", "column") 
relations.add_relation_pair("foreign_key", "column", "column") 
relations.add_relation_pair("composition", "table", "column") 
relations.add_relation_pair("reads", "database_user", "table") 
relations.add_relation_pair("writes", "database_user", "table") 
relations.add_relation_pair("deletes", "database_user", "table") 
relations.add_relation_pair("owns", "bounded_context", "dabatase_user") 
relations.add_relation_pair("owns", "bounded_context", "table") 
relations.add_relation_pair("reads", "bounded_context", "table") 
relations.add_relation_pair("writes", "bounded_context", "table") 
relations.add_relation_pair("contains", "software_system", "container") 
relations.add_relation_pair("contains", "container", "component") 
relations.add_relation_pair("operation", "container", "container") 
relations.add_relation_pair("operation", "software_system", "container") 
relations.add_relation_pair("operation", "software_system", "software_system") 
relations.add_relation_pair("operation", "container", "software_system") 


class schemas(SchemaElement):
    base = base
    datamodel = datamodel
    bounded_context = bounded_context
    c4 = c4


schemas.set_values({  
    "base": base, 
    "datamodel": datamodel, 
    "bounded_context": bounded_context, 
    "c4": c4,
})


class nodes(Nodes): 
    system_node = "system_node"  # type: str     
    table = "table"  # type: str    
    column = "column"  # type: str    
    database_user = "database_user"  # type: str     
    bounded_context = "bounded_context"  # type: str     
    software_system = "software_system"  # type: str    
    container = "container"  # type: str    
    component = "component"  # type: str    


nodes.set_values({   
    "system_node": Node("system_node"),  
    "table": Node("table"),
    "column": Node("column"),
    "database_user": Node("database_user"),  
    "bounded_context": Node("bounded_context"),  
    "software_system": Node("software_system"),
    "container": Node("container"),
    "component": Node("component"),
})