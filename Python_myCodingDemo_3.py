# a game of Rock Paper Scissors
# a working program that accepts the user's input (r, p, or s)

# user 1
while True:
    while True:
        p1 = input("Player 1, Enter Rock(r), Paper(p), or Scissors(s): ")
        if p1 in ["r","p","s"]:
            break
        print("Please enter a valid input")

# user 2
    while True:
        p2 = input("Player 2, Enter Rock(r), Paper(p), or Scissors(s): ")
        if p2 in ["r","p","s"]:
            break
        print("Please enter a valid input")

    if((p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == "p") or (p1 == 'p' and p2 == "r")):
        print("Player 1 Wins!")
    elif ((p2 == 'r' and p1 == 's') or (p2 == 's' and p1 == "p") or (p2 == 'p' and p1 == "r")):
        print("Player 2 Wins!")
    else:
        print("It's a Tie!")
    
# the game runs once    
    again = input("play again (y/n)? ")
    if again == "n": 
        print("Bye!")
        break
