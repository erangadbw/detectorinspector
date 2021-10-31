from bs4 import BeautifulSoup
from stringMatcher import * 
import requests
import matplotlib.pyplot as plt


#takes in a string and checks the string to see if it contains any of the
#the numerical patterns that we want to plot
def determineAndReturnColType(textval):
    stringtype = returnMeterStringPattern(textval)

    if(stringtype != None):
        return stringtype
    stringtype = returnStringPattern(textval,"(^|[ ])\\d+[:.]\\d+([:.]\\d+)?")
    if(stringtype != None):
        return stringtype
    if(is_float(textval)):
        return textval

    return None

#given a columnindex grabs all the data in that index and returns it in a array
def getNumericalData(tabledata, columnindex):

    numericalData = []
    
    for row in tabledata[1:]:
        col = row.find_all("td")[columnindex]
        numericalData.append(determineAndReturnColType(col.text))
    
    return numericalData


#Checks the table for a numerical row, plots the data if found
#and also returns true.
def checkforNumericalRowAndPlot(table):
    tabledata = table.tbody.find_all("tr")

#Insures it only grabs a table that has more than 2 rows 
    if(len(tabledata)< 2):
        print("Table too small to plot")
        return False

    row = tabledata[1]
    colnum =0
    numericalcolindex= None

    #Iterates through the first row of the columns to determine if any of them 
    #contains numerical data 
    for col in row.find_all("td"):
        found = determineAndReturnColType(col.text)
        if(found != None):
            print("Found defined numerical column value: "+found)
            numericalcolindex = colnum
            continue
        colnum += 1 

    if(numericalcolindex != None):
        print("plotting graph")
        NumericalData = getNumericalData(tabledata, numericalcolindex )
        plt.plot(range(len(NumericalData)), NumericalData)
        plt.savefig('wikitable.png')
       
        return True
    else:
        print("no numerical column found")
        return False





