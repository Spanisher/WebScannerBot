import os

def dame_tu_ip(url):
	comando = "tor-resolve " + url
	proceso_comando= os.popen(comando)
	resultado= str(proceso_comando.read())
	#marcador=resultado.find('has address') + 12
	#return resultado[marcador:].splitlines()[0]
	return resultado 



