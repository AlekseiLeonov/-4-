import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:
        reader = csv.DictReader(input_file)
        data = []
        for row in reader:
            data.append(row)

    json_data = json.dumps(data, indent=4)
    print(json_data, end='')


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
