from pprint import pprint
from dataclasses import dataclass, field, asdict
import inspect

@dataclass(frozen=True, order=True)
class Circle:
    x: int = field(compare=False)
    y: int = field(compare=False)
    r: int


c1 = Circle(1, 1, 1)
c2 = Circle(-1, 2, 0.5)
pprint(asdict(c1))
print(c1 > c2)
# pprint(inspect.getmembers(Circle, inspect.isfunction))