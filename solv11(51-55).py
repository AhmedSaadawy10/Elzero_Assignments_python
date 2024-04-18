#1
my_nums = [15,81,5,17,20,21,13]
index =0
for num in sorted(my_nums, reverse=True):
    if num % 5==0:
        index +=1
        print(f"{index}=> {num}")

#================================================================
#2
print("_" * 40)

for i in range(1,21):
    
    if i == 6 or i ==9 or i ==12:
        continue
    print(str( i ).zfill(2))
    
#================================================================
#3
print("=" * 40)
my_rank={
    "Math":"A",
    "Science":"B",
    "Drawing":"A",
    "Sports":"C",
} 
degrees={
    "A":100,
    "B":70,
    "C":50
} 

totaldegree=0

for main_key,main_value in my_rank.items():
    
    degree = degrees[main_value]
    totaldegree += degree
    
    print(f"My rank in {main_key} And this is equal {degree} points")

print(f"total points= {totaldegree}")    

#================================================================
#4

print("_" * 40)

students={
    "Ahmed":{
        "Math":"A",
        "Science":"D",
        "Draw":"B",
        "Sports":"C",
        "Thinking":"D"
    },
    
    "Sayed":{
        "Math":"B",
        "Science":"B",
        "Draw":"B",
        "Sports":"D",
        "Thinking":"A"
    },
    
    "Mahmoud":{
        "Math":"D",
        "Science":"A",
        "Draw":"A",
        "Sports":"B",
        "Thinking":"B"
    }
    
    
}

grades={
    "A":100,
    "B":80,
    "C":70,
    "D":50
}

#first solution with nested for loop without .item()

# for student in students :
    
#     total=0
    
#     print("-" * 30)
#     print("--- Student Name: =>" + student +" ---")
#     print("-" * 30)
    
#     for subjects in students[student]:
        
#         for grade in students[student][subjects]:
#             points=grades[grade]
#             total += points
#         print(f"-{subjects}=> {points} points")
        
#     print(f"Total points for students is : {total}")  


#secoond solution with nested for loop with.item()
for student , subjects in students.items() :
    
    total=0
    
    print("-" * 30)
    print(f"-- Student Name : {student} --")
    print("-" * 30)
    
    for subject , grade in subjects.items():
        
        points = grades[grade]
        total += points
        
        print(f"-{subject} => {points}")
    
    print(f"Total points for students grade is {total}")    