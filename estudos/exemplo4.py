from dataclasses import dataclass, InitVar


@dataclass
class Test:
    b: int = 6
    id: int = 1

    def __post_init__(self):
        print(f"the value of id is {self.id} in the post_init")
        print(f"is id a property: {isinstance(self.id, property)}")
        self._id = self.id

    @property
    def id(self):
        print("using the getter id")
        return self._id

    @id.setter
    def id(self, to):
        print(f"using the setter to:{to}")
        self._id = to


print("\nInit with position argument")
a = Test()
print("a is", a)
print("a.id is", a.id)

print("\nInit with explicit key")
a4 = Test(id=4)
print("a4.id is", a4.id)