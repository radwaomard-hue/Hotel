print("					HOTEL					")

name=input('enter your name:')
age=int(input('enter your age:'))
address=input('enter your address:')
nationality =input('enter your nationality:')

#rooms={key:value}
rooms={
'room101':550,
'room102':500,
'room103':300,
'room104':350,
'room105':750
}

choice=input('enter your choice rooms:')
if choice in rooms:
	print('available room')
	time=input('choice days or hours:')
	if time=="days":
		days=int(input('enter days:'))
		total=days * rooms[choice]
		print(total)
		print('					customer Information					 ')
		print("room:",choice)
		print('name:',name,end="		")
		print('address:',address,end="		")
		print('nationality:',nationality,end="		")
		print('age:',age)
		from datetime import datetime

		now = datetime.now()  
		print("Date:", now.date())  
		print("Time:", now.time())
	elif time =="hours":
		hours=int(input('enter your hours:'))
		total=hours * (rooms[choice]/24)
		print(total)
		print('					customer Information					 ')
		print("room:",choice)
		print('name:',name,end="		")
		print('address:',address,end="		")
		print('nationality:',nationality,end="		")
		print('age:',age)
		from datetime import datetime

		now = datetime.now()  
		print("Date:", now.date())  
		print("Time:", now.time())
	else:
		print('try again')
else:
	print('room not available ')
