#1

def remove_char(char):#1 create the function
        return char[1:-1]

friends_map=["AEmanS","ROsamaN","LAhmedL","KGamalO"]#2 create the list

clean_list=map(remove_char,friends_map)#3 map the function and the list in a varaiable

for friend in clean_list:#4 create the loop
    print(friend)

print("-" * 20)
#with lambda function
for name in map(lambda string: string[1:-1],friends_map):
    print(name)


#============================================================
#2
print("=" * 40)

friends_filter = ["osama", "azom", "elzaem", "naom", "ahmed", "AllAM"]

#dedfine function return the name endswith char 'm'
def get_names(name):
    if name:
        name = str(name)
        if name.endswith('m') or name.endswith('M'):
            print(f"{name}")

names = filter(get_names, friends_filter)

for name in names:
    print(f"{name}")
    

# with lambda function 
print("With lambda function:")
for friend in filter(lambda name : name[-1]=='m' or name[-1]== 'M',friends_filter):
    print(friend)  

#================================================================
#3
print("=" * 40)

from functools import reduce

def multiply_number(x,y):
    return x * y

numbers=[2,4,6,2,10]

result=reduce(multiply_number,numbers)

print(f"the result = {result}") 

#================================================================
#4
print("=" * 40)

skills=("Python","Java",20,"Html",30,"JavaScript") 

# skills_counter=enumerate(reversed(skills),50) 

for counter,skill in enumerate(reversed(skills),50) :
    if type(skill)==str:
        print(f"{counter} - {skill}")  
#------------------------------------
print("=" * 40)
# another way 
index =50
reversed_skills = reversed(skills)
for skill in reversed_skills:
    if type(skill)==str:
        print(f"{index} - {skill}")
        index += 1

