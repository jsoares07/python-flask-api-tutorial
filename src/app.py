from flask import Flask, jsonify, request
import json
app = Flask(__name__)

global todos

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET', 'POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    return jsonify(todos)

#It's going to remove one todo based on a given position at the end of the url, and return the updated list of todos.
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)