import os

def scan_ports(opcion,ip):
	comando = 'proxychains nmap ' + opcion + " " + ip
	ejecutar_comando= os.popen(comando)
	resultado = str(ejecutar_comando.read())
	return resultado


