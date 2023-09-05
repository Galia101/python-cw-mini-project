# write your code here
def padel_court_cost(court_types):
    if court_types=="indoor":
        return 30
    elif court_types=="outdoor":
        return 20

def rackets_cost(racket_brand):
    if racket_brand == "bullpadel":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "suix":
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes == "one":
        return 2
    elif ball_boxes == "two":
        return 3.5
    elif ball_boxes == "three":
        return 5
    
def padel_game_cost():
    court_type= input("your preferad courtype:")
    racket_brand= input("your prefered racket brand")
    ball_boxes= input(int("number of ball boxes you need:"))

    total_cost= padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return total_cost

padel_court_cost("court_type")
rackets_cost("rackets_cost")
padel_balls_cost("boll_boxes")
print("padel_game_cost")

court_type: ("indoor")
racket_brand:("nox")
ball_boxes: 2