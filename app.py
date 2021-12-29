from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from importCSV import planeMetrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seatSelector.db'
db = SQLAlchemy(app)

class airlineModels(db.Model):
    planeID = db.Column(db.Integer, primary_key=True)
    planeAirline = db.Column(db.String(200), nullable=False)
    planeModel = db.Column(db.String(200), nullable=False)
    planeLayoutCSV = db.Column(db.String(200), nullable=False)
    
# noOfRows = planeMetrics[0]
# capacity = planeMetrics[2]
# capacityArray = planeMetrics[3]

cTs = ['A','C','D']
cTs = ['','A','B','C','D','E','F','G','J','K','L']


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        planeOption = request.form['planeChoice']
        Metrics = planeMetrics(planeOption)
        noOfColumns = Metrics[1]
        planeLayout = Metrics[4]
        rowTitles = Metrics[5]
        return render_template('index.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=cTs, rowTitles=rowTitles)
    else:
        return render_template('index.html')

@app.route('/log-in')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)