from bs4 import BeautifulSoup
import urllib.request
import time

tmp_scoDom = ''
tmp_scoExt = ''
icpt = 0

ip = '192.168.0.50'
port = '14192'

def vibrate(level=20):
	url = 'http://' + ip + ':' + str(port) + '/Vibrate?v=' + str(level)
	print ("================ vibrate ===================")
	print (url)
	try:
		response = urllib.request.urlopen(url)
	except IOError:
		print ("connection refused, launch body chat please")
	time.sleep(10)
	url = 'http://' + ip + ':' + str(port) + '/Vibrate?v=' + str(0)
	print (url)
	try:
		response = urllib.request.urlopen(url)
	except IOError:
		print ("connection refused, launch body chat please")

while 1:
	#url = "http://mathemagie.net/sextoy_but/index.html"
	url = "https://www.lequipe.fr/Football/match/363830"
	try:
		r = urllib.request.urlopen(url).read()
	except:
		pass

	soup = BeautifulSoup(r,"html.parser")

	scoDom = (soup.find("div", {"id": "scoDom"}).text)
	scoExt = (soup.find("div", {"id": "scoExt"}).text)

	scoDom  = ("".join(scoDom.split()))
	scoExt = ("".join(scoExt.split()))
	print ("domicile => " + scoDom)
	print ("extérieur => " +scoExt) 
	print ("======")
	#print (icpt)
	if icpt == 0:
		tmp_scoExt = scoExt
		tmp_scoDom = scoDom
	if icpt > 0:
		if scoDom != tmp_scoDom:
			vibrate()
			tmp_scoDom = scoDom
		if scoExt != tmp_scoExt:
			vibrate()
			tmp_scoExt = scoExt
	icpt = icpt +1 
	time.sleep(5)
