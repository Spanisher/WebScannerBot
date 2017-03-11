from tld import get_tld

def dame_el_dominio(url):
	nombre_del_dominio = get_tld(url)
	return nombre_del_dominio

