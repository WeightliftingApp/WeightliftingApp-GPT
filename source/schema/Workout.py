from schema.Exercise import Exercise


class Workout(object):
    def __init__(
        self,
        name: str,
        uuid: str,
        date: str,
        duration: int,
        dateModified: bool,
        exercises: list,
        supersets: list,
    ):
        self.name = name
        self.uuid = uuid
        self.date = date
        self.duration = duration
        self.dateModified = dateModified
        self.exercises = list(map(lambda x: Exercise(**x), exercises))
        self.supersets = supersets

    def __repr__(self):
        return f"Workout(name={self.name}, uuid={self.uuid}, date={self.date}, dateModified={self.dateModified}, exercises={len(self.exercises)}, supersets={len(self.supersets)})"
