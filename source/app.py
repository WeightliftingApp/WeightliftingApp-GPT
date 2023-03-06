import data
import leaderboard

maxUsers = 0
name, iteration, metric = "Bench Press", None, "volume"

userData = data.loadJsonUserData(max=maxUsers)
# data.saveUserData(userData)
# userData = data.loadUserData()

workouts = list(map(lambda x: x.workouts, userData.values()))
workouts = [item for sublist in workouts for item in sublist]

exercises = list(map(lambda x: x.exercises, workouts))
exercises = [item for sublist in exercises for item in sublist]

exercises = leaderboard.filterExercises(exercises, name, iteration=iteration)
maxByUser = leaderboard.topUsers(exercises, metric)


def printEntry(index, entry):
    percent = f"(top {index / len(maxByUser) * 100:.1f}%)"
    print(f"#{index + 1}\t{entry} {percent}\n")


displayName = f"{iteration} {name}" if iteration else name
print(f"- {len(maxByUser)} users have performed {displayName}")
print(f"- Ranked by {metric}")
print("------------------\n")

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
    elif entry.user.name in usersToPrint:
        printEntry(index, entry)
