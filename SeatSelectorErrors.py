# Name: Isaac Ponsford
# Student ID: 201458733
# Title: SeatSelectorErrors.py
# Description: Includes all custom python errors which are used it "app.py" for error handling

class BlankNameError(Exception):
    pass

class OverCapacityError(Exception):
    pass

class PassengerExistsError(Exception):
    pass

class ClassBelowZeroError(Exception):
    pass

class ClassAboveNineError(Exception):
    pass