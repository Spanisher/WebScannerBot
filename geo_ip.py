import urllib.request
import io

def geoIp(ip):
	requestopen=urllib.request.urlopen("http://ip-api.com/json/"+str(ip),data=None)
	data = io.TextIOWrapper(requestopen, encoding='utf-8')
	return data.read()

