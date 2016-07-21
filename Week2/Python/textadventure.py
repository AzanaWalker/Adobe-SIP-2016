start = '''
You wake up one morning and find that you arent in your bed you arent even in your room.
Youre in the middle of a giant maze.
A sign is hanging from the ivy You have one hour. Dont touch the walls.
There is a hallway to your right and to your left.
'''


print(start)


user_input = input("Type 'left' to go left or 'right' to go right.")
if user_input == "left":
    print("You decide to go left and you get attacked by a dementor ") 
    done = True
    print("Your soul has been sucked out by a dementor and now you are as dead as Sirius Black")
    user_input = input("BUT WAIT! You just realized that you are in the Little Hangleton graveyard, where Cedric Diggory was killed and his spririt offered another chance at life. Type 'come back to life' to come back to life or 'give up' to end your story here.")
    if user_input == 'come back to life':
    	print("Wise human you are. Choose a direction, 'up' or 'down' ")
    	if user_input == 'up':
    		print("Smart choice. You come across a ladder that leads you up and out of the maze and to safety. No more maze for you!")
    	elif user_input == 'down':
    		print("Baaaad choice buddy. You fall into a sinkhole filled with quicksand and fall through the hole to reach hell")
    		print('GAME OVER')
    elif user_input == 'give up':
    		print("Lazy one you are. Game Over ya coward")
elif user_input == "right":
	print("You choose to go right and you reach a fork in the road and come across a mountain troll")
	done = True
	user_input = input("Type 'ask him for help' or 'be independent and try to find your own way'")
	if user_input == "ask him for help":
		print("The troll directs you to a chest that contains a map instructing you how to get out of the maze and some money as a reward for choosing wisely")
		print("You use the map to get out of the maze and blow all the money on Golf Wang merch")

	elif user_input == "be independent and try to find your own way":
		user_input = input("Choose a direction, 'left' or 'right' ")
		if user_input == "left":
			print("You are now lost and end up starving to death because you are a silly human and forgot to charge your phone or bring a flare")
			print("THE END")
		elif user_input == "right":
			print("You run into a vine covered wall and realize that you now have to climb the wall to get out")
			user_input = input("Type 'climb' to climb or 'give up' to give up and accept your doomed fate")
			if user_input == "climb":
				print("You are a smart human and have finally made your way out")
				print("Be happy that you did not die in the maze. YAY!")
			elif user_input == "give up":
				print("YOU DED")

