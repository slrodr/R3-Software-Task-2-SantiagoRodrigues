import socket

speeds = ['0', '1', '2', '3', '4', '5']
speed = 0

#Socket Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1435))

s.listen(1)
client, address = s.accept()
with client:
	print(f"Connection from {address} has been established") #check correct
	while True:
		data = client.recv(1024)
		client.send(data)
		data = data.decode ('utf-8')
		#print(f"Received: {data.decode('utf-8')}")
		if str(data) in speeds:  #Check if entered key sets a speed
			speed = int((int(data)/5) * 255)  #Set speed based on received keys
			#print(f"Speed: {speed}")
		else:
			speed = speed

		#Motor Steering
		if data =='w':
			print(f"[f,{speed}][f,{speed}][f,{speed}][f,{speed}]")
		if data =='a':
			print(f"[r,{speed}][r,{speed}][f,{speed}][f,{speed}]")
		if data == 's':
			print(f"[r,{speed}][r,{speed}][r,{speed}][r,{speed}]")
		if data == 'd':
			print(f"[r,{speed}][r,{speed}][f,{speed}][f,{speed}]")

client.close()

