from flask import Flask, render_template, request, redirect

#from tools import cleanFileName
from importCSV import planeMetrics
from SQLHelper import getPlaneInfo, getDistinctFlights, getDistinctPlanes, CSVtoSQL, insertLinkTable, getFlightAirlineModel, insertModelTable
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':

        csv = request.files['csvfile']
        csv.save(os.path.join("plane_layouts", csv.filename))

        print((csv))
        return render_template('blank.html')
    else:
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

@app.route('/flights')
def flightsPage():
    flights = getDistinctFlights()
    return render_template("layoutselect.html", flights = flights)

@app.route('/sql', methods=['POST', 'GET'])
def sqlPage():
    
    flightNo = "GH777"
    airlineModel = getFlightAirlineModel(flightNo)

    noOfRows, noOfColumns, capacity, capacityArray, planeLayout, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(flightNo)

    return render_template('sql.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)

@app.route('/plane-view/<id>')
def landing_page(id):

    airlineModel = getFlightAirlineModel(id)

    noOfRows, noOfColumns, capacity, capacityArray, planeLayout, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(id)

    return render_template('sql.html', fNo = id , planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)

@app.route('/admin', methods=['POST', 'GET'])
def adminPage():

    if request.method == 'POST':

        planeOption = request.form['browsers']
        flightNo = request.form['a']
        
        CSVtoSQL(flightNo, planeOption)
        insertLinkTable((flightNo, planeOption))
        layouts = getDistinctPlanes()
        return render_template('admin.html', layouts = layouts)
    else:
        layouts = getDistinctPlanes()
        return render_template('admin.html', layouts = layouts)

@app.route('/new-plane', methods=['POST', 'GET'])
def newPlanePage():

    if request.method == 'POST':

        planeOption = request.form['planeLayouts']
        flightNo = request.form['flightNumber']
        
        CSVtoSQL(flightNo, planeOption)
        insertLinkTable((flightNo, planeOption))
        layouts = getDistinctPlanes()
        return render_template('newplane.html', layouts = layouts)
    else:
        layouts = getDistinctPlanes()
        return render_template('newplane.html', layouts = layouts)

@app.route('/new-csv', methods=['POST', 'GET'])
def newCSVPage():

    if request.method == 'POST':
        
        planeName = request.form['planeName']

        csv = request.files['csvfile']

        fn = csv.filename.replace(" ", "").lower()
        csv.save(os.path.join("plane_layouts", fn))

        insertModelTable(planeName, fn.split(".")[0])

        return render_template('newcsv.html')
    else:
        return render_template('newcsv.html')

if __name__ == "__main__":
    app.run(debug=True)