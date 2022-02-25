from flask import Flask, render_template, request, redirect

from importCSV import planeMetrics
from SQLHelper import getPlaneInfo

app = Flask(__name__)

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

@app.route('/sql', methods=['POST', 'GET'])
def sqlPage():
    
    Metrics = planeMetrics("emb145")
    noOfColumns = Metrics[1]
    planeLayout = getPlaneInfo("BA45")
    rowTitles = Metrics[5]
    columnTitles = Metrics[6]

    return render_template('sql.html', planeLayout = planeLayout, noOfColumns = noOfColumns, cTs=columnTitles, rowTitles=rowTitles)

if __name__ == "__main__":
    app.run(debug=True)