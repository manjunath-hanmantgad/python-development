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

@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name): # name part of string:name is passed into the parameter
    request_data = request.get_json() # grab the data entered from postman
    # match the store name 
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price":request_data["price"]} # request_data is data which client enters from postman
            store["items"].append(new_item) # appending to store's item
            return new_item , 201
    return {"message":"Store not found"}, 404 # if client enters a store which is not there in our db or list
    
    