from random import shuffle

#Function to shuffle the List 
def shuffle_list(mylist):
    # Take in list, and return shuffled version
    shuffle(mylist)
    
    return mylist
#Function to take player's input
def player_guess():
    
    guess = ''
    while guess not in ['0','1','2','3']:
        guess = input("Pick a Valid number ")
        
    return int(guess)
#Function to check the player's guess is correct or not
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong Guess! Try Again')
        guess = player_guess()
        check_guess(mylist,guess)
        

#Initial List 
mylist=['','O','','']
         
#Shuffle the List 
shuffled_list=shuffle_list(mylist)
#Get User's Guess
guess = player_guess()
#Check User's Guess 
check_guess(mylist,guess)
