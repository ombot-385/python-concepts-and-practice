print("welcome to treasure island")
choice1=input("you are at a crossroad choose 'left'or 'right' where you would want to go \n").lower()

if(choice1=="left"):
    choice2=input("you came to a lake do you want to 'swim' or 'wait'\n").lower()
    if(choice2=="wait"):
        choice3=input("you came to a huge door of three colours 'red' and 'yrllow' and 'blue' \n").lower()
        if(choice3=='blue'):
            print("you found the treasure")
        elif(choice3=='yellow'):
            print("you enter the room of fire game over")
        elif(choice3=='red'):
            print("you entered the room of beast so game over")
        else:
            print("door dont exist so game over")
    else:
        print("wrong choice game over")
else:
    print("wrong path game over")