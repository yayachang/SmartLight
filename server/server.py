#!/usr/bin/python
import socket
import commands
import datetime

TAG='[ETB]'
HOST='0.0.0.0'
PORT=50007

ESP_HOST = '192.168.1.5'
ESP_PORT = 1234

def runLightServer():
	global serverSocket
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
	serverSocket.bind((HOST,PORT))
	serverSocket.listen(1)
	
def connectESP8266():
	try:
		global espSocket
		espSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		espSocket.connect((ESP_HOST,ESP_PORT))
		espSocket.settimeout(5)
	except socket.error:
		print(str(datetime.datetime.now())+':'+TAG+'ESP8266 socket.error, recconect...')
		connectESP8266()

runLightServer()
connectESP8266()


while 1:
	#wait App send command
	print str(datetime.datetime.now())+':'+'------waiting------\n'
	connection,address=serverSocket.accept()
	sendData=connection.recv(3)
	print str(datetime.datetime.now())+':'+TAG+'Connected '+address[0] + ':' + str(address[1])+' -- send data:'+sendData
	
	try:
		#send command to esp8266
		if sendData == '0':
			espSocket.sendall('0')
		elif sendData == '1':
			espSocket.sendall('1')
		elif sendData == '2':
			espSocket.sendall('2')
		else:
			espSocket.sendall('0')
		print str(datetime.datetime.now())+':'+TAG+'Send data to ESP8266:'+sendData
		
		#receive response from esp8266
		esp8266Response = espSocket.recv(1024)
		print(str(datetime.datetime.now())+':'+TAG+'ESP8266 response:{}'.format(esp8266Response)+'\n')
		#send response to App
		connection.sendall(esp8266Response)

		connection.close()
	except:
		print(str(datetime.datetime.now())+':'+TAG+'ESP8266 error')
		print(str(datetime.datetime.now())+':'+TAG+'reconnect ESP8266')
		connectESP8266()
connection.close()
