#1
def get_score(**kwargs):
    for subject, score in kwargs.items():
        print(f"{subject} => {score}")
        

# get_score(math=80, js=60, html=90)

#================================================================
#2
print("=" * 40)

def get_people_score(*name,**scores):
    if name:
        name = name[0]
        print(f"Hello {name} this is your score table:")
    
    if scores:
        index=0
        for sub, score in scores.items():
            index += 1
            print(f"{index}-{sub} => {score}")
    else:
        print(f"Hello {name} You Have not any scores")

get_people_score("ahmed", Math=30, js=40, html=70)
print("=" * 40)
get_people_score(Math=30, js=40, html=70)
print("=" * 40)
get_people_score("Saadawy")

#================================================================
#3
print("=" * 40)


score_list={
    "Math":"90",
    "Science":"80",
    "language":"100"
    
}   

get_people_score("Omar",**score_list)