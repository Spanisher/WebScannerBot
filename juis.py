import os

def quien_eres_morenito(url):
	jodido_comando='proxychains whois ' + url
	procesado_del_jodido_comando=os.popen(jodido_comando)
	resultado_del_jodido_comando=str(procesado_del_jodido_comando.read())
	return resultado_del_jodido_comando