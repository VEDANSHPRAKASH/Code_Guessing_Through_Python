import random

def getDigits(num): 
    return [int(i) for i in str(num)]

def noDuplicates(num): 
    num_li = getDigits(num) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False
    
def generateNum(): 
    while True: 
        num = random.randint(1000,9999) 
        if noDuplicates(num): 
            return num 
        
def numOfBullsCows(num,guess): 
    em_wp = [0,0] 
    num_li = getDigits(num) 
    guess_li = getDigits(guess) 
      
    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i: 
                em_wp[0] += 1
            else: 
                em_wp[1] += 1
    
    return em_wp 

num = generateNum() 
tries =int(input('Enter number of tries: ')) 

while tries > 0: 
    guess = int(input("Enter your guess: ")) 
      
    if not noDuplicates(guess): 
        print("Number should not have repeated digits. Try again.") 
        continue
    if guess < 1000 or guess > 9999: 
        print("Enter 4 digit number only. Try again.") 
        continue
      
    em_wp = numOfBullsCows(num,guess) 
    print(f"{em_wp[0]} exact match of digit, {em_wp[1]} digit match but in wrong position") 
    tries -=1
      
    if em_wp[0] == 4: 
        print("You guessed right!") 
        break
else: 
    print(f"You ran out of tries. Number was {num}")
