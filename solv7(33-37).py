#1
#differnt 4types are true.
print(bool("ahmed"))
print(bool(["ahmed"]))
print(bool(12))
print(bool(True))

#________________________________________________________________
#differnt 4types are false.
print(bool(""))
print(bool([]))
print(bool(0))
print(bool(False))

#================================================================
#2
print("=" * 40)

# =>fisrt,create three variables
html="80%"
css="70%"
js="60%"

#=> by using the boolean operators we test the condition
print(bool((html and css and js) > "50%") )


#================================================================
#3
print("=" * 40)


#=>we create the variables
num_one=10
num_two=20
num=20

# => print the bool of num is greater than one of the two numbers
print(bool(num > (num_one or num_two)))

# => print the bool of num is greater than  the two numbers or not
print(bool(num > (num_one and num_two)))

#================================================================
#4
print("=" * 40)

num1=10
num2=20
result= num1 + num2

print(f"the result = {result}")

print(f"the result of exponent the result number of 3 = {result**3}")

print(f"the result of module the number by  26000 = {(result**3) % 26000}")

print(f"the result of division the number on  5 = {((result**3) % 26000) / 5}")

print(type(((result**3) % 26000) / 5))

#convert the result to a string
print(type(str(((result**3) % 26000) / 5)))

