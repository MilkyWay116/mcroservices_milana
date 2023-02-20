from dataclasses import dataclass
from typing import Optional

@dataclass
class Pet:
    name: str
    view: str
    age: int
    illness: str
    cost: int
    created: str = ""
    status: str = "not paid"
    id: Optional[int] = None