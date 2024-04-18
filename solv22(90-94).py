#1
# Num = input("Enter a number :")

# if len(Num) != 1:
#         raise IndexError("only one char allowed, integer number")

# if Num.isdigit():
#     Num = int(Num)
#     if Num==0:
#         raise ValueError("number must be greater than zero")
#     print(f"The number {Num}")
# else:
#     raise TypeError("Invalid number, must be an integer")


#============================================================================
#2
print(f"=" * 40)

# try:
#     letter = input("add letter from A-Z : ")
#     if len(letter) != 1:
#         raise IndexError("you must write one letter only")

#     if not letter.istitle():
#         raise ValueError("The Letter Not In A - Z")

# except IndexError as I:
#         raise (I)
# except ValueError as v:
#         raise (v)

# else:
#     print(f"the letter is {letter}")

#================================================================
#3
print("=" * 40)

def calculate(num1, num2) -> int: #type hinting
    return num1 + num2

res = calculate(10, 10)
print(type(res))
print(calculate(10, 20))



