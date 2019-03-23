import urllib.request
import urllib.parse
import sys
import re
import operator
import collections

def help():
    """
    This is the help function
    """
    print("Usage is ./matt_bybee.py <file input>")
    return

def parseArg(argument):
    """
    This prgram accepts a log file and parses the contents of it looking for errors
    """
    n = 0 #for final loop to ensure only top 25 errors are shown
    d = {} #dictionary
    data = urllib.request.urlopen(argument).readlines() #url

    for i in range(len(data)): #go over each line individually
        line = data[i].decode("utf-8") #convert from BYTE to STR
        if (re.search("\[error\]", line)): #regex determine if error
            result = re.split("\s", line) #split on spaces
            if result[-2] in d: #if key exists, increment value
                d[result[-2]] += 1
            else: #if key does not exist, initiate key and base value of 1
                d[result[-2]] = 1

    print ("*** TOP 25 PAGE ERRORS ***") 

    for key, value in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
        #iterate over a sorted dictionary
        print ("Count: %9i Page: %s" % (value, key)) #print result
        n += 1 #but only top 25
        if (n == 25):
            break
        else:
            continue

    return

#main
try: #do try/catch for portability
    parseArg(sys.argv[1])
except IndexError:
    help()
