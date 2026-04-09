import random
letters=['a','b,c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','#','@',"%","^","&",'*','()',"-",'_',"="]

print("welcom to the pypassword generator")
nr_letter=int(input("how many letters would you likein your password?"))
nr_symbol=int(input("how many symbols would you likein your password?"))
nr_number=int(input("how many number would you likein your password?"))

password=""
for character in range(0,nr_letter):
    password+=random.choice(letters)

for character in range(0,nr_symbol):
    password+=random.choice(symbols)

for character in range(0,nr_number):
    password+=random.choice(numbers)

print(password)