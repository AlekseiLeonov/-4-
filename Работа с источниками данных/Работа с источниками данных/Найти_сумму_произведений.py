import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r") as file:
        data = json.load(file)
    sum_ = sum([item["score"] * item["weight"] for item in data])
    sum_ = round(sum_, 3)
    return sum_


print(task())
