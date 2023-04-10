from flask import Flask, request
from test import getsepal
from flask_cors import CORS, cross_origin


app = Flask("__name__")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
@cross_origin()
def get():
    return "hello"

@app.route("/model", methods=["POST"])
@cross_origin()
def slr():
    s = request.json["x"]
    r = getsepal(s)
    return str(r)


if __name__ == "__main__":
    print("server running")
    app.run(debug=True)
