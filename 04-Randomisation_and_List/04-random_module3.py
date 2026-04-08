import random
#import list    #it could be used like this but problem is pythol file cant start with number but here i named it in this way to organise in order rest we can import like this
#from list import states

states=["himachal pradesh","tamil nadu","madhya pradesh","karnatka","maharastra"]
print(random.choice(states))

random_index=random.randint(0,4)
print(states[random_index])


length=(len(states))
print(length)
print(states[length-1])