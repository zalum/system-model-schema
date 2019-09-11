from jinja2 import Environment, FileSystemLoader

from stubs import loader

__module_file = "schema.py"


def generate_stubs():
    properties = dict(schemas=loader.get_schemas())
    stub = __render_stubs(**properties)
    file = open("./sms/" + __module_file, "w")
    file.write(stub)
    file.close()


def __render_stubs(**properties):
    env = Environment(
        loader=FileSystemLoader("./stubs/templates")
    )
    template = env.get_template(__module_file + ".j2")
    return template.render(properties)


if __name__ == "__main__":
    generate_stubs()
