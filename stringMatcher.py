import re

#Functions for finding string patters and returning the pattern found 


#checks for patter like  "1.0 m " and removes the m when returning it
def returnMeterStringPattern(text):

    meterString = re.compile("\\d+\\.\\d+\\sm\\s")
    
    meters =meterString.search(text) 

    if meters != None:
        return meters.group(0).replace("m", "")
    else: 
        return meters

#this function allows you to place the regex for the pattern you are searching for
def returnStringPattern(text,regex):

    meterString = re.compile(regex)
    
    time =meterString.search(text) 

    if time != None:
        return time.group(0)
    else: 
        return time

#returns the string if the text is a float only  
def is_float(text):
    try: 
        float(text)
        return True
    except:
        return False              

