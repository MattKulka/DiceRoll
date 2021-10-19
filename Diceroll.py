import random 
while True:     
     print(''' 1. roll the dice             2. quit    ''')    
     user = int(input("What would you like to do? \n"))     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     else:         
        break
