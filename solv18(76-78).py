#1
# import random
# print(f"random number between 10 and 50 = {random.randrange(10,50)}")
# print(f"random even number between 2 and 10 = {random.randrange(2,10,2)}")
# print(f"random odd number between 1 and 9 = {random.randrange(1,9,2)}")
# print(dir(random))

#================================================================
#2
print("=" * 40)

# import my_mod
# print(dir(my_mod))
# print(my_mod.say_hello("Ahmed"))
# print(my_mod.say_welcome("Saadawy"))

#================================================================
#3
print("=" * 40)

from my_mod import say_welcome
print(say_welcome("Mohamed"))

#================================================================
#4
print("-"* 30)

from my_mod import say_hello
print(say_hello("Saadawy"))