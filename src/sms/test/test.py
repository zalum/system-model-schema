from sms.test.test_types import A, B
import sms.test.test_types as test_types

x = A("x")
y = B("y")
b = getattr(test_types, "B")
z = b("z")

print(x.name)
print(y.name)
print(z.name)
