import random
letters=['a','b,c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','#','@',"%","^","&",'*','()',"-",'_',"="]

print("welcom to the pypassword generator")
nr_letter=int(input("how many letters would you likein your password?"))
nr_symbol=int(input("how many symbols would you likein your password?"))
nr_number=int(input("how many number would you likein your password?"))

password_list=[]
for char in range(0,nr_letter):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbol):
    password_list.append(random.choice(symbols))

for char in range(0,nr_number):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print(password_list)
# Lists can be shuffled strings cant

 #we need to the following because passowrd_list will be printed as list but we need as a string
password=""
for char in password_list:
    password+=char

print(f"your password is {password}")
