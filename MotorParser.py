import HTMLParser
import urllib

class MotorParser(HTMLParser.HTMLParser):
#class MotorParser(HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
#        self.strname = ''
#        self.strdata = ''

    def handle_starttag(self, tag, attributes):
#        if tag != 'td':
        if tag != 'div':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'id' and value == 'content':
                break
        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)
#            print data

    def pair_data(self, pairdata):
#        print 'pairing data'
        arlen = len(pairdata)
        strname = ''
        strdata = ''
        motordataarray = []
#        print arlen
        i = 0
        while (i < arlen):
            mod = i%2
#            print mod
            if mod == 0:
                strname = pairdata[i]
            else:
                strdata = pairdata[i]
                str = "\"" + strname + "\"" + ": " + "\"" + strdata + "\""  + ","
#                self.print_pair(str)
                motordataarray.append(str)
            i = i + 1
#            print "{" + strname + "=" + strdata + "}"
        return motordataarray


    def print_pair(self, str):
        print str


    def print_motor_data(self, dataarray):
        for i in dataarray:
            print i
#        print dataarray


    def print_output_header(self):
#        print ' '
#        print ' '
        print 'Running Motor Parser'
        print ' ' 

    def get_data(self):
        return self.data

    
    def get_motor_info(self, url):
        
#        p = MotorParser()
#        f = urllib.urlopen("http://pro38.com/products/pro75/motor/MotorData.php?prodid=5069L1685-P")
        f = urllib.urlopen(url)
        html = f.read()
#        print html
        self.feed(html)
        arr = self.get_data()
        output = self.pair_data(arr)
        return output



#p = MotorParser()
#temp = p.get_motor_info("http://pro38.com/products/pro75/motor/MotorData.php?prodid=5069L1685-P")
#p.print_output_header()
#p.print_motor_data(temp)
#p.close()

