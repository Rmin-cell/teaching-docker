from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple in-memory todo list
todos = [
    {"id": 1, "task": "Learn Docker", "completed": False},
    {"id": 2, "task": "Build a container", "completed": False}
]

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Welcome to Docker Todo API"})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json.get('task', ''),
        "completed": False
    }
    todos.append(new_todo)
    return jsonify({"todo": new_todo}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)