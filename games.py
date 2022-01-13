choice1 =input("Enter your choice 'scissors','paper','rock': ?")
choice2 =input("Enter your choice 'scissors','paper','rock': ?")
# choice =input("Enter your choice 'scissors','paper','rock': ?")
total =[f"{choice1},{choice2}"]
if choice1 ==choice2 :
    print("The game is tied")
elif choice1 =="rock":
    if choice2 == "paper":
      print("Paper win ")
# else:
#     print("Rock win")

if choice1 =="rock" :
    if choice2 =="scissors":
        print("ROCK wins")

if choice1 =="scissors":
    if choice2 =="paper" :
        print("Scissors win")

if choice1 =="scissors" :
    if choice2 =="rock":
        print("Rock win")

  

