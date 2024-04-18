#1
myname= "Ahmed",
print(type(myname))

#================================================================
#2
print("=" * 40)
friends = ("Osama", "Ahmed", "Saadawy")
"""
tuple is immutable object 
so to update it we need to convert it to list
"""
list_friends = list(friends)
list_friends[0]="Elzero"

friends = tuple(list_friends)
print(friends)
print(type(friends))
print(len(friends))

#===================================================================
#3
print("=" * 40)
nums = (1,2,3)
letters = ('A', 'B', 'C')

nums_letters = nums + letters

print(nums_letters)
print(len(nums_letters))


#===================================================================
#4
print("=" * 40)

my_tuple = (1, 2, 3)
a,b,c = 1,2,3
print(a)
print(b)
print(c)