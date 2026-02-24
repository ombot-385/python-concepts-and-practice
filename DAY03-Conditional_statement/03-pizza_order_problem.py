#small pizza=15,medium pizza=20,large pizza=25
#add pepperoni +2(for small),+3 for medium or large

#add cheese=+1

print("welcome to python pizza deliveries")
size=input("what size do you want s,m,l" )
pepperoni=input("do you want pepperoni on your pizza?y or n")
cheese=input("do you want extra cheese?y or n")

cost=0
if(size=="s"):
    cost+=15
elif(size=="m"):
    cost+=20
else:
    cost+=25

if((pepperoni=="y")and (size=="s")):
    cost+=2
elif((pepperoni=="y")and (size=="m" or size=="l")):
    cost+=3

if(cheese=="y"):
    cost+=1

print(f"your final bill is{cost} ")


