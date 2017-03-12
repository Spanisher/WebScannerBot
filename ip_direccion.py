import os

def dame_tu_ip(url):
	comando = "tor-resolve " + url
	proceso_comando= os.popen(comando)
	resultado= str(proceso_comando.read())
	#marcador=resultado.find('has address') + 12
	#return resultado[marcador:].splitlines()[0]
	return resultado 

def dame_tu_host(ip):
	comando = "proxychains nslookup " + ip
	proceso_comando = os.popen(comando)
	resultado = str(proceso_comando.read())
	marca = resultado.find(('name = '))
	marca2 = resultado.find('Server:		')
	marcaFin = resultado.find('Authoritative')
	marcaFin2 = resultado.find('Non-authoritative')
	if resultado[marca:marcaFin] == "":
		return resultado
	else:
		return resultado[marca2:65] + resultado[marca:marcaFin]



