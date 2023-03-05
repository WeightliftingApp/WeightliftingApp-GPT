from typing import Optional


class User(object):
    def __init__(
        self,
        dateCreated: str,
        totalWorkouts: int,
        totalExercises: int,
        totalSets: int,
        totalVolume: int,
        totalDuration: int,
        currentStreak: int,
        longestStreak: int,
        xp: int,
        achievementListVersion: int,
        name: Optional[str] = None,
        weight: Optional[float] = None,
        imageData: Optional[str] = None,
    ):
        self.dateCreated = dateCreated
        self.name = name
        self.weight = weight
        self.totalWorkouts = totalWorkouts
        self.totalExercises = totalExercises
        self.totalSets = totalSets
        self.totalVolume = totalVolume
        self.totalDuration = totalDuration
        self.currentStreak = currentStreak
        self.longestStreak = longestStreak
        self.xp = xp
        self.achievementListVersion = achievementListVersion
        self.imageData = imageData

    def __repr__(self):
        return f"User(name={self.name}, workouts={self.totalWorkouts}, xp={self.xp})"
