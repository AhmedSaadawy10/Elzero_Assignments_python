#1
num1=int(input("please enter the first number : "))
num2=int(input("please enter the second number : "))
operation=input("Select one of these operations [+,-,/,%,*] to perform : ").strip()


if operation == "+":
    result= num1 + num2
    print(f"the result of the operation {num1} {operation} {num2} = {result}")
elif operation == "*":
    result= num1 * num2
    print(f"the result of the operation {num1} {operation} {num2} = {result}")
elif operation == "-":
    result= num1 - num2
    print(f"the result of the operation {num1} {operation} {num2} = {result}")
elif operation == "/":
    result= num1 / num2
    print(f"the result of the operation {num1} {operation} {num2} = {result}")
elif operation == "%":
    result= num1 % num2
    print(f"the result of the operation {num1} {operation} {num2} = {result}")
else:
    print("this operation not found")


#================================================================
#2
print(f"=" * 40)

age = input("Enter Your age : ")

print(f"App is suitable for you " if age.isdigit() and int(age) > 16 else "App is not suitable for you")

#================================================================
#3
print("=" * 40)

your_age = input("Enter Your age : ")

if your_age.isdigit() and your_age in range(10,100):
    your_age = int(your_age)
    ageInMonths = your_age*12
    ageInWeeks = ageInMonths * 4
    ageInDays = your_age * 365
        
    print(f"Your Age In Months is {ageInMonths} months")
    print(f"Your Age In Weeks is {ageInWeeks} weeks")
    print(f"Your Age In Days is {ageInDays} days")
    
else:
    print("Your age must be a number between 10 and 100")

#================================================================
#4
print("=" * 40)

countries=["Egypt","Qatar","Ksa","Palestine","Syria"]
country=input("Enter your country : ").strip().capitalize()

discount=30
price=100

if country in countries:
    print(f"you have a discount cuase of your country the final price = {price-discount}")
else:
    
    print(f"Your country not eligable for discount ,the final price = {price}")