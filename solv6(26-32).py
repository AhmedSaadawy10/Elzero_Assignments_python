#1
my_list=[1,2,3,3,4,5,1]
unique_list=[1,2,3,4,5]

print(unique_list)
print(type(unique_list))

unique_list.remove(unique_list[-1])
print(unique_list)

#============================================================================
#2
print("="* 40)

nums={1,2,3}
letters={"A","B","C"}


# =>1
print(nums.symmetric_difference(letters))

# =>2
allitems=nums.union(letters)
print(allitems)

# =>3
#convert set to list
nums_list= list(nums)
letters_list= list(letters)

nums_list.extend(letters_list)

#then return list to set
nums= set(nums_list)
letters= set(letters_list)

#finally print updated set
print(nums)

#================================================================
#3
print("_" * 40)

my_set={1,2,3}
my_letters={"A", "B", "C"}

# =>1
print(my_set)

# =>2
my_set.clear()
print(my_set)
# =>3
my_set.add("A")
my_set.add("B")

print(my_set)
#=>4
my_set.discard("C")
#=>Remove an element from a set if it is a member.
# If the element is not a member, do nothing.

#================================================================
#4
print("_" * 40)

set_one={1,2,3}
set_two={1,2,3,4,5,6}

print(set_one.issubset(set_two))

#================================================================
#5
print("_" * 40)

skills={
    "Html":"90%",
    "css":"70%",
    "js":"60%",
    "python":"50%"
}
#to add another skill
skills["php"]="80%"

print(f"{list(skills)[0]},progress is => {skills['Html']}")
print(f"{list(skills)[1]},progress is => {skills['css']}")
print(f"{list(skills)[2]},progress is => {skills['js']}")
print(f"{list(skills)[3]},progress is => {skills['python']}")
print(f"{list(skills)[4]},progress is => {skills[list(skills)[4]]}")


