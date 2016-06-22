from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


print("CHOSE YOUR location and destination code ")

print("Agartala	Tripura	Agartala Singerbhil	IXA
Agra	Uttar Pradesh	Agra Airport	AGR
Ahmedabad	Gujarat	Ahmedabad Airport	AMD
Allahabad	Uttar Pradesh	Allahabad Bamrauli	IXD
Amritsar	Punjab	Amritsar Raja Sansi Airport	ATQ
Aurangabad	Maharashtra	Chikalthan	IXU
Bagdogra	Sikkim	Bagdogra Airport	IXB
Bangalore	Karnataka	Bangalore Airport	BLR
Bhavnagar	Gujarat	Bhavnagar Civil Airport	BHU
Bhopal	Madhya Pradesh	Bhopal Airport	BHO
Bhubaneswar	Orissa	Bhubaneswar Airport	BBI
Bhuj	Gujarat	Bhuj Rudra Mata Airport	BHJ
Calcutta (Kolkata)	West Bengal	Netaji S C Bose International Airport	CCU
Chandigarh	Chandigarh	Chandigarh Airport	IXC
Chennai(Madras)	Tamil Nadu	Menmbarkam Airport	MAA
Cochin	Kerala	Cochin Airport	COK
Coimbatore	Coimbatore	Coimbatore Peelamedu Airport	CJB
Daman	Daman	Daman Airport	NMB
Dehradun	Uttar Pradesh	Dehradun Grant Airport	DED
Dibrugarh	Assam	Dibrugarh Airport	DIB
Dimapur	Nagaland	Dimapur Airport	DMU
Diu	Daman and Diu	Diu Airport	DIU
Gauhati	Assam	Gauhati Borjhar	GAU
Goa	Goa	Dabolim Airport	GOI
Gwalior	Madhya Pradesh	Gwalior Airport	GWL
Hubli	Karnataka	Hubli Airport	HBX
Hyderabad	Andhra Pradesh	Begumpet Airport	HYD
Imphal	Manipur	Imphal Municipal Airport	IMF
Indore	Madhya Pradesh	Indore Airport	IDR
Jaipur	Rajasthan	Jaipur Airport	JAI
Jammu	Jammu & Kashmir	Jammu Airport	IXJ
Jamnagar	Gujarat	Govardhanp Airport	JGA
Jamshedpur	Jharkhand	Jamshedpur Sonari Airport	IXW
Jodhpur	Rajasthan	Jodhpur Airport	JDH
Jorhat	Assam	Rowriah Airport	JRH
Kanpur	Utter Pradesh	Kanpur Airport	KNU
Khajuraho	Madhya Pradesh	Khajuraho Airport	HJR
Kozhikode (Calicut)	Kerala	Kozhikode (Calicut) Airport	CCJ
Leh	Jammu & Kashmir	Leh Airport	IXL
Lucknow	Utter Pradesh	Amausi Airport	LKO
Ludhiana	Punjab	Ludhiana Sahnewal	LUH
Madurai	Tamil Nadu	Madurai Airport	IXM
Mangalore	Karnataka	Mangalore Bajpe Airport	IXE
Mumbai (Bombay)	Maharashtra	C S M International Airport	BOM
Nagpur	Maharashtra	Sonegaon Airport	NAG
Nanded	Maharashtra	Nanded Airport	NDC
Nasik	Maharashtra	Gandhi Nagar Airport	ISK
New Delhi	Delhi	Indira Gandhi International Airport	DEL
Patna	Bihar	Patna Airport	PAT
Pondicherry	Union Territory (UT)	Pondicherry Airport	PNY
Poona (Pune)	Maharashtra	Lohegaon Airport	PNQ
Porbandar	Gujarat	Porbandar Airport	PBD
Port Blair	Andaman and Nicobar Islands	Port Blair Airport	IXZ
Puttaparthi	Andhra Pradesh	Puttaparthi Airport	PUT
Rae Bareli	Uttar Pradesh	Rae Bareli Airport	BEK
Rajkot	Gujarat	Rajkot Airport	RAJ
Ranchi	Jharkhand	Ranchi Airport	IXR
Shillong	Meghalaya	Shillong Barapani Airport	SHL
Silchar	Mizoram	Kumbirgram Airport	IXS
Srinagar	J & K	Srinagar Airport	SXR
Surat	Gujrat	Surat Airport	STV
Tezpur	Assam	Tezpur Airport	TEZ
Tiruchirapally	Tamil Nadu	Tiruchirapalli Airport	TRZ
Tirupati	Andhra Pradesh	Tirupati Airport	TIR
Trivandrum	Kerala	Trivandrum International Airport	TRV
Udaipur	Rajasthan	Udaipur Airport	UDR
Vadodara	Gujarat	Vadodara Airport	BDQ
Varanasi	Utter Pradesh	Babatpur Airport	VNS
Vijayawada	Andhra Pradesh	Vijayawada Airport	VGA
Vishakhapatnam	Andhra Pradesh	Vishakhapatnam Airport	VTZ
")


read location 
read destination
date=input("Enter date for the filght in format Y-M-D")

link="https://www.google.co.in/flights/#search;f="+location+";t="+destination+";d="+str(date)+"+tt=0"



page=urlopen(link).read();
soup=BeautifulSoup(page);


