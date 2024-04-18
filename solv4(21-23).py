#1
list1=['Ahmed','Mohamed','Saadawy','Fosha','Ali']

print(f"\"{list1[0]}\" => Method one")
print("\""+list1[0]+"\" => Method two")

print(f"\"{list1[-1]}\" => Method one")
print("\""+list1[-1]+"\" => Method two")

#================================================================
#2
print("=" * 40)

print(f"the odd names :{list1[::2]}")
print(f"the even names :{list1[1::2]}")

#================================================================
#3
print("=" * 40)

print(f"{list1[1:4]}")
print(f"{list1[3::]}")
#================================================================
#4
print("=" * 40)

#solution1

list1[3]="Elzero"
list1[4]="Elzero"

print(list1)
#solution2
print("=" * 40)

list1[-1:-3:-1]="Elzero", "Elzero"
print(f"{list1}")

#================================================================
#5
print("=" * 40)

# add new friend at first in list
list1.insert(0, "Elzero1")
# add new friend at last in list
list1.append("Elzero2")

print(list1)

#================================================================
#6
print("=" * 40)

#remove first two names
list1[0:2]=[]

#remove the last name
list1.pop() 
#another way to remove last name
# list1.remove(list1[-1])

print(list1)

#================================================================
#7
print("=" * 40)

friends=["Ahmed","Osama","Ali"]
employees=["Fosha","Farag"]
school=["Elsorouk","Elsalam"]

friends.extend(employees)
friends.extend(school)

print(friends)

#================================================================
#8
print("=" * 40)

#sort list from a-z
friends.sort()
print(f"{friends}")

# sort list from z-a 
friends.sort(reverse=True)
print(f"{friends}")

#================================================================
#9
print("=" * 40)

print(len(friends))


#================================================================
print("=" * 40)

technologies=["Java","Cpp","Python","C#",["flask","Php","Django"]]

print(technologies[-1][0])
print(technologies[-1][-1])