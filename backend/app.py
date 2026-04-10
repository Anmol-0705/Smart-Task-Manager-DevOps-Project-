import os
from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# MongoDB setup
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/')
client = MongoClient(mongo_uri)
db = client.taskdb
tasks_collection = db.tasks

# ---------------- API ROUTES ---------------- #

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {
        "title": data.get("title"),
        "completed": False
    }
    result = tasks_collection.insert_one(task)
    task["id"] = str(result.inserted_id)
    del task["_id"]
    return jsonify(task), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        task_data = {
            "id": str(task["_id"]),
            "title": task.get("title"),
            "completed": task.get("completed", False)
        }
        tasks.append(task_data)
    return jsonify(tasks)


@app.route('/tasks/<id>/complete', methods=['PUT'])
def complete_task(id):
    result = tasks_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"completed": True}}
    )
    if result.matched_count == 0:
        return jsonify({"error": "Task not found"}), 404
        
    task = tasks_collection.find_one({"_id": ObjectId(id)})
    task_data = {
        "id": str(task["_id"]),
        "title": task.get("title"),
        "completed": task.get("completed")
    }
    return jsonify(task_data)

@app.route('/tasks/completed', methods=['DELETE'])
def delete_completed_tasks():
    result = tasks_collection.delete_many({"completed": True})
    return jsonify({"message": f"Deleted {result.deleted_count} tasks"}), 200

# ---------------- UI ROUTE ---------------- #

@app.route('/')
def serve_ui():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)