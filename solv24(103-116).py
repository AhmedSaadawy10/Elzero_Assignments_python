#1
class game:
    def __init__(self,game_name,developer,release_data,price):
        #Instance Attribute
        self.game_name = game_name
        self.developer = developer
        self.release_data = release_data
        self.price = price
        
    #create function to get the game info    
    def game_info(self):
        return f"Game name is {self.game_name}, Developer is {self.developer},Release data in {self.release_data} and price in Egypt is {self.price} Egyption pounds"
    
#create instance
game_1=game("Snake","Python",2010,2500)

#to print the instance
print(game_1.game_info())

#================================================================
#2
print("=" * 40)

class user:
    def __init__(self,f_name,m_name,age,gender):
        self.f_name = f_name
        self.m_name = m_name
        self.age = age
        self.gender = gender
        
    def get_full_info(self):
        if self.gender=='male' and self.age < 40:
            return f"Hello Mr.{self.f_name} {self.m_name:.1s}. {[40-int(self.age)]} years to reach 40 "    
        elif self.gender=='female' and self.age < 40:
            return f"Hello Miss.{self.f_name} {self.m_name:.1s}. {[40-int(self.age)]} years to reach 40 " 
        else:  
            return f"Hello {self.f_name},sure that you enter your gender(male or female) and your age is less than 40 " 
        
#create instance users
user_1=user("Ahmed","Mohmed",30,"male")        
user_2=user("Mona","Ahmed",50,"female")        

#print users
print(user_1.get_full_info())       
print(user_2.get_full_info())   

#================================================================
#3
print("-"* 30)

class message:
    #Attribute class
    #static method
    def print_message():
        return "Hello from class message"
    def __init__(self):
        pass
    
# to print anything between the class and def __init__(self):
print(message.print_message())    

#________________

#================================================================
#4
print("-"* 30)
class Games:
    @staticmethod
    def show_games(games):
        if type(games) == str:
            return f"I Have One Game Called \"{games}\""
        elif type(games) == list:
            if len(games) == 1:
                return "I Have One Game:\n-- " + "\n-- ".join(games)
            else:
                return "I Have Many Games:\n-- " + "\n-- ".join(games)
        elif type(games) == int:
            if games == 1:
                return "I Have 1 Game."
            else:
                return f"I Have {games} Games."

my_game = "Shadow Of Mordor"
my_games_names = ["Ys II", "Ys Oath In Felghana", "YS Origin"]
my_games_count = 80

print(Games.show_games(my_game))
print(Games.show_games(my_games_names))
print(Games.show_games(my_games_count))

#================================================================
#5
print("=" * 40)


class Members:

    def __init__(self,n,p):
        self.name =n
        self.permission =p

    def show_info(self):
            return f"your name is {self.name} and your permission is {self.permission}"

class Admin(Members):
    def __init__(self,n,p):
        super().__init__(n,p)# using super() way to inherit

class Moderator(Admin):
    def __init__(self,n,p):
        Members.__init__(self,n,p)# using class way to inherit 

member_1=Admin("Ahmed","Admin")
member_2=Moderator("fosha","Moderator")

print(member_1.show_info())
print(member_2.show_info())

#================================================================
#6
print("=" * 40)


class A:
    def __init__(self,one):
        self.one=one
        
class B:
    def __init__(self,two):
        self.two=two
        
class C:
    def __init__(self,three):
        self.three=three
        
class Text(A,B,C):
    def __init__(self,one,two,three):
        super().__init__(one) 
        #لانه هنا بيورث اتنين براميتر من اول كلاس ةهة 
        #inerit from A class first ,so it takes (self,one) only ,so we must instantiate another parameters 
        self.two=two
        self.three=three
    
    def show_name(self):     
        return self.one+self.two+self.three                     
        
the_name=Text("El","ze","ro")

# print(Text.mro())
print(the_name.show_name())