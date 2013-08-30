from MotorParser import *
from urllib import *
#import HTMLParser
#import urllib

class MotorFileHandler():
    def __init__(self):
        self.motorseries = 29
        self.baseurl = 'http://pro38.com/products/pro29/motor/MotorData.php?prodid='
        self.outputdatadir = './motor-data/'


    def motorfiles(self):
        try:
            filename = str(self.motorseries) + 'mm-motor-list.txt'
            print filename
            inputfile = open(filename, 'r')
#            motoriterator(inputfile)
        except IOError:
            print 'Cannot open file', filename
        else:
#            print inputfile
            self.motoriterator(inputfile)
        finally:
            inputfile.close()


    def motoriterator(self, motorlist):
        for motor in motorlist:
#           This was an error - redundant iteration 
#            motor = motorlist.readline()
            self.getmotordata(motor.strip())


    def getmotordata(self, motorid):
        try:
            outfile = self.outputdatadir + motorid + ".txt"
            url = self.baseurl + motorid
            print outfile
            outputfile = open(outfile, 'w')
            mp = MotorParser()
            motordata = mp.get_motor_info(url)
            for item in motordata:
                outputfile.write(item)
            mp.close()
        except IOError:
            print 'Cannot open outputfile', outfile
        else:
            print 'Getting motor data for: ' + motorid
        finally:
            outputfile.close()
#            print 'This is the finally block'

mfh = MotorFileHandler()
mfh.motorfiles()
mfh.close()

