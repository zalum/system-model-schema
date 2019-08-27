from jinja2 import Environment, FileSystemLoader

from sms.schema import system_model_schema

__stub_name = "schema.pyi"


def generate_stubs():
    nodes = system_model_schema.nodes
    stub = __render_stubs(nodes)
    file = open("./sms/" + __stub_name, "w")
    file.write(stub)
    file.close()


def __render_stubs(nodes):
    env = Environment(
        loader=FileSystemLoader("./stubs/templates")
    )
    template = env.get_template(__stub_name + ".j2")
    return template.render(nodes=nodes.list())


if __name__ == "__main__":
    generate_stubs()
