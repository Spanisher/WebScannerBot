import urllib.request
import io

#Sobrescribimos la clase para que no cante la libreria a la hora de parsear algunas web
class AppURLopener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"

'''opener = AppURLopener()
response = opener.open('http://httpbin.org/user-agent')'''

def los_robotos_jeje(url):
	if url.endswith('/'):
		direcion=url
	else:
		direcion=url+'/'
	'''req = urllib.request(direcion+"robots.txt",headers={'User-Agent': 'Mozilla/5.0'})
	requesta= urllib.request.urlopen(req,data=None)'''
	opener = AppURLopener()
	prueba = opener.open(direcion+"robots.txt",data=None)
	data = io.TextIOWrapper(prueba, encoding='utf-8')
	'''requesta= urllib.request.urlopen(direcion+"robots.txt",data=None)		
	data = io.TextIOWrapper(requesta, encoding='utf-8')'''
	return data.read()

