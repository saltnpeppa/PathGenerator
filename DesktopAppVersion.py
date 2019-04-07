import csv
from pathlib import Path
import math

values = []
coords = []

fileInput = input('Enter a file: ')
filepath = Path(fileInput)

distanceConstant = float(input('Enter a distance constant: '))


with open(f'{filepath}', encoding='utf-8-sig') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        values.append(row)

for i in range(0, len(values)):
    val = values[i]
    val = list(map(float, val))
    coords.append(val)


def distance(a, b):
    return math.sqrt(((b[1] - a[1]) ** 2) + (b[0] - a[0]) ** 2)


def NSect(n, array):
    xCoords = []
    yCoords = []
    i = (array[1][0] - array[0][0]) / n
    j = (array[1][1] - array[0][1]) / n
    for a in range(1, n):
        xCoords.append(array[0][0] + i * a)
        yCoords.append(array[0][1] + j * a)
    return list(map(list, zip(xCoords, yCoords)))


def twoCoordGetter(array):
    twoCoords = []
    for i in range(0, len(array) - 1):
        twoCoords.append([array[i], array[i + 1]])
    return twoCoords


def PrintCoords1(array, n):
    vals = []
    for i in range(0, len(array) - 1):
        for element in NSect(n, twoCoordGetter(coords)[i]):
            vals.append(element)
    return vals


def PrintCoords2(array, n):
    vals = []
    for i in range(0, len(array) - 1):
        for element in NSect(n, twoCoordGetter(array)[i]):
            vals.append(element)
    vals.insert(0, array[0])
    vals.insert(len(vals), array[len(array) - 1])
    return vals


def NGenerator(d):
    n = 2
    while distance(PrintCoords1(coords, n)[(int(len(PrintCoords1(coords, n)) / 2) - 1)],
                   PrintCoords1(coords, n)[int(len(PrintCoords1(coords, n)) / 2)]) >= d:
        n = n + 1
    return n


def CoordsFinal():
    n = NGenerator(distanceConstant)
    a = PrintCoords2(coords, n)
    b = PrintCoords2(a, n)
    return PrintCoords2(b, n)


def FileWriter(array):
    print("Outputted data to Output.csv")
    f = open("Output.csv", "w")
    return f.write(str(array).replace('], [', '\n').replace(', ', ',')[2:-2])


FileWriter(CoordsFinal())
# You can run the funtion on itself as many times as you want in def CoordsFinal()