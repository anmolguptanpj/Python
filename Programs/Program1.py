import datetime

name = str(input("Enter Your Name: ")).title().replace(" ","")
year = int(input("Enter your Birth Year: "))



currentYear = datetime.date.today().year

age = currentYear - year

print("Name:",name)
print("Age:",age)

