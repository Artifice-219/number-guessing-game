import random

def determine_winner(user, computer):
    # if player is correct return 1 
    if(user == computer):
        print('You guessed right')
        return 1
    # player is incorrect and choice is "high" 
    # return 0
    elif(user != computer and user > computer):
        print('Oops !, you guessed high')
        return -1
    # player is incorrect and choice is "low" 
    # return 0
    elif(user != computer and user < computer):
        print('Oops !, too low')
        return -1

def generate_rand():
    return random.randint(0,10)
        
        
# im still uncomfortable with how pythons define a block of code
# that is why i make this to mark where i make funtionc
# and where the main "code" start

   
player_life = 3
score = 0

print("Can you what number im thinking right now ?? ")

while(True):
    # initializations made here will be resetted each run of the iteration

    computer_choice = generate_rand()
    user_choice = int(input('Enter youre choice '))

    result = determine_winner(user_choice, computer_choice);

    # if the result is correct increment the player_score
    if(result == 1):
        score += 1
    elif(score == 0):
        print(f'Computer choice {computer_choice}')
        player_life += result
    
        
    print(f'Player score {score} | Player life {player_life}')

    if(player_life == 0 or score == 3):
        choice = str(input(('Would you like to play again [ y/n ]')))
        
        # program termination
        if(choice == 'n' or choice == 'N'):
            break