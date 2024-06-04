# this is flask framework webservice..

# to run it individually run following commands on terminal
# set FLASK_APP=app.py
# set FLASK_ENV = environment
# flask run
# flask app will run in default url that is 127.0.0.1:5000
# u can test your webservices using postmen on url http://127.0.0.1:5000/countries via get and post(json data post) methods


# app.py
import uvicorn
from fastapi import FastAPI
from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

# this method will create new id for new record


def _find_next_id():
    return max(country["id"] for country in countries) + 1


# list all records in the database(global variable currently defined)
@app.get("/countries")
def get_countries():
    return jsonify(countries)


# add a new record to the database(global variable)
@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


# route = FastAPI()


# @route.get("/")
# async def root():
#     return {"message": "Hello, GeeksforGeeks!"}

# if __name__ == "__main__":
#     uvicorn.run(route, host="0.0.0.0", port=8000)
