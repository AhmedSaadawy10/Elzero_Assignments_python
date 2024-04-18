#1
name = input("Enter Your Name : ").strip().capitalize()
print(f"hello {name} happy to see you here")

#================================================================
#2
print("=" * 40)

age = input("Enter Your Age : ").strip()

#check if age is digit
if age.isdigit():
    age = int(age)
    if age < 16:
        print(f"Hello your age is under 16 some article not suitable for you. ")
    else:
        print(f"Hello your age is suitable  All article are available for you. ")


#================================================================
#3
print("=" * 40)

first_name = input("Enter your firstname: ").strip().capitalize()
second_name = input("Enter your secondname: ").strip().capitalize()

print(f"hello {first_name} {second_name:.1s}, happy to see you!")


#================================================================
#4
print(f"=" * 40)

email = input("Enter your email: ").strip().lower()

print(f"the name before @ "+email[0:email.index("@")].capitalize())
print(f"the domain after @ "+email[email.index("@")+1 : ].capitalize())
