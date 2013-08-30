import urllib 

p = MotorParser
#f = urllib.urlopen("http://domain.com/somepage.html")
f = urllib.urlopen("http://pro38.com/products/pro75/motor/MotorData.php?prodid=5069L1685-P")
html = f.read()
p.feed(html)
p.close()

