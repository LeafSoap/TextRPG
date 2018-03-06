import random
from playerClass import *


class AI(Character):
    def update(self):
        """ Similar to Player.update(). """
        if self.currenthp < 1:  # Checks to see if the enemy is dead.
            self.death()
    def death(self):
        combatenemy.remove(self)  # Removes the enemy from the combatenemy list.


class Humanoid(AI):
    def __init__(self):
        super(Humanoid, self).__init__()
        self.name = "Peasant"
        self.maxhp = 15
        self.currenthp = self.maxhp
        self.maxmana = 10
        self.luck = 5
        self.strength = 2
        self.add_item(healthPotion())
    def update(self):
        if(self.currenthp < self.maxhp - 1):
            x = -1
            for i in self.inventory:
                x += 1
                if i.type == "potion":
                    if self.currenthp - i.points >= i.points:
                        self.inventory[x].use(self)
                    print("{0} used a {1}!".format(self.name, i.name))



class Bandit(Humanoid):
    def __init__(self):
        super(Bandit, self).__init__()
        self.strength = 2
        self.name = "Peasant"
        self.maxhp = 15
        self.add_item(leatherHat())
        self.add_item(leatherChest())
        self.add_item(leatherPants())


class Animal(AI):
    def attack(self, enemy):
        if self.currenthp > 0:
            combatroll = random.randint(1, 100)
            damage = int(self.strength/2)
            if combatroll < 80:
                print(str('&&& {0} attacked {1} for {2} points of damage with his right paw! &&&'
                          .format(self.name, enemy.name, damage)))
                enemy.currenthp -= damage
            else:
                print("{0} missed his right paw attack!".format(self.name,))
            combatroll = random.randint(1, 100)
            if combatroll < 80:
                print(str('&&& {0} attacked {1} for {2} points of damage with his left paw! &&&'
                          .format(self.name, enemy.name, damage)))
                enemy.currenthp -= damage
            else:
                print("{0} missed his left paw attack!".format(self.name,))
            if enemy.currenthp < 0:
                enemy.currenthp = 0
            time.sleep(0.5)
            print("========================================")
            print("{0}: {1}/{2}".format(enemy.name, enemy.currenthp, enemy.maxhp))
            print("========================================")

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.hasAI = True
        self.name = "Giant Rat"
        self.maxhp = 10
        self.currenthp = self.maxhp
        self.maxmana = 10
        self.luck = 1
        self.strength = 4

#
# Adding enemies to tier lists
#
#
tier1enemy = (Humanoid(),Humanoid())

tier2enemy = (Bandit())
tier1gold = random.randint(10, 20)
