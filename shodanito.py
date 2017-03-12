import shodan
import sys
import io

SHODAN_API_KEY = "ZpshAGght7Y4wcORioScKwvWzzR99dca"

api = shodan.Shodan(SHODAN_API_KEY)


def shodanizar(ip):
	try:
		host = api.host(ip)

		# Imprimiendo la información obtenida
		basicData= str('IP: %s' % host['ip'])+"\n"+str('Pais: %s' % host.get('country_name'))+"\n"+str('City: %s' % host.get('city'))+"\n"+str('Latitud: %s' % host['latitude'])+"\n"+str('Longitud: %s' % host['longitude'])+"\n"+str('Hostname: %s' % host['hostnames'])+"\n"
		portData="\n\n"
		# Imprimimos los banners
		for item in host['data']:			
			portData=portData+str ('Puerto: %s' % item['port'])+str ('Banner: %s' % item['data'])
		return basicData+portData

	except Exception as e:
		print('Ups! Ha ocurrido un error: %s' % e)

