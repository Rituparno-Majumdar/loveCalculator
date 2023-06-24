print("Welcome to the love calculator love birds!  ")

name1 = input("enter first name:  ").lower()
name2 = input("enter second name:  ").lower()

trueStrengthName1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
trueStrengthName2 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')

trueStrength = trueStrengthName1 + trueStrengthName2

loveStrengthName1 = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
loveStrengthName2 = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

loveStrength = loveStrengthName1 + loveStrengthName2

trueLoveStrength_int = str(trueStrength) + str(loveStrength)
trueLoveStrength_int = int(trueLoveStrength_int)

print(trueLoveStrength_int)

if trueLoveStrength_int < 10 or trueLoveStrength_int > 90:
    print(f"Your score is, {trueLoveStrength_int} you go together like Coke and Mentos")
elif trueLoveStrength_int <= 50 or trueLoveStrength_int >= 40:
    print(f"Your score is, {trueLoveStrength_int} you are alright together ")
else:
    print(f"Your score is, {trueLoveStrength_int}")
