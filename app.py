from flask import Flask, render_template, request, redirect
from importCSV import planeMetrics

app = Flask(__name__)

planeMetrics = planeMetrics("emb145")

noOfRows = planeMetrics[0]
noOfColumns = planeMetrics[1]
capacity = planeMetrics[2]
capacityArray = planeMetrics[3]

print(noOfRows)

planeLayout = planeMetrics[4]


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', planeLayout = planeLayout)

@app.route('/log-in')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)