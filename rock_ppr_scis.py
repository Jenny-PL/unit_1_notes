# code to practice debugging with!

def winner(player_1, player_2):
    if not (player_1.isalpha() and player_2.isalpha()):
        return None
    player_1 = player_1.lower()
    player_2 = player_1.lower()
    
    # set of options
    options = {'rock', 'paper', 'scissors'}
    
    if player_1 not in options or player_2 not in options:
        return None
    
    if player_1 == player_2:
        return "It's a tie!"
        
    if player_1 == "rock":
        if player_2 == "paper":
            return "Player 2 wins!"
        else:
            return "Player 1 wins!"
            
    elif player_1 == "paper":
        if player_2 == "scissors":
            return "Player 2 wins!"
        else:
            return "Player 1 wins"
            
    elif player_1 == "scissors":
        if player_2 == "paper":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

answer = winner('rock', 'paper')
print(answer)