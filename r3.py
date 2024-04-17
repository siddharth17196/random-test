
from dataclasses import dataclass, field


@dataclass
class emp:
    id: int
    name: str
    tens: int = field(repr=False, default=0)
    hundreds: int = field(repr=False, default=0)

    def __eq__(self, value: object) -> bool:
        return self.tens*10+self.hundreds*100 == value.tens*10+value.hundreds*100
    # def __eq__(self, value: object) -> bool:
    #     return self.tens*10+self.hundreds*100 == value.tens*10+value.hundreds*100
    def __lt__(self, value: object) -> bool:
        return self.tens*10+self.hundreds*100 < value.tens*10+value.hundreds*100

e1 = emp(1, "fdasf", 14, 2)
e2 = emp(1, "frew", 24, 1)
e3 = emp(1, "ffsdg", 1, 5)

print(e1 >= e2)