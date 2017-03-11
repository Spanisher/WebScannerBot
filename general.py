import os

def crear_directorio(directorio):
	if not os.path.exists(directorio):
		os.makedirs(directorio)

def escribir_file(path, data):
	ficheritolere=open(path, 'w')
	ficheritolere.write(data)
	ficheritolere.close()

def hacer_rar(nombrefile):
	comando  = "rar "+ nombrefile
	procesar_comando=os.popen(comando)

def comprobar_directorio(directorio):
	if not os.path.exists(directorio):
		return False
	else:
		return True



	