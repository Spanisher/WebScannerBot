import telebot
from telebot import types
from main import *
import datetime
from datetime import datetime, date

#Creamos nuestro objeto bot con el token de la api
scanBot=telebot.TeleBot("367982708:AAHgvsHCKFWAbJSgagzZvIcSYS3J1p4Tw-I")

knownUsers = [line.rstrip('\n') for line in open('usuarios.txt')]
userStep = {}
userProj = {}
hideBoard=types.ReplyKeyboardRemove()

#Hook para controlar las acciones del usuario
def get_user_step(uid):
	if uid in userStep:
		return userStep[uid]
	else:
		knownUsers.append(uid)
		userStep[uid] = 0
		print ("Nuevo usuario detectado, que no ha usado mi bot todavia")
		return 0

# Función para los logs y etc
def listener(messages):
	for m in messages:
		cid = m.chat.id
		if m.content_type == 'text': # Sólo saldrá en el log los mensajes tipo texto
			if cid > 0:
				mensaje = str(m.chat.first_name) + " [" + str(cid) + "] " + str(datetime.now())+" : " + m.text 
			else:
				mensaje = str(m.from_user.first_name) + "[" + str(cid) + "] "+ str(date.today())+" : " + m.text 
			f = open('log.txt', 'a')
			f.write(mensaje + '\n')
			f.close()
			print (mensaje)

scanBot.set_update_listener(listener)

@scanBot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	if str(cid) not in knownUsers: 
		knownUsers.append(str(cid))  
		usuario=m.chat.username
		ficher = open( 'usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
		ficher.write( str(cid) +"\n")
		ficher.close()
		userStep[cid] = 0  
		scanBot.send_message(cid, "Hola extraño deja que te escanee......")
		scanBot.send_message(cid, "Escaneado completo, ahora sé quien eres.... "+str(usuario))
	else:
		scanBot.send_message( cid, "Bienvenido al WebScanner que puedo hacer por ti")

@scanBot.message_handler(commands=['scan'])
def command_scan(m):
	cid=m.chat.id
	nombre = m.text[6:]
	if (nombre[0:3] == "www"):
		botones=types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=2)
		botones.add("ROBOTS","PUERTOS","WHOIS","SHODAN")		
		print(nombre[4:])
		scanBot.send_chat_action(cid, 'typing')
		gather_info(nombre[4:],"http://"+nombre,'-v -sV')
		userProj[cid]=nombre[4:]
		scanBot.send_message(cid,'elige algo pa descargar',reply_markup=botones)
		userStep[cid]=2
	elif ((nombre[0].isdigit()) and (nombre[-1].isdigit())):
		botones=types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=2)
		botones.add("INFO","SHODAN")
		print(nombre)
		scanBot.send_chat_action(cid, 'typing')
		gather_info_ip(nombre)
		userProj[cid]=nombre
		scanBot.send_message(cid,'elige algo pa descargar',reply_markup=botones)
		userStep[cid]=2
	else:
		scanBot.send_message(cid, "Introduce una direccion válida www.loquesea.com")

@scanBot.message_handler(func=lambda message: get_user_step(message.chat.id)==2)
def manejo_descarga(m):
	cid=m.chat.id
	if m.text=='ROBOTS':
		scanBot.send_document(cid,open("www/"+userProj[cid]+" "+str(date.today())+"/robots_txt.txt", 'rb'), reply_markup=hideBoard)
	elif m.text=='PUERTOS':
		scanBot.send_document(cid,open("www/"+userProj[cid]+" "+str(date.today())+"/nmap.txt", 'rb'), reply_markup=hideBoard)
	elif m.text=='WHOIS':
		scanBot.send_document(cid,open("www/"+userProj[cid]+" "+str(date.today())+"/whois.txt", 'rb'), reply_markup=hideBoard)
	elif m.text=='INFO':
		scanBot.send_document(cid,open("www/"+userProj[cid]+" "+str(date.today())+"/reverse_dns.txt", 'rb'), reply_markup=hideBoard)
	elif m.text=='SHODAN':
		scanBot.send_document(cid,open("www/"+userProj[cid]+" "+str(date.today())+"/shodan_info.txt", 'rb'), reply_markup=hideBoard)
	else:
		scanBot.send_message(cid,'carota')


scanBot.polling(none_stop=True)