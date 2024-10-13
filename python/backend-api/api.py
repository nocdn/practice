from flask import Flask

app = Flask(__name__)

file = open("./tasks.txt")
tasks_array = file.read()
print(tasks_array)

@app.route("/read/<index>")
def return_tasks(index):
    return tasks_array[index]


app.run(host="0.0.0.0", port=5001)
