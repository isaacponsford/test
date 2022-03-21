from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getAverageHappiness, getClassSeats,  getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getLayoutClassArray, getPassengerArray, getPassengerGroupDecending, getPassengersWithRef, getPlaneSeatClasses, groupHappinessFunction, happinessFunction, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity
import sqlite3

# array =[[1,x], [2,x], [3,x], [4,x], [5,x]]
# createPassCSVArray(array)

print(avgHappy)
# print(round(avgHappy,2))