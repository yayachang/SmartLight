# This script is run on boot
import pyb
import esp
pin  = pyb.Pin(2, pyb.Pin.OUT_PP)

def recv(socket,data):
	if pin.value():
		pin.value(0)
		socket.send('on')
	else:
		pin.value(1)
		socket.send('off')

socket = esp.socket()
socket.onconnect(lambda s: s.onrecv(recv))
socket.bind(('0.0.0.0',1234))
socket.listen(1)