from flask import Flask, render_template, request, redirect
from importCSV import planeMetrics

app = Flask(__name__)

planeMetrics = planeMetrics("777")

# noOfRows = planeMetrics[0]
# capacity = planeMetrics[2]
# capacityArray = planeMetrics[3]

cTs = ['A','C','D']
noOfColumns = planeMetrics[1]
planeLayout = planeMetrics[4]


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', planeLayout = planeLayout, noOfColumns = noOfColumns)

@app.route('/log-in')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)