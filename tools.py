def isBlank(array):
    blank = True

    for element in array:
        if element != "":
            blank = False
    
    return blank

def cup():
    temp = ['4', '4', '4', '4']
    titles = ['D', 'E', 'F', 'G']
    columnTitles = ['A', 'B', 'C', '', 'D', 'E', 'F', 'G', '', 'J', 'K', 'L']

    out = []

    x = 0 #temp point
    y = 0 #cT point

    while x < len(columnTitles):

        print(x)
        print(len(columnTitles))
        print(y)
        print(len(titles))

        if y > len(titles)-1:
            out.append('')
            x = x + 1
        elif columnTitles[x] == titles[y]:
            out.append(temp[y])
            x = x + 1
            y = y + 1
        else:
            out.append('')
            x = x + 1

    print(out)
