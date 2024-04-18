#1
my_list=["E","Z","R",1,2,3]
my_tuple=("L","E","O")
my_data=[]

for data in zip(my_list, my_tuple):
    my_string=''.join(data)
    print(my_string,end='')

#================================================================
#2
print("=" * 40)

my_list1=["E","L","Z","E","R","O",1,2]
my_tuple1=("E","Z","R",1,2,"E","R","O")
my_list2=["L","E","O",1,2,"E","R","O"]
my_data=[]

for item1,item2,item3 in zip(my_list1,my_tuple1,my_list2):
    if item1==item2==item3:
        my_data.append(item1)

print(my_data)
final_string=''.join(str(elem) for elem in my_data)

print(final_string) 

#================================================================
#4
print("=" * 40)

def say_hello_to(name):  
    '''this function to say hello to {name}'''    
    return f"Say hello to {name}"  

print(say_hello_to('Ahmed'))
print(say_hello_to.__doc__)

#5
print("-"*30)

my_friends =["Ahmed","Mohamed","Saadawy"]


def say_hello(somepeople):
    '''this function to say hello to anyone'''    
    for some in somepeople:
        print(f"hello ${some}")
        
say_hello(my_friends) 
# say_hello(my_friends.__doc__) 
print(say_hello.__doc__)