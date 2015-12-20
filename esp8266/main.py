# This script is run on boot
import pyb
import esp

pin  = pyb.Pin(2, pyb.Pin.OUT_PP)

def recv(socket,data):        
	print('receive cmd:')
	print(data)
	if data == b'0':
		pin.value(0)
	elif data == b'1':
		pin.value(1)
	print('current status:')
	print(pin.value())
	socket.send(str(pin.value()))

socket = esp.socket()
socket.onconnect(lambda s: s.onrecv(recv))
socket.bind(('0.0.0.0',1234))
socket.listen(1)
