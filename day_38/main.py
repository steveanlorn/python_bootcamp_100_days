import datetime
import requests
import os

GENDER = "male"

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_EP = ""
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")


def update_sheet(exercise: str, duration: str, calories: str):

    now = datetime.datetime.now()
    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%H:%M:%S")

    param = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.capitalize(),
            "duration": duration,
            "calories": calories,
        }
    }

    header = {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + SHEETY_AUTH_TOKEN
    }

    response = requests.post(SHEETY_EP, json=param, headers=header)
    response.raise_for_status()


def get_exercise(query: str, weight: float, height: float, age: int) -> []:
    param = {
        "query": query,
        "gender": GENDER,
        "weight_kg": weight,
        "height_cm": height,
        "age": age,
    }

    header = {
        "x-app-id": NUTRITIONIX_ID,
        "x-app-key": NUTRITIONIX_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(NUTRITIONIX_EP, json=param, headers=header)
    response.raise_for_status()
    response_body = response.json()

    if len(response_body["exercises"]) == 0:
        return None

    exercises = []
    for e in response_body["exercises"]:
        exercises.append({
            "duration_min": e["duration_min"],
            "nf_calories": e["nf_calories"],
            "name": e["name"],
        })

    return exercises


user_age = int(input("Your age: "))
user_weight = float(input("Your weight in kg: "))
user_height = float(input("Your height in cm: "))
user_query = input("What exercise did you do: ")
predicted_exercises = get_exercise(age=user_age, weight=user_weight, height=user_height, query=user_query)

print(f"Detected {len(predicted_exercises)} exercise(s):\n")
for i in range(len(predicted_exercises)):
    ex = predicted_exercises[i]
    print(f"{i+1}: {ex['name'].capitalize()}, duration (minute): {ex['duration_min']}, cal: {ex['nf_calories']}")

print("=================")
if input("Do you want to record it? (yes/no): ").lower() == "yes":
    for ex in predicted_exercises:
        update_sheet(exercise=ex["name"], duration=ex["duration_min"], calories=ex["nf_calories"])

    print("Updated")
