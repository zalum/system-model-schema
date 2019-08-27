class A:
    def __init__(self, name):
        self.name = name


__this_module = globals()
__this_module["B"] = type("B", (A,), dict(bname=1))
