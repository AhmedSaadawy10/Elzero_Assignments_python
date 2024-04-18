#1
my_string="hello"    

def reverse_string(my_string):
    yield my_string
    
my_iterator = iter(reversed(my_string))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# for item in my_iterator:
#     print(item)
    
#________________________________________________________________
#2
print("-"*30)

def my_decorator(func) :#my decorator
    
    def add_sugar():# name just for decorator
        print("Sugar added from decorator")
        func()#excute function
        print("#"*30)
    return add_sugar   


@my_decorator#sugar sentax
def create_tea():
    print("Tea created")

@my_decorator#sugar sentax   
def create_caffe():
    print("caffe created")    
    

create_tea()
create_caffe()    