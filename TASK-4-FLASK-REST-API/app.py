from flask import Flask, request

app = Flask(__name__)

tasks_list = [
    {"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Build REST API"}
]

@app.route("/")
def home():
    return "Flask REST API is running!"

@app.route("/tasks")
def get_tasks():
    return {"tasks": tasks_list}
        

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for task in tasks_list:
        if task["id"] == task_id:
            return task

    return {"error": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks_list:
        if task["id"] == task_id:
            tasks_list.remove(task)
            return {"message": "Task deleted successfully"}

    return {"error": "Task not found"}, 404

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    for task in tasks_list:
        if task["id"] == task_id:
            task["title"] = data["title"]
            return task

    return {"error": "Task not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)