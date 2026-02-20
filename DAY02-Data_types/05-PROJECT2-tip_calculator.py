print("WELCOME TO TIP CALCULATOR")
bill=float(input("what was your total bill"))
tip=int(input("how much tip you would like to give 10,12 or 15"))
people=int(input("how many people to split the bill"))

each_person_pay=(bill*(tip/100)+bill)/people
print(f"each person pay{each_person_pay}")

