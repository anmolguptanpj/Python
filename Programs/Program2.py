age = int(input("Enter age:"))
qualification = input("Enter your qualification:").lower()
citizenship = (input("Enter your citizenship:")).replace(" ","").title()
experience = int(input("Enter your teaching year count"))


if age>=18 and qualification =="graduate" and citizenship == "Indian":
    if experience >=5:
        print(f"Congratulations! with {experience} years of experience , you are eligible for senior position.")
    else:
        print("You are eligible for junior position.")
else:
    print("Specifically, you do not meet criteria for this role")