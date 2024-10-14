import json
from flask import Flask

app = Flask(__name__)

with open("./tasks.txt", 'r') as file:
    tasks_array = json.load(file)


@app.route("/read/<index>")
def return_tasks(index):
    try:
        index = int(index)
        if 0 <= index < len(tasks_array):
            return tasks_array[index]
        else:
            return "Index out of range", 400
    except ValueError:
        return "Invalid index", 400

@app.route("/write/<index>", methods=["POST"])
def write_tasks(index):

app.run(host="0.0.0.0", port=5001)
