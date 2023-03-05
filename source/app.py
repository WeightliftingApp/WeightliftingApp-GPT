import data
from pprint import pprint

userData = data.loadJsonUserData("data/user-data-backups/v13", max=0)
# data.saveUserData(userData)
# userData = data.loadUserData()

workouts = list(map(lambda x: x.workouts, userData.values()))
workouts = [item for sublist in workouts for item in sublist]
exercises = list(map(lambda x: x.exercises, workouts))
exercises = [item for sublist in exercises for item in sublist]
sets = list(map(lambda x: x.sets, exercises))
sets = [item for sublist in sets for item in sublist]

pprint(f"Users: {len(userData)}")
pprint(f"Workouts: {len(workouts)}")
pprint(f"Exercises: {len(exercises)}")
pprint(f"Sets: {len(sets)}")
