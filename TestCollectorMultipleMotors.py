import urllib 
import MotorParser


#p = MotorParser.MotorParser()

motorSize = "29"
motorFileName = "./" + motorSize + "mm-motor-list.txt"
motorFile = open(motorFileName, 'r')

for line in motorFile:

    p = MotorParser.MotorParser()
    print ' '
    print ' '
    print "Printing " + motorSize + "mm  motor information for: " + line

    temp = p.get_motor_info("http://pro38.com/products/pro" + motorSize + "/motor/MotorData.php?prodid=" + line)
    p.print_output_header()
    p.print_motor_data(temp)
    p.close()


motorFile.close()
#p.close()
