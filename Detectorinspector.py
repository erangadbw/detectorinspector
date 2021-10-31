from bs4 import BeautifulSoup
from stringMatcher import * 
import DetectorInspectorFunctions
import requests
import matplotlib.pyplot as plt
import sys


numericalcolindex = None
try:
 url = sys.argv[1]
except IndexError:
    print("Please Enter Valid URL address")
    exit()
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

#grabs all of the tables on the document
tables = soup.find_all("table")


#iterates through all of the tables until it finds a table with a numerical row sufficent for plotting
for  table in tables:
    if(DetectorInspectorFunctions.checkforNumericalRowAndPlot(table) == True):
        break

