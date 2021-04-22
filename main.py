import time
import random
# guessing Game
# RPS
# Dice Roll
# Fortune Teller

def guessingGame():
	#print("This is the guessing game")
	cpu = random.randint(1,10)
	user = int(input("Guess what number I'm thinking of: "))
	while (cpu != user):
		user = int(input("Try again: "))

	print("You guessed it!")

def RPS():
	#print("This is rock paper scissors")
	print("1 = Rock, 2 = Paper, 3 = Scissors")
	cpu = random.randint(1,3)
	user = int(input("Pick a weapon: "))
	if(cpu == '1'):
		if(user == '1'):
			print("Tie")
		elif(user == '2'):
			print("You Won")
		elif(user == '3'):
			print("You Lost")
	elif(cpu == '2'):
		if(user == '1'):
			print("You lost")
		elif(user == '2'):
			print("Tie")
		elif(user == '3'):
			print("You Win")
	elif(cpu == '3'):
		if(user == '1'):
			print("You won")
		elif(user == '2'):
			print("You lost")
		elif(user == '3'):
			print("Tie")

def diceRoll():
	#print("This is the dice roll")
	print(random.randint(1,6))

def fortuneTeller():
	#print("This is the fortune teller")
	fortunelist = ["You will win the lottery","You will eat a rotten meal","Your hater will come to see you tomorrow","A sock will talk to you.","Go buy some clothes..."]
	print(fortunelist[random.randint(0,len(fortunelist)-1)])

# 'main' function
# this is where we define how we our program to run

def main():
	#print("This is the main function")

	# Tell the user their game options
	# Ask the user to choose ope
	# Call the correct function based on user input
	print("GAMEBOX OPTIONS: Guessing Game, Rock/Paper/Scissors, Dice Roll, Fortune Teller")
	print("GuessingGame = GG, Rock/Paper/Scissors = RPS, Dice Roll = DR, Fortune Teller = FT")
	userPick = input("Pick a game to play: ")

	if(userPick == 'GG'):
		guessingGame()
	elif(userPick ==  'RPS'):
	 RPS()
	elif(userPick == 'DR'):
		diceRoll()
	elif(userPick == 'FT'):
		fortuneTeller()
	else:
		print("Sorry that was an invaild input")
		print()
		main()

# This controls the execution of our code
if __name__ == "__main__":
	main()