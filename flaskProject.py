
from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name': u'Raju',
        'contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Rahul',
        'contact': u'9876543222', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': data[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)