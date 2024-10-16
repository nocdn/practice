import json
from flask import Flask, request

app = Flask(__name__)

with open("./tasks.txt", 'r') as file:
    tasks_array = json.load(file)

def write_to_file(data_to_write):
    with open("./tasks.txt", 'w') as file:
        json.dump(data_to_write, file)


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

@app.route("/write", methods=["POST"])
def write_tasks():
    new_task = request.json.get('task')
    tasks_array.append(new_task)
    write_to_file(tasks_array)
    return {"message": "Task added", "new_task": new_task}, 201

app.run(host="0.0.0.0", port=5001)
