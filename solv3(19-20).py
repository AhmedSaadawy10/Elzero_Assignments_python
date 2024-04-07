#1
print(type(100))
print(type(100.10))
print(type(100 + 2j))

#________________________________________________________________
#2
print("_" * 40)

mycomplex= 100+5j

print(f"The imaginary part is : {mycomplex.imag}")
print(f"The real part is : {mycomplex.real}")

#________________________________________________________________
#3
print("_" * 40)

n=10

print("{:.10f}".format(n))
print(f"{n:.5f}")

#________________________________________________________________
#4
print("_" * 40)

num= int(123.345)

print(num) 

print(type(num))

#________________________________________________________________
#5
print("_" * 40)

print(100-115)
print(50 * 30)
print(21 % 4)
print(110 / 11)
print(97 // 20)