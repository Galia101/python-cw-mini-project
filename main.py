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
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    
def padel_game_cost():
    court_type= input("Enter cour type: ")
    racket_brand= input("Enter racket brand: ")
    ball_boxes= input(int("Enter number of ball boxes: "))

    total_cost= padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return total_cost

print(f"total cost{padel_game_cost()}")
