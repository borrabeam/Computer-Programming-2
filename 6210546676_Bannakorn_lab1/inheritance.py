class Pet:
    def __init__(self,name,owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self,thing):
        print(self.name + " ate a" + str(thing) + "!")
    
    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        print(self.name + " says woof!")

class Cat(Pet):
    def __init__(self,name,owner,lives=9):
        super().__init__(name,owner)
        self.lives = lives

    def talk(self):

        print(self.name + ' says meow! ')
    
    def lose_life(self): 
#  """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'   becomes False. 
#  If this is called after lives has reached zero, print   out that the cat has no more lives to lose."""
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print('The cat has no more lives to lose. ')


class NoisyCat(Cat):  
#  """A Cat that repeats things twice."""  
# """Talks twice as much as a regular cat."""   # fill me in  

    def talk(self): 
        super().talk
        super().talk


