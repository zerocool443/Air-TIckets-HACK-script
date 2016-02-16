from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


location = "MAA";
destination = "DEL";
date=input("Enter date in format Y-M-D")

link="https://www.google.co.in/flights/#search;f="+location+";t="+destination+";d="+str(date)+"+tt=0"



page=urlopen(link).read();
soup=BeautifulSoup(page);


