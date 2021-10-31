## How to Run

in the detector inspector directory run the program using python. Insure you have the latest python installed with the BeautifulSoup library. The program will take the first
argument for the website you want the program to look at as shown below. 

```
python .\DetectorInspector.py "https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression"

```
## Assumptions

The program will look through all of the tables in the page for a numerical column. Once a numerical column is found it will only graph that column and the program will terminate once that column is plotted and saved in a file called wikitable.png within the detectorinspector directory. 

Only columns with explictily numerical values will be plotted with the inclusion of some outliers such as those with meter readings e.g "1.73 m (5 ft 8 in)" and time readings e.g
"1:51.9"

## Testing

Testing can be done by running  pytest on the test_DetectorInspectorFunctions.py and test_stringMatcher.py scripts. 
