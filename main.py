from dominios import *
from general import *
from ip_direccion import *
from juis import *
from los_robotos import *
from mapeo import *
from shodanito import *
from datetime import date

#Creamos la variable con el directorio 
ROOT_DIR='www'
#Creamos el directorio, la misma función implementada en general.py comprueba si el directorio está creado o no para crearlo
crear_directorio(ROOT_DIR)

def gather_info(name, url, opcion):
	if not comprobar_directorio("www/"+name + " " + str(date.today())):
		try:
			nombre_dominio = dame_el_dominio(url)
			direccion_ip = dame_tu_ip(nombre_dominio)
			nmap = scan_ports(opcion, direccion_ip)
			robots = los_robotos_jeje(url)
			whois = quien_eres_morenito(nombre_dominio)
			shodaninfo = shodanizar(direccion_ip)
			#print(nombre_dominio+"\n"+direccion_ip+"\n"+nmap+"\n"+robots+"\n"+whois)
			crear_informe(name, url, nombre_dominio, direccion_ip,nmap,robots,whois,shodaninfo)
		except Exception as e:
			print( type(e).__name__ )


def crear_informe(name, full_url, nombre_dominio, direccion_ip,nmap,robots,whois,shodita):
	directorio_proyecto = ROOT_DIR + '/' + name + " " + str(date.today())
	crear_directorio(directorio_proyecto)
	escribir_file(directorio_proyecto+'/full_url'+'.txt',full_url)
	escribir_file(directorio_proyecto+'/domain_name'+'.txt',nombre_dominio)
	escribir_file(directorio_proyecto+'/nmap'+'.txt',nmap)
	escribir_file(directorio_proyecto+'/robots_txt'+'.txt',robots)
	escribir_file(directorio_proyecto+'/whois'+'.txt',whois)
	escribir_file(directorio_proyecto+'/shodan_info'+'.txt',shodita)

def gather_info_ip(ip):
	if not comprobar_directorio("www/"+ ip + " " + str(date.today())):

		try:
			host = dame_tu_host(ip)
			shodaninfo = shodanizar(ip)
			directorio_proyecto = ROOT_DIR + '/' + ip + " " + str(date.today())
			crear_directorio(directorio_proyecto)
			escribir_file(directorio_proyecto+'/reverse_dns'+'.txt',host)
			escribir_file(directorio_proyecto+'/shodan_info'+'.txt',shodaninfo)
		except Exception as e:
			print( type(e).__name__ )


