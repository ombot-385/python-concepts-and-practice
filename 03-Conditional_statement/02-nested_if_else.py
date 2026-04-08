print("welcome to rollercoaster ride")
height=int(input("enter your height in cm"))

if(height>120):
    print("you can take a ride")
    age=int(input("enter yor age"))
    if(age<=12):
        print("please pay $5")
    elif(age<=18):
        print("please pay $7")
        
    else:
        print("please pay $12")

    
else:
    print("sorry you have to grow taller before you can ride")
