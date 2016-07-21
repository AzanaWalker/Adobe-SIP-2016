class Dog():

        #Constructor function
        def __init__(self, furColor, weight, eyeColor, name):
                self.furColor = furColor
                self.weight = weight
                self.eyeColor = eyeColor
                self.name = name

            #function
        def bark(self):
                print("Woof")
        def wag(self):
                print("Wagging Tail")
        def run(self):
                print("Your dog is running away")


Toto = Dog("Brown", 25, "Blue", "Toto")
(Toto.run)



