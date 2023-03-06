import schema
from typing import Optional


def filterExercises(
    exercises: list[schema.Exercise], name: str, iteration: Optional[str] = None
):
    filterFunction = lambda x: name in x.name and iteration in x.iteration
    if iteration is None:
        filterFunction = lambda x: name in x.name
    return list(filter(filterFunction, exercises))


class Item(object):
    def __init__(self, user: schema.User, set: schema.Set, metric: str):
        self.user = user
        self.set = set
        self.metric = metric
        self.sortValue = set[metric] * user.settings().weightMultiplier()
        self.weighSuffix = user.settings().weightSuffix()

    def __lt__(self, other):
        return self.sortValue < other.sortValue

    def __repr__(self):
        return f'{self.user.name}: {self.set[self.metric]} {self.weighSuffix}\n- "{self.set.exercise().displayName()}" {self.set}'


def topUsers(exercises: list[schema.Exercise], metric: str):
    sets = list(map(lambda x: x.sets, exercises))
    sets = [item for sublist in sets for item in sublist]

    maxByUser = {}
    for set in sets:
        user = set.exercise().workout().user()
        if user not in maxByUser:
            maxByUser[user] = set
        elif (set[metric] or 0) > maxByUser[user][metric]:
            maxByUser[user] = set

    maxByUser = list(map(lambda x: Item(x[0], x[1], metric), maxByUser.items()))
    maxByUser.sort(reverse=True)

    return maxByUser
