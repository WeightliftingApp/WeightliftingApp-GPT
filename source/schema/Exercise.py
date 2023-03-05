from schema.Set import Set
from typing import Optional


class Exercise(object):
    def __init__(
        self,
        name: str,
        category: str,
        style: str,
        sets: list,
        iteration: Optional[str] = None,
    ):
        self.name = name
        self.iteration = iteration
        self.category = category
        self.style = style
        self.sets = list(map(lambda x: Set(**x), sets))

    def __repr__(self):
        name = self.name if self.iteration is None else f"{self.iteration} {self.name}"
        return f"Exercise(name={name}, category={self.category}, style={self.style}, sets={len(self.sets)})"
