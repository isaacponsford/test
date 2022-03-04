def isBlank(array):
    blank = True

    for element in array:
        if element != "":
            blank = False
    
    return blank

def cleanFileName(filename):
    filename = filename.replace(" ", "").upper()
    return(filename)