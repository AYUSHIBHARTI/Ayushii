from flask import Flask, request
app = Flask(__name__)

task_list = []

@app.route('/tasks', methods=['GET'])
def view_tasks():
    return "<br>".join(task_list) if task_list else "No tasks available."

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        task_list.append(task)
        return "Task added!"
    return "No task description provided."

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    try:
        task_list.pop(index)
        return "Task deleted!"
    except IndexError:
        return "Task not found."

if __name__ == '__main__':
    app.run(debug=True)

