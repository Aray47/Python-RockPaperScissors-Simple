import random
import time
import sys


userscore = 0
compscore = 0
winscore = 0

move = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']

print("**Welcome to Rock, Paper, Slammmers**")
print("Best of 3, 5, or 7?")
winscore = int(input())

while True:
	print("\nYou: ",userscore, "| Me:",compscore, "out of ",winscore)
	player_move = input("r = Rock, p = Paper, s = Scissors. \nYour move: ").capitalize()
	computer_move = random.choice(move)

	print("Rock....")
	time.sleep(1)
	print("Paper...")
	time.sleep(1)
	print("Scissors...")
	time.sleep(1)
	print("Shoot!\n")
	time.sleep(.5)
	print("You: ", player_move)
	print("Me: ", computer_move)

	if player_move == computer_move:
		print("Tie")
	elif player_move + computer_move in player_wins:
		userscore = userscore + 1
		print("You win!")
	else:
		compscore = compscore + 1
		print("You lose!")

	if userscore == winscore:
		print("You defeated me")
		quit()
	if compscore == winscore:
		print("Get rekt, bud")
		quit()




