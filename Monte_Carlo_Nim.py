class nimgame:
    def __init__(self,stack,player1,player2,show = True):
        self.players = {1:player1,2:player2}
        self.stack = stack
        self.show = show
    def runmatch(self):
        player_ind = 1
        player = self.players[player_ind]
        while self.stack != 0:
            move = player.move(self.stack)
            self.stack -= move
            if self.show == True:
                print(player_ind,move,self.stack)
            player_ind = 3 - player_ind
            player = self.players[player_ind]
        #once the stack reaches 0, that player must've taken the last one. So, since we already switched, switch again
        return 3 - player_ind

def valid_moves(stack):
    if stack <= 0:
        print('error')
    if stack == 1:
        return [1]
    if stack == 2:
        return [1,2]
    return [1,2,3]

import random
class randomplayer:
    def __init__(self):
        pass
    def move(self,stack):
        moves = valid_moves(stack)
        return random.choice(moves)

class human:
    def __init__(self):
        pass
    def move(self,stack):
        moves = valid_moves(stack)
        move_made = int(input())
        return move_made
    
class MonteCarloplayer:
    def __init__(self):
        pass
    def move(self,stack):
        moves  = valid_moves(stack)
        best_move = 1
        most_wins = 0
        for i in moves:
            current_wins = 0
            k = 0
            while k < 100:
                dummy_plug = randomplayer()
                dummy_plug2 = randomplayer()
                match = nimgame(stack - i, dummy_plug,dummy_plug2,False)
                if match.runmatch() == 2:
                    current_wins += 1
                k += 1
            if current_wins > most_wins:
                most_wins = current_wins
                best_move = i
        return best_move
                    
                       
class Perfectplayer:
    def __init__(self):
        pass
    def move(self,stack):
        if stack == 1 or stack == 2 or stack == 3:
            return stack
        if stack % 4 != 0:
            return stack % 4
        return random.choice([1,2,3])
    