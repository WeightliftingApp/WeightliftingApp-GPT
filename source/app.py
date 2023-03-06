import data
from pprint import pprint
import schema
from typing import Optional

userData = data.loadJsonUserData(max=0)
# data.saveUserData(userData)
# userData = data.loadUserData()

workouts = list(map(lambda x: x.workouts, userData.values()))
workouts = [item for sublist in workouts for item in sublist]

exercises = list(map(lambda x: x.exercises, workouts))
exercises = [item for sublist in exercises for item in sublist]


def filterExercises(
    exercises: list[schema.Exercise], name: str, iteration: Optional[str] = None
):
    filterFunction = lambda x: name in x.name and iteration in x.iteration
    if iteration is None:
        filterFunction = lambda x: name in x.name
    return list(filter(filterFunction, exercises))


exerciseIteration = None
exerciseName = "Bench Press"
displayName = (
    f"{exerciseIteration} {exerciseName}" if exerciseIteration else exerciseName
)

filteredExercises = filterExercises(exercises, exerciseName, exerciseIteration)
filteredSets = list(map(lambda x: x.sets, filteredExercises))
filteredSets = [item for sublist in filteredSets for item in sublist]

maxByUser = {}
for set in filteredSets:
    user = set.exercise().workout().user()
    if user not in maxByUser:
        maxByUser[user] = set
    elif (set.oneRM or 0) > maxByUser[user].oneRM:
        maxByUser[user] = set

maxByUser = sorted(maxByUser.items(), key=lambda item: item[1].oneRM, reverse=True)


def printEntry(index, entry):
    user, set = entry
    print(
        f'#{index + 1}\t{user.name} ({set.oneRM} lbs, top {index / len(maxByUser) * 100:.1f}%, "{set.exercise().displayName()}")'
    )


print(f"{len(maxByUser)} users have performed {displayName}")
print("------------------")

usersToPrint = [
    "Chappy",
    "Tchantheman",
    "Billy Asel",
    "Billy A",
    "Billy",
    "Bobby Asel",
    "Paul A",
    "Pierce",
    "User 3705032469",
]

for index, entry in enumerate(maxByUser):
    if index < 25:
        printEntry(index, entry)
    elif entry[0].name in usersToPrint:
        printEntry(index, entry)
