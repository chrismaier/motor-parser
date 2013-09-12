import urllib 
import MotorParser

p = MotorParser.MotorParser()
temp = p.get_motor_info("http://pro38.com/products/pro75/motor/MotorData.php?prodid=5069L1685-P")
temp.print_output_header()
temp.print_motor_data(temp)
p.close()
