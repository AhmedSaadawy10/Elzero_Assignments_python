#1
def calculate(num1,num2,operation):
    
# add operation 
    if str(operation).lower() in ('add','a'):
        return num1 + num2

    # subtract operation 
    elif str(operation).lower() in ('subtract','s'):
        return num1 - num2
    
    # multiply operation 
    elif str(operation).lower() in ('multiply','m'):
        return num1 * num2 
    
    else:
        print("Invalid operation")
    
#print add operation     
print("add result".center(30,"="))     
print(f" the result of operator = {calculate(20,10,'ADd')}")  
print(f" the result of operator = {calculate(20,10,'A')}")
#print subtract operation     
print("subtract result".center(30,"="))     
print(f" the result of operator = {calculate(20,10,'s')}")  
print(f" the result of operator = {calculate(20,10,'suBtract')}") 
#print multiply operation     
print("multiply result".center(30,"="))     
print(f" the result of operator = {calculate(20,10,'M')}")  
print(f" the result of operator = {calculate(20,10,'Multiply')}") 

#================================================================
#2
print("_" * 40)

def addition(*nums):
    addresult=0
    
    for i in nums:
        
        if i==10:
            continue
        
        elif i==5:
            addresult -=5
            
        else:    
            addresult +=i
    
    print(f"the result of operator = {addresult}")
        
addition(10,30,40,6,5) 

#================================================================
#3
print("_" * 40)

def show_skills(name,*skills):

        if skills:
            print(f"Hello {name} your skills are : ")

            for sk in skills:
                print(f"-{sk}")

        else:    
            print(f"Hello {name} you don't have any skills")
            
show_skills("Ahmed","Html","Css","Python","Js")     
show_skills("mohamed") 

#================================================================
#4
print("_" * 40)   

def say_hello(name,age="Unknown",country="Unknown Country"):
    print(f"Hello {name} your age is {age} and you live in {country} !")
    
say_hello("Ahmed")    
say_hello("Mohamed","20","Egypt")