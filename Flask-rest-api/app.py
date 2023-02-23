from flask import Flask

app = Flask(__name__)

# where we will store our data 

# currently in a python list then later on a database 

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 200
            }
        ]
    }
]

# information want to retrieve is using GET

@app.get("/store") #http://127.0.0.1:5000/store

def get_scores():
    return {"stores":stores}