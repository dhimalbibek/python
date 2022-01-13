player1 =input ("Select the options : ")
player2 =input ("Select the options : ")
possible_results = ["rock","scissors","paper"]

print =[f"{player1},{player2}"]

if player1 == player2 :
    print("game tied")
elif player1 == "rock" :
    if player2 == "scissors":
     print("Player1 win")
    else :
        print("Player2 win")
elif player1 == "paper" :
    if player2 == "rock":
        print("player2 win")
    else:
     print("Player1 win")

