import os
import json
import tqdm
from schema.UserData import UserData
import _pickle as pickle


def loadJsonUserData(directory: str, max: int = 0) -> dict[str, UserData]:
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


def saveUserData(
    userDataDict: dict[str, UserData], directory: str = "data/cached-data"
):
    os.makedirs(directory, exist_ok=True)
    for name, user in tqdm.tqdm(userDataDict.items()):
        with open(f"{directory}/{name}.pkl", "wb") as f:
            pickle.dump(user, f)


def loadUserData(directory: str = "data/cached-data") -> dict[str, UserData]:
    userDataDict = {}
    for file in tqdm.tqdm(os.listdir(directory)):
        with open(f"{directory}/{file}", "rb") as f:
            userData = pickle.load(f)
            userDataDict[userData.user.name] = userData
    return userDataDict
