from dataclasses import dataclass, InitVar


@dataclass()
class C:
    i: int
    j: int = None
    dt: InitVar[str] = "INCLUIR"

    def __post_init__(self, data):

        if self.i == 0:
            self.dt = "ALTERAR"
        else:
            self.dt = "INCLUIR"


c = C(0,2)
print(c)
print(c.dt)
