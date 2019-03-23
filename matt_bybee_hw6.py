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
    x = urllib.request.urlopen(argument) #url

    data = x.readlines()
    for i in range(len(data)):
        line = data[i].decode("utf-8")
        if (re.search("\[error\]", line)):
            result = re.split("\s", line)
            if result[-2] in d:
                d[result[-2]] += 1
            else:
                d[result[-2]] = 1

    print ("*** TOP 25 PAGE ERRORS ***") 
    for key, value in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
        print ("Count: %9i Page: %s" % (value, key))
        n += 1
        if (n == 25):
            break
        else:
            continue
    return

#main
try:
    parseArg(sys.argv[1])
except IndexError:
    help()
