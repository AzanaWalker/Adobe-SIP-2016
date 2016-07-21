number = 420
guess = input("Guess my lucky number!")

while number != int(guess):
	if number < int(guess):
		print("Whoops! Guessed a little high there")
		guess = input("try again")
	elif number > int(guess):
		print("Yikes! Your guess is too low now")
		guess = input("try again ")

if number == int(guess):
		print("It's your lucky day!")
		print("Game Over!")