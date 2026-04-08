states=["himachal pradesh","tamil nadu","madhya pradesh","karnatka","maharastra"]
print(states)
print(states[3])

states[2]="kerala"
print(states)

states.append("andhra pradesh")
print(states)

states.extend("arunachal pradesh")
print(states)

states.extend(["arunachal pradesh","assam"])
print(states)