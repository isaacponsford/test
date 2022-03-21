from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getAverageHappiness, getClassSeats,  getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getLayoutClassArray, getPassengerArray, getPassengerGroupDecending, getPassengersWithRef, getPlaneSeatClasses, groupHappinessFunction, happinessFunction, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity
import sqlite3

print()