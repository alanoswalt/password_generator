#This file
import string
import random

class generator:


    def __init__(self, ammount):
        self.ammount = ammount
        self.x=""
        self.y=0


    def gen_pass(self):
        
        
        while self.y < self.ammount:
            self.x += random.choice(string.ascii_letters)
            self.x +=str(random.randint(0,9))
            self.y +=1
        print(self.x)
        




new_generation = generator(15)

new_generation.gen_pass()


