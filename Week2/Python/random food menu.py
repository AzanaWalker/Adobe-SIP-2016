import random
flavor_feel = ["creamy.", "thick", "spicy", "mild", "fiery",
               "moist", "chunky", "moldy", "spoiled", "crumbly"]
food_type = [" sweet and sour", " alfredo", " country-style", " barbeque", " smothered",
             " asian-style", " refried", " blanched", " boiled","  baked"]
food = [" chicken", " beef", " beans with rice", " chicken with rice", " lamb",
        " turkey", " tofu", " noodles", " spaghetti", " mashed potatoes with gravy"]
food_adjective = len(flavor_feel)
type_food = len(food_type)
enter_mouth = len(food)

#random_adjective = random.randint(0, len(flavor_feel)-1)
#type_food = random.randint(0,len(food_type)-1)
#enter_mouth = random.randint(0,len(food)-1)

#print(food_type[random_type])


for i in range(10):
    food_adjective = random.randint(0,len(flavor_feel)-1)
    type_food = random.randint(0,len(food_type)-1)
    enter_mouth = random.randint(0,len(food)-1)
    
    print(flavor_feel[food_adjective] + food_type[type_food] + food[enter_mouth])

    del flavor_feel[food_adjective]
    del food_type[type_food]
    del food[enter_mouth]
