from distutils.log import error
import random

def play():
    user = input("what is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()
    
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Tie".format(user,computer)
        user = input("what is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")


    # r > s, s > p, p > r
    if is_win(user,computer):
        return "Player{}:CPU{}. You won!".format(user,computer)
    return "Player{}:CPU{}. You lost.".format(user,computer)

def is_win(player,computer):
    # return true if player beats computer
    #winning conditions:# r > s, s > p, p > r

    if(player == 'r' and computer =='s') or (player == 's' and computer =='p') or (player =='p' and computer =='r'):
      return True
    return False

if __name__ == '__main__':
    print(play())
    




    
        

