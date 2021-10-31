import DetectorInspectorFunctions
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def test_determineAndReturnColType():
    assert  DetectorInspectorFunctions.determineAndReturnColType("2.0 m  (asd13q221#)") == "2.0  "
    assert  DetectorInspectorFunctions.determineAndReturnColType("12:00:12") == '12:00:12'
    assert  DetectorInspectorFunctions.determineAndReturnColType("2") == '2'



def test_checkforNumericalRowAndPlot():

    url = 'https://en.wikipedia.org/wiki/500_metres'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    tables = soup.find_all("table")

    table = tables[0]
    assert DetectorInspectorFunctions.checkforNumericalRowAndPlot(table) == False

   