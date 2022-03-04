from SQLHelper import CSVtoSQL, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes
from importCSV import planeMetrics

#data = ("BA23", "B", "25", 1, 1, 4)
# insertPlaneLayout(data)

# x = getPlaneInfo("BA45")

# CSVtoSQL("BA1", "emb145")
print(getDistinctPlanes())