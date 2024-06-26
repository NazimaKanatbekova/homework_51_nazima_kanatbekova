from django.db import models
import random


# Create your models here.
class Cat:
    HAPPY_CAT_AVATAR = 'images/happy_cat.png'
    CAT_AVATAR = 'images/cat.png'
    SAD_CAT_AVATAR = 'images/sad_cat.png'

    def __init__(self, name, age=1, hunger=40, happiness=40):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happiness = happiness

    def feed(self):
        if self.happiness > 0:
            if self.hunger > 100:
                self.happiness -= 30
            else:
                self.hunger += 15
                self.happiness += 5

        self._check_limits()

    def play(self):
        if self.happiness > 0:
            if self.hunger > 100:
                self.happiness -= 5
            else:
                self.hunger -= 10
                self.happiness += 15
                if random.randint(1, 3) == 1:
                    self.happiness = 0

        self._check_limits()

    def sleep(self):
        self.happiness = 0
        self._check_limits()


    def _check_limits(self):
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 100:
            self.happiness = 100


    def get_avatar(self):
        if self.happiness >= 70:
            return self.HAPPY_CAT_AVATAR
        elif self.happiness >= 30:
            return self.CAT_AVATAR
        else:
            return self.SAD_CAT_AVATAR

