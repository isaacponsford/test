

# columntitleread = "A,B,C,D,E,F,G,J,K,L"
# columnTitles = columntitleread.split(",")
# print(columnTitles)

# aisleLocation = "C,G,8,22,45"
# aisleLocation = aisleLocation.split(",")

from SQLHelper import CSVtoSQL, insertPlaneLayout

CSVtoSQL("BA45", "emb145")

# data = ("BA23", "B", "25", 1, 1)
# insertPlaneLayout(data)