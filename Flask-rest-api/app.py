from flask import Flask, request

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

#@app.get("/store") #http://127.0.0.1:5000/store
@app.route('/store', methods=["GET"]) # .get was not working somehow !!

def get_scores():
    return {"stores":stores}

@app.route('/store', methods = ["POST"])
def create_store():
    request_data = request.get_json() # getting the data which client is posting in postman
    new_store = {"name": request_data["name"], "items":[]} # creating a new store 
    stores.append(new_store)
    return new_store, 201 # 201 is status code

