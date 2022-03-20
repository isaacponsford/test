from flask import Flask, redirect, render_template, request, url_for, g
import os
import sqlite3

from importCSV import getPassengerCSV, planeMetrics, tempValid
from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getFlightPassengerRef, getPassengerArray, getPlaneInfo, getDistinctFlights, getDistinctPlanes, getPlaneSeatClasses, happinessFunction, insertLinkTable, getFlightAirlineModel, insertModelTable, insertPassengerTable, passengerExists, planeCSVtoSQL, unassignedPlanes, getDistinctPassengersRef, insertPassengerLinkTable, getPassengerClassArray, getClassArray, getPassengerCount
from SeatSelectorErrors import BlankNameError, ClassAboveNineError, ClassBelowZeroError, OverCapacityError, PassengerExistsError
from tools import getFullActualArray, getPlaneActual, totalCapacity, getFullClassArray

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
   
    return render_template('home.html')

@app.route('/flights')
def flightsPage():
    flights = getDistinctFlights()


    return render_template("layoutselect.html", flights = flights)

@app.route('/plane-view/<id>')
def planeViewPage(id):

    airlineModel = getFlightAirlineModel(id)

    noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(id)
    keyClassArray = getPlaneSeatClasses(id)
    seatCapacity = totalCapacity(getClassArray(id))
    info = "Number of Seats: " + str(seatCapacity)

    try:
        passRef = getFlightPassengerRef(id)
        passAmount = totalCapacity(getPassengerClassArray(passRef))

        title = str(id) + " Layout (" + passRef + ")"
        info=info + " - Passengers: " + str(passAmount) + " - Percentage Occupancy: " + str(round((passAmount / seatCapacity) * 100)) + "%"
    except:
        title = str(id) + " Layout"
    
    return render_template('sql.html', id=id,title = title, info = info, planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles,keyClassArray=keyClassArray)

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
            
            planeCSVtoSQL(flightNo, planeOption)
            insertLinkTable((flightNo, planeOption))

            msg = "Data has been successfully inserted"
        except sqlite3.IntegrityError:
            msg = "Flight Number already exists, go to flight select to see flight"
        except Exception as e:
            msg = "Data has not been successfully inserted. Try again"
            print(e)

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
            tempMin, tempMax = tempValid(fn.split(".")[0])

            if tempMin < 0:
                raise ClassBelowZeroError
            elif tempMax > 9:
                raise ClassAboveNineError
            else:
                insertModelTable(planeName, fn.split(".")[0])
                msg = "Data inputed successfully"

        except FileNotFoundError:
            msg = "Please select a CSV file"
        except BlankNameError:
            msg = "Please dont leave the plane name empty"
        except sqlite3.IntegrityError:
            msg = "Plane name already exists. Go to 'new plane' on \n admin page to create a new instance of this plane"
        except ClassBelowZeroError:
            msg = "Current CSV includes classes which are less than 0. \nThis application only accepts classes from 1 to 9"
            os.remove(os.path.join("plane_layouts", fn))
        except ClassAboveNineError:
            msg = "Current CSV includes classes which are greater than 9. \nThis application only accepts classes from 1 to 9"
            os.remove(os.path.join("plane_layouts", fn))
        except:
            msg = "Data not inputed successfully. Please try again"

        return render_template('newcsv.html', msg = msg)
    else:
        return render_template('newcsv.html', msg = "")

@app.route('/new-passengers', methods=['POST', 'GET'])
def newPassengerPage():

    if request.method == 'POST':
        
        msg = ""

        try:
            
            csv = request.files['csvfile']
            
            fn = csv.filename.replace(" ", "").lower()
            passRef = fn.split('.')[0]

            if passengerExists(passRef) == True:
                raise PassengerExistsError

            csv.save(os.path.join("passengerCSV", fn))

            passengers = (getPassengerCSV(passRef))
            
            for x in passengers:
                insertPassengerTable(x)

            msg = "Data inputed successfully"

        except FileNotFoundError:
            msg = "Please select a CSV file"
        except PassengerExistsError:
            msg = "Passengers already exists"
        except:
            msg = "Data not inputed successfully. Please try again"

        return render_template('newpassengers.html', msg = msg)
    else:
        return render_template('newpassengers.html', msg = "")

global plnOption
plnOption = ""
global psgrOption
psgrOption = ""

@app.route('/passenger-assign', methods=['POST', 'GET'])
def passengerAssignPage():

    if request.method == 'POST':

        msg = ""
        classArray = []
        actualArray = []

        if request.form["btn"]=="View":

            try:
                global plnOption
                global psgrOption

                planeOption = request.form['planeChoice']
                passengerOption = request.form['passengerChoice']

                plnOption = planeOption
                psgrOption = passengerOption

                if (totalCapacity(getClassArray(planeOption))) < (getPassengerCount(passengerOption)):
                    raise OverCapacityError
                
                classArray = getFullClassArray(getClassArray(planeOption), getPassengerClassArray(passengerOption))
                
                msg = "Data Shown"

            except OverCapacityError:
                msg = "Too many passengers to fit in that plane, please choose new passenger set or plane"

        elif request.form["btn"]=="Input":

            try:
                
                #Get the plane and passenger options, given by the user at view stage (see above)
                planeOption = plnOption
                passengerOption = psgrOption

                #Get all passengers and all seats from SQL in a array of tuples in class groups, 
                # where first element in class number and second is number of passengers or seats in that class

                seats = getClassArray(planeOption)
                passengers = getPassengerClassArray(passengerOption)

                #Creates a multidimension array for display purposes of class number, passengers, seats and capacity for displau purposes
                classArray = getFullClassArray(seats, passengers)

                #Inputs seats and passengers and returns the "actual" array, where all passengers should actually sit at the end (e.g. upgrade where over capacity, etc.)
                actual, upDowns = getPlaneActual(seats, passengers)

                #Creates a new array, much like "FullClassArray", for display purposes only, with now actual and upgrade and downgrades
                actualArray = getFullActualArray(seats, passengers, actual, upDowns)

                #Inserts passenger flight reference number into SQL link table to relate passenger list to flight number
                insertPassengerLinkTable(planeOption, passengerOption)

                #Itterate through "actual" list in reverse order (from lowest class to first class)
                for x in reversed(actual):
                    getAssignedClassTicket(x[0], actual, planeOption)
                
                happinessFunction(passengerOption)
                
                msg = "Data Successfully Inserted"

            except Exception as e: 

                print(e)
                msg = "Data was not successfully inserted. Try again"

        elif request.form["btn"]=="Display":

            planeOption = plnOption
            return redirect(url_for('planeViewPage', id=planeOption))
            
        planes = unassignedPlanes()
        passengers = getDistinctPassengersRef()
        return render_template('passengerassign.html', planes = planes, passengers = passengers, msg = msg, classArray=classArray, actualArray = actualArray, planeOption = plnOption, passengerOption = psgrOption)
    else:
        planes = unassignedPlanes()
        passengers = getDistinctPassengersRef()
        planeOption = ""
        passengerOption = ""
        return render_template('passengerassign.html', planes = planes, passengers = passengers, msg = "", classArray = [], actualArray=[], planeOption = planeOption, passengerOption = passengerOption)

@app.route('/passenger-remove', methods=['POST', 'GET'])
def passengerRemovePage():

    if request.method == 'POST':
        msg = ""

        try:
            planeOption = request.form['planeChoice']
            clearPassengersFlightNumber(planeOption)
            msg = "Plane successfully cleared"
        except Exception as e:
            msg = "Plane NOT successfully cleared"
            print(e)
        planes = getDistinctFlights()
        return render_template('passengerremove.html', planes = planes, msg = msg)
    else:
        planes = getDistinctFlights()
        return render_template('passengerremove.html', planes = planes, msg = "")

@app.route('/db-clear', methods=['POST', 'GET'])
def databaseClearPage():

    if request.method == 'POST':
        msg= ""

        try:
            clearAll()
            msg = "Database sucessfully cleared"
        except:
            msg = "Error"
        return render_template('cleardb.html', msg = msg)
    else:
        return render_template('cleardb.html', msg = "")

@app.route('/passenger-table/<id>')
def passengerTablePage(id):

    passengerArray = []
    seatCapacity = totalCapacity(getClassArray(id))
    info = "Number of Seats: " + str(seatCapacity)
    
    try:
        passRef = getFlightPassengerRef(id)
        passAmount = totalCapacity(getPassengerClassArray(passRef))

        passengerArray = getPassengerArray(passRef)

        info=info + " - Passengers: " + str(passAmount) + " - Percentage Occupancy: " + str(round((passAmount / seatCapacity) * 100)) + "%"
    except:
        pass
        # title = str(id) + " Layout"
    
    title = "Passengers for: " + str(id)

    return render_template('passengertable.html', id=id,title = title, info = info, passengerArray = passengerArray)

@app.route('/class-view/<id>')
def classViewPage(id):

    airlineModel = getFlightAirlineModel(id)

    noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(id)
    keyClassArray = getPlaneSeatClasses(id)
    seatCapacity = totalCapacity(getClassArray(id))
    info = "Number of Seats: " + str(seatCapacity)

    try:
        passRef = getFlightPassengerRef(id)
        passAmount = totalCapacity(getPassengerClassArray(passRef))

        title = str(id) + " Layout (" + passRef + ")"
        info=info + " - Passengers: " + str(passAmount) + " - Percentage Occupancy: " + str(round((passAmount / seatCapacity) * 100)) + "%"
    except:
        title = str(id) + " Layout"
    
    return render_template('classview.html', id=id,title = title, info = info, planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles,keyClassArray=keyClassArray)

@app.route('/happiness-view/<id>')
def happinesssViewPage(id):

    airlineModel = getFlightAirlineModel(id)

    noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)
    planeLayout = getPlaneInfo(id)

    keyClassArray = getPlaneSeatClasses(id)
    seatCapacity = totalCapacity(getClassArray(id))
    
    info = "Number of Seats: " + str(seatCapacity)

    try:
        passRef = getFlightPassengerRef(id)
        passAmount = totalCapacity(getPassengerClassArray(passRef))

        title = title = " Happiness View for " + str(id) +"(" + passRef + ")"
        info=info + " - Passengers: " + str(passAmount) + " - Percentage Occupancy: " + str(round((passAmount / seatCapacity) * 100)) + "%"
    except:
        title = " Happiness View for " + str(id)
    
    return render_template('happinessview.html', id=id,title = title, info = info, planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles,keyClassArray=keyClassArray)

if __name__ == "__main__":
    app.run(debug=True)