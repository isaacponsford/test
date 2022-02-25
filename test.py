# columntitleread = "A,B,C,D,E,F,G,J,K,L"
# columnTitles = columntitleread.split(",")
# aisleLocation = "C,G,8,22,45"
# aisleLocation = aisleLocation.split(",")
#CSVtoSQL("BA45", "emb145")

# data = ("BA23", "B", "25", 1, 1)
# insertPlaneLayout(data)

from SQLHelper import CSVtoSQL, insertPlaneLayout, getPlaneInfo
from importCSV import planeMetrics

#x = getPlaneInfo("BA45")
#print(x)

data = ("BA23", "B", "25", 1, 1, 4)
insertPlaneLayout(data)