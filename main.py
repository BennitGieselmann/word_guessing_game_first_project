
# in the beginning, the programm tells player one, what to do
print("_________________________________________________________________________________________________________________")
print("welcome to the word guessing game!")
input("press enter to start!")
print("_________________________________________________________________________________________________________________")
print("You are Player one, please think of a word with five letters, press after every letter enter, have fun!")
print("_________________________________________________________________________________________________________________")
# now player one can choose the word
player1_letter1 = str(input("please enter the first letter: "))
player1_letter2 = str(input("please enter the second letter: "))
player1_letter3 = str(input("please enter the third letter: "))
player1_letter4 = str(input("please enter the fourth letter: "))
player1_letter5 = str(input("please enter the fifth letter: "))
print("_________________________________________________________________________________________________________________")
# here it shows player one the word that was choosen
print("your word is: " + player1_letter1 + player1_letter2 + player1_letter3 + player1_letter4 + player1_letter5)
print("_________________________________________________________________________________________________________________")
# now it asks if player one want to continue, if not player one can choose the word again as many times as player one wants
p1yess = int(input("Do you want to continue? Type [1] for 'yes' or [2] for 'no': "))
print("_________________________________________________________________________________________________________________")
while p1yess > 1:
    player1_letter1 = str(input("please enter the first letter: "))
    player1_letter2 = str(input("please enter the second letter: "))
    player1_letter3 = str(input("please enter the third letter: "))
    player1_letter4 = str(input("please enter the fourth letter: "))
    player1_letter5 = str(input("please enter the fifth letter: "))
    print("your word is: " + player1_letter1 + player1_letter2 + player1_letter3 + player1_letter4 + player1_letter5)
    print("_________________________________________________________________________________________________________________")
    p1yess = int(input("Do you want to continue? Type [1] for 'yes' or [2] for 'no': "))
    print("_________________________________________________________________________________________________________________")

# after player one pressed enter, the programm scroll 15 lines down and it's the turn of player two
input("please press 'enter' ")
count_1 = 1
while count_1 < 15:
    print(" ")
    count_1 = count_1 + 1
print("_________________________________________________________________________________________________________________")
print("you are the second player, try to guess player one's word letter by letter, press enter after every letter, have fun!")
input("press enter to start!")
print("_________________________________________________________________________________________________________________")
# now its time for the second player to guess the word
player2_letter1 = str(input("please enter your first out of five letters: "))
player2_letter2 = str(input("please enter your second out of five letters: "))
player2_letter3 = str(input("please enter your third out of five letters: "))
player2_letter4 = str(input("please enter your fourth out of five letters: "))
player2_letter5 = str(input("please enter your fifth out of five letters: "))
print("_________________________________________________________________________________________________________________")
print("your word is: "+ player2_letter1 + player2_letter2 + player2_letter3 + player2_letter4 + player2_letter5)
print("_________________________________________________________________________________________________________________")
# now it asks if player two want to continue, if not player two can choose the word again as many times as player two wants,for example player two can ask player one for tips
p2yess = int(input("Do you want to continue? Type [1] for 'yes' or [2] for 'no': "))
print("_________________________________________________________________________________________________________________")
while p2yess > 1:
    player2_letter1 = str(input("please enter your first out of five letters: "))
    player2_letter2 = str(input("please enter your second out of five letters: "))
    player2_letter3 = str(input("please enter your third out of five letters: "))
    player2_letter4 = str(input("please enter your fourth out of five letters: "))
    player2_letter5 = str(input("please enter your fifth out of five letters: "))
    print("_________________________________________________________________________________________________________________")
    print("your word is: " + player2_letter1 + player2_letter2 + player2_letter3 + player2_letter4 + player2_letter5)
    print("_________________________________________________________________________________________________________________")
    p2yess = int(input("Do you want to continue? Type [1] for 'yes' or [2] for 'no': "))
    print("_________________________________________________________________________________________________________________")
#now the programm compares the letters of player two with those of player one
if player1_letter1 == player2_letter1:
    print("letter one was correct!")
else:
    print("letter 1 was incorrect!")
if player1_letter2 == player2_letter2:
    print("letter one was correct!")
else:
    print("letter 2 was incorrect!")
if player1_letter3 == player2_letter3:
    print("letter one was correct!")
else:
    print("letter 3 was incorrect!")
if player1_letter4 == player2_letter4:
    print("letter one was correct!")
else:
    print("letter 4 was incorrect!")
if player1_letter5 == player2_letter5:
    print("letter one was correct!")
else:
    print("letter 5 was incorrect")
print("_________________________________________________________________________________________________________________")
# if all the letters are the same, player two wins
if player1_letter1 == player2_letter1 and player1_letter2 == player2_letter2 and player1_letter3 == player2_letter3 and player1_letter4 == player2_letter4 and player1_letter5 == player2_letter5:
    print("congrats! The word was " + player1_letter1 + player1_letter2 + player1_letter3 + player1_letter4 + player1_letter5 + "!")
    print("_________________________________________________________________________________________________________________")
    print("you have won the game!")
    print("_________________________________________________________________________________________________________________")
    input("press 'enter' to close the game!")
    print("_________________________________________________________________________________________________________________")
    quit("see you next time!")
    print("_________________________________________________________________________________________________________________")
# if all the letters are not the same, player two loses
else:
    print("sorry you have lost the game the word was " + player1_letter1 + player1_letter2 + player1_letter3 + player1_letter4 + player1_letter5)
    print("_________________________________________________________________________________________________________________")
    input("press 'enter' to close the programm ")
    print("_________________________________________________________________________________________________________________")
    quit("see you next time!")
    print("_________________________________________________________________________________________________________________")






