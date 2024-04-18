#1

num = input("Enter the number : ")
if num.isdigit() and int(num) > 0:
    num = int(num)
    c=0
    while num > 0:
        num -=1
        if num==6:
            continue
        if num==0:
            break
        print(num)
        c += 1
    print(f"the number of digits you printed: {c}")
else:
    print(f"the number must be greater than 0")


#================================================================
#2
print("=" * 40)

friends = ["Ahmed", "Saadawy","ali","Farag"]
ignored_names_count = 0
index = 0

while index < len(friends):
    if friends[index][0].islower():
        ignored_names_count += 1
        index += 1
        continue
    print(friends[index])
    index += 1

print("Number of ignored names:", ignored_names_count)

#============================================================================
#3
print("=" * 40)

skills=["html", "css","js","bootstrap"]

c=0
while c <len(skills):print(skills[c]);c += 1

#=============================================================================
#4
print("=" * 40)
myFriend = []
my_friends_length= 4
c=0

while c <= my_friends_length:
    add_friend = input("Enter the friend you want to add: ")

    if add_friend.isupper():
        print(f"Sorry, {add_friend} is not a valid name. Please enter a name with lowercase letters only.")
        continue
    elif add_friend.islower():
        add_friend = add_friend.capitalize()
        print(f"The first letter of the name {add_friend} has been capitalized.")
    myFriend.append(add_friend.strip())
    c +=1
    index = my_friends_length - c
    if index > 0:
        print(f"You have {index} more index left in your list.")
    elif index==0 :
        print("Your list is full.")
        print(myFriend)
        break
    

#================================================================
