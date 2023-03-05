from schema.Workout import Workout
from schema.User import User


class UserData(object):
    def __init__(
        self,
        typeList: dict,
        achievements: list,
        templateList: dict,
        workouts: list,
        settings: dict,
        user: dict,
        version: int,
    ):
        self.typeList = typeList["list"]
        self.achievements = achievements
        self.templateList = templateList
        self.workouts = list(map(lambda x: Workout(**x), workouts))
        self.settings = settings
        self.user = User(**user)
        self.version = version

    def __repr__(self):
        return f"UserData(typeList={len(self.typeList)}, achievements={len(self.achievements)}, templateList={len(self.templateList)}, workouts={len(self.workouts)}, settings={len(self.settings)}, user={len(self.user)}, version={self.version})"
