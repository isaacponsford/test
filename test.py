from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getClassSeats,  getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getLayoutClassArray, getPassengerArray, getPassengerGroupDecending, getPassengersWithRef, getPlaneSeatClasses, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity

group_tickets = ("1o2",[['C',18,"W"], ['C',19,""],['C',20,"A"],['C',21,'AW'],['C',22,"W"]])
seats = group_tickets[1] # = [[C,18,"W"], [C,19,""],[C,20,"A"]
groupId = group_tickets[0] # = "1o2"

passIDs = [[56,'A'],[57,''],[58,'W'],[59,'W'],[60,'']]

wA = []
aA = []
bA = []
awA = []

wC = 0
aC = 0
bC = 0
awC = 0

for x in range(len(seats)):
    curr = seats[x]
    if curr[2] == 'W':
        wA.append(x)
    elif curr[2] == 'A':
        aA.append(x)
    elif curr[2] == '':
        bA.append(x)
    elif curr[2] == 'AW':
        awA.append(x)


print(wA)
print(aA)
print(bA)
print(awA)

outArray = []

for passID in passIDs:
    if passID[1] == 'W':
        if wC < len(wA):
            outArray.append((passID[0], seats[wA[wC]][0],seats[wA[wC]][1]))
            wC = wC + 1
    
    if passID[1] == 'A':
        if aC < len(aA):
            outArray.append((passID[0], seats[aA[aC]][0],seats[aA[aC]][1]))
            aC = aC + 1

    if passID[1] == '':
        if bC < len(bA):
            outArray.append((passID[0], seats[bA[bC]][0],seats[bA[bC]][1]))
            bC = bC + 1
        
    # if passID[1] == 'aw':
    #     if awC < len(awA):
    #         outArray.append((passID[0], awA[awC][0],awA[awC][1]))
    #         awC = awC + 1
        
print(outArray)