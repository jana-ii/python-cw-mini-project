# write your code here
def padel_court_cost(court_type):
    if court_type == ('indoor'):
        return 30
    elif court_type ==('outdoor'):
        return 20
    else:
        return False



def rackets_cost(racket_brand):
    if racket_brand == ('bullpadel'):
        return 100
    elif racket_brand == ('nox'):
        return 140
    elif racket_brand == ('siux'):
        return 200
    else :
        print('we dont have that')
    



def padel_ball_cost(ball_box):
    if ball_box == 1:
        return 2
    elif ball_box == 2:
        return 3.5
    elif ball_box == 3:
        return 5 
    else :
        return 

    
def padel_game_cost():
    court_type = input('what court do u want? indoor or outdoor ')
    racket_brand = input('what racket do u want? bullpadel or nox or siux ')
    ball_box = int(input('how many ball boxes do you want 1,2 or 3? '))
    return padel_ball_cost(ball_box) + rackets_cost(racket_brand) + padel_court_cost(court_type)

print (padel_game_cost())

