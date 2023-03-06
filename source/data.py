import os
import json
import tqdm
from schema.UserData import UserData
import _pickle as pickle

UserDataByName = dict[str, UserData]

defaultJsonDataDirectory = "data/user-data-backups/v13"
defaultCachedDataDirectory = "data/cached-data"


def loadJsonUserData(
    directory: str = defaultJsonDataDirectory, max: int = 0
) -> UserDataByName:
    userDataDict = {}
    for file in tqdm.tqdm(os.listdir(directory)):
        max -= 1
        with open(f"{directory}/{file}") as f:
            jsonData = json.load(f)
            userData = UserData(**jsonData)
            userDataDict[userData.user.name] = userData
        if max == 0:
            break
    return userDataDict


def saveUserData(userData: UserDataByName, directory: str = defaultCachedDataDirectory):
    os.makedirs(directory, exist_ok=True)
    for name, user in tqdm.tqdm(userData.items()):
        with open(f"{directory}/{name}.pkl", "wb") as f:
            pickle.dump(user, f)


def loadUserData(directory: str = defaultCachedDataDirectory) -> UserDataByName:
    userData = {}
    for file in tqdm.tqdm(os.listdir(directory)):
        with open(f"{directory}/{file}", "rb") as f:
            data = pickle.load(f)
            userData[data.user.name] = data
    return userData
