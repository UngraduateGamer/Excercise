import time
name=input('Enter your Name: ')
current_time=time.strftime('%H:%M:%S')
print("The Time is :",current_time)

hours=int(time.strftime('%H'))

if (hours>0 and hours<=12):
    print("Good Morning",name)
    
elif(hours>12 and hours<17):
    print("Good AfterNoon",name)
    
elif(hours>=17 and hours<24):
    print("Good Night",name)
    