import datetime
import re
import os

'''
run in prod:
 cat gc_2017-03-27_05-11-01.log | grep "Eden: \|pause " | grep mixed -A 1
stats working on output     file holding:
2017-03-27T11:50:45.516-0400: 23983.926: [GC pause (G1 Evacuation Pause) (mixed), 0.0682548 secs]
   [Eden: 328.0M(328.0M)->0.0B(332.0M) Survivors: 30.0M->26.0M Heap: 1377.3M(7168.0M)->642.0M(7168.0M)]
   we wantto make the datew uniquq and for rachdate use the min heap size after mix gc
'''
file = "/Users/eladw/PycharmProjects/gcStat/resources/gcOld.log"
#file = "/Users/eladw/PycharmProjects/gcStat/resources/svpr.log"
stats = {}
quantity = -1


def printLines():
    quotes = open("/Users/eladw/PycharmProjects/gcStat/resources/gcOld.log")
    contents_of_file = quotes.read()
    quotes.seek(0)
    print(quotes.read())
    quotes.close()

#printLines()


def getLines():
    with open(file, 'r') as in_file:
        tempDate = ""
        tmpVal = ""
        for line in in_file:
            match = re.search(r'\d{4}-\d{2}-\d{2}', line)
            if match is not None:
                date = match.group()
                tempDate = date;
                '''print(date, line)'''
            else:
                if "Heap" in line:
                    tmpVal = line.split("Heap", 1)[1]
                    tmpVal = tmpVal.split("->", 1)[1]
                    tmpVal = tmpVal.split("(", 1)[0]
                    tmpVal = tmpVal.split("(", 1)[0]
                    tmpVal = tmpVal[0:tmpVal.__len__()-3]
                    print tmpVal

                    oldVal = stats.get(tempDate);
                    if(tempDate in stats.keys()):
                        oldVal = stats.get(tempDate);
                        if(oldVal is None):
                            stats[tempDate] = tmpVal
                        else:
                            if int(tmpVal)<int(oldVal):
                                stats[tempDate] = tmpVal
                    else:
                        stats[tempDate] = tmpVal

        for k,v in stats.items():
            print(k,v)


# def extractFromBrackets(line):
#
#     tmpVal = re.search(r'\((.*?)\)', tmpVal).group(1)
#     return tmpVal


getLines()