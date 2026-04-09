# printing number from 1 to 10 using while loops
n=0
while(n<11):
    print(n)
    n+=1

# printing odd numbers from 1 to 100 using whole loops
t=0
while(t<=100):
    if(t%2==0):
        t+=1
        continue
    else:
        print(t)
        t+=1
    
# Infinite loops
while(5>3):
    print("5 is alsways greater than 3")