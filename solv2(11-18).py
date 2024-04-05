#1
myname="Ahmed"
myage="20"
mycountry="Egypt"

print('"'+"Hello, "+"'"+myname+"' ,"+"How you doing \\  "+'"""'+" Your Age is "+'"'+myage+'""'+" And your country is : "+mycountry)

#================================================================
#2
print("=" * 40)

print('"'+"Hello, "+"'"+myname+"' ,"+"How you doing \\ \n" 
    +' """'+" Your Age is "+'"'+myage+'""'+' + \n'
    +" And your country is : "+mycountry)

#================================================================
print("=" * 40)
#3
# Using indexing to access single item
name = "ElZero"

print(name[1])#L
print(name[2])#Z
print(name[-1])#O

#================================================================
print("=" * 40)
#4
#Using slicing to access multiple item
print(name[1:4])#lZe
print(name[0:5:2])#Ezr
print(name[-2:-7:-2])#rZE

#================================================================
print("=" * 40)
#5
name5 = "#@#@ElZero#@#@"
print(name5.strip("#@"))

#================================================================
print("=" * 40)
#6
num1="1"
num2="11"
num3="119"
num4="1199"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))

#================================================================
print("=" * 40)
#7
#we should get length of the string at first
name_one="Ahmed"
name_two="M_Saadawy"

print(name_one.rjust(15,'@'))
print(name_two.rjust(15,'@'))

#================================================================
print("=" * 40)
#8
#to convert capital letter to small letter and the reverse ,we use swapcase method
print(name_one.swapcase())
print(name_two.swapcase())

#================================================================
print("=" * 40)
#9
msg="I love python and Although I love elzero web school"

print(msg.count("love"))
print(msg.count("love",0,25))

#=================================================================
print("=" * 40)
#10
print("the index of Z in ElZero is "+ str(name.index("Z")))

#================================================================
print("=" * 40)
#11

msg2="I <3 python and Although I <3 elzero web school"

print(msg2.replace("<3","love",1))

#================================================================
print("=" * 40)
#12
print(msg2.replace("<3","love",2))

#================================================================
print("-" * 40)
#13

myname2="Osama"
myage2=30
mycountry2="United"
salary=3.50054

print(f"My name is {myname2:s} and my age is {myage2:d} and I live in {mycountry2:s} and my salary is {salary:.3f}")


