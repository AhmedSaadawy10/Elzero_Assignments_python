#1
value=(0,1,2)

if any(value):#there is value = true so i will continue
    my_var=0 
    
my_list=[ True,1,1,['A','B'],10,5,my_var]

if all(my_list[:4] or all(my_list[:6]) or all(my_list[:])):
    print("Good")  
else:
    print("Bad")   

#the result => 'Good'    

#================================================================
#2
print("=" * 40)

v=9
my_range=list(range(v))
print((sum(int(my_range)+v)) + pow(v,v,v))
#================================================================
#3
print("_" * 40)

n=20
l=list(range(n))

if round(sum(l)/n)==max(0,3,10,2,-100,-23,9):
    print("Good")
else:
    print("Bad")


#================================================================
#4
print("=" *40)
#4
print("_" * 40)

#my_all functions
def my_all(*num):
    
    if all(num):
        return True
    else:
        return False
        # print("All values must be true")

# my_any function
def my_any(*num):
    if any(num):
        return True
    else:
        return False
        # print("at least one value must be true") 
        
        
#my min_function
def my_min(*num) :
    for i in (num):
        return min(i)

#my max_function
def my_max(*num) :
    for i in (num):
        return max(i)

list_m=[1,2,3,4,5,6,7,8]  
        
print(my_all(1,1,True,['a','b']))
print(my_all(1,1,True,0))

print(my_any('',[],False,0))
print(my_any('A',[1],True,0))

print(my_min(list_m))
print(my_max(list_m))
