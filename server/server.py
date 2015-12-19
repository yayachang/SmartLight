#!/usr/bin/python
import socket
import commands
HOST='0.0.0.0'
PORT=50007

ESP_HOST = '192.168.1.21'
ESP_PORT = 1234

def runLightServer():
	try:
		global irc
		irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		irc.bind((HOST,PORT))
		irc.listen(1)
	except socket.error:
		print ('server socket.error, reconnect...')
		runLightServer()

def connectESP8266():
	try:
		global irc8266
		irc8266=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		irc8266.connect((ESP_HOST,ESP_PORT))
		irc8266.settimeout(5)
	except socket.error:
		print('ESP8266 socket.error, recconect...')
		connectESP8266()

runLightServer()
connectESP8266()

while 1:
	print '------waiting------'
	try:
		conn,addr=irc.accept()
		data=conn.recv(1024)
		print 'Connected '+addr[0] + ':' + str(addr[1])+',receive:'+data
	except:
		print('Light server error')
		print('restart light server')
		runLightServer()
	try:
		if data:
			irc8266.sendall('1')
		else:
			irc8266.sendall('0')
		data2 = irc8266.recv(1024)
		print('ESP8266 response:{}'.format(data2)+'\n')
	except:
		print('ESP8266 error')
		print('reconnect ESP8266')
		connectESP8266()
conn.close()