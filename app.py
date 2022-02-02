from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from importCSV import planeMetrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seatSelector.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class airlineModels(db.Model):
    planeID = db.Column(db.Integer, primary_key=True)
    planeAirline = db.Column(db.String(200), nullable=False)
    planeModel = db.Column(db.String(200), nullable=False)
    planeLayoutCSV = db.Column(db.String(200), nullable=False)

class airplaneLayout(db,Model):
    seatID = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(10))
    column = db.Column(db.String(10))
    occupied = db.Column(db.Boolean)



@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template('blank.html')

@app.route('/plane-layouts', methods=['POST', 'GET'])
def planeLayoutPage():

    if request.method == 'POST':
        planeOption = request.form['planeChoice']
        
        Metrics = planeMetrics(planeOption)
        noOfColumns = Metrics[1]
        planeLayout = Metrics[4]
        rowTitles = Metrics[5]
        columnTitles = Metrics[6]

        return render_template('index.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)
    else:
        return render_template('index.html')

@app.route('/admin')
def adminPage():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)