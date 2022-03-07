from flask import Flask, render_template, request
import os
import sqlite3

from importCSV import planeMetrics
from SQLHelper import getPlaneInfo, getDistinctFlights, getDistinctPlanes, CSVtoSQL, insertLinkTable, getFlightAirlineModel, insertModelTable, unassignedPlanes, getDistinctPassengersRef, insertPassengerLinkTable
from SeatSelectorErrors import BlankNameError

app = Flask(__name__)

# @app.route('/plane-layouts', methods=['POST', 'GET'])
# def planeLayoutPage():

#     if request.method == 'POST':
#         planeOption = request.form['planeChoice']
        
#         noOfRows, noOfColumns, capacity, capacityArray, planeLayout, rowTitles,columnTitles = planeMetrics(planeOption)

#         return render_template('index.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)
#     else:
#         return render_template('index.html')
#@app.route('/sql', methods=['POST', 'GET'])
# def sqlPage():
    
#     flightNo = "GH777"
#     airlineModel = getFlightAirlineModel(flightNo)

#     noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)
#     planeLayout = getPlaneInfo(flightNo)

#     return render_template('sql.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)

@app.route('/', methods=['POST', 'GET'])
def index():
   
    return render_template('blank.html')

@app.route('/flights')
def flightsPage():
    flights = getDistinctFlights()
    return render_template("layoutselect.html", flights = flights)

@app.route('/plane-view/<id>')
def landing_page(id):

    airlineModel = getFlightAirlineModel(id)

    noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(id)

    return render_template('sql.html', fNo = id , planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)

@app.route('/admin', methods=['POST', 'GET'])
def adminPage():

    return render_template('admin.html')

@app.route('/new-plane', methods=['POST', 'GET'])
def newPlanePage():

    if request.method == 'POST':
        msg = ""

        try:
            planeOption = request.form['planeLayouts']
            flightNo = request.form['flightNumber']
            
            CSVtoSQL(flightNo, planeOption)
            insertLinkTable((flightNo, planeOption))
            msg = "Data has been successfully inserted"
        except sqlite3.IntegrityError:
            msg = "Flight Number already exists, go to flight select to see flight"
        except:
            msg = "Data has not been successfully inserted. Try again"

        layouts = getDistinctPlanes()
        return render_template('newplane.html', layouts = layouts, msg = msg)
    else:
        layouts = getDistinctPlanes()
        return render_template('newplane.html', layouts = layouts, msg = "")

@app.route('/new-csv', methods=['POST', 'GET'])
def newCSVPage():

    if request.method == 'POST':
        
        msg = ""

        try:
            planeName = request.form['planeName']
            csv = request.files['csvfile']

            if planeName == "":
                raise BlankNameError
            
            fn = csv.filename.replace(" ", "").lower()
            csv.save(os.path.join("plane_layouts", fn))

            insertModelTable(planeName, fn.split(".")[0])
            msg = "Data inputed successfully"
        except FileNotFoundError:
            msg = "Please select a CSV file"
        except BlankNameError:
            msg = "Please dont leave the plane name empty"
        except sqlite3.IntegrityError:
            msg = "Plane name already exists. Go to 'new plane' on \n admin page to create a new instance of this plane"
        except Exception as e:
            msg = "Data not inputed successfully. Please try again"
            print(e)

        return render_template('newcsv.html', msg = msg)
    else:
        return render_template('newcsv.html', msg = "")

@app.route('/passenger-assign', methods=['POST', 'GET'])
def passengerAssignPage():

    if request.method == 'POST':

        msg = ""
       
        try:

            planeOption = request.form['planeChoice']
            passengerOption = request.form['passengerChoice']

            insertPassengerLinkTable(planeOption, passengerOption)
            
            msg = "Data Successfully Inserted"
        except:
            msg = "Data was not successfully inserted. Try again"
            
        planes = unassignedPlanes()
        passengers = getDistinctPassengersRef()
        return render_template('passengerassign.html', planes = planes, passengers = passengers, msg = msg)
    else:
        planes = unassignedPlanes()
        passengers = getDistinctPassengersRef()
        return render_template('passengerassign.html', planes = planes, passengers = passengers, msg = "")

if __name__ == "__main__":
    app.run(debug=True)