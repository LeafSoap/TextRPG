import sys
import random
import time
from enemyClass import *
from itemClass import *


# Using a global variable to track the amount of players in the game.
# This variable will be changed within the character_creation() function.
number_of_players = 0
combatenemy = []


class Character:
    """ Class used to track the player."""
    def __init__(self):
        """ Constructs an object using the stats from character_creation()"""
        # Attributes from character creation:
        # Each player object will have their own unique 'identifier' attribute. This identifier will be 1 for Player 1,
        # 2 for Player 2, etc. This will allow easier multi-player support.
        self.identifier = 0
        self.name = "NULL"
        self.maxhp = 5
        self.maxmana = 0
        self.luck = 0
        # Attributes generated using the ones above:
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        # Experience/Level attributes:
        self.level = self.maxhp + self.maxmana + self.luck - 24
        self.neededexp = 0
        self.currentexp = 0
        # Inventory/Gold attributes:
        self.inventory = []
        weaponPower = 0
        self.gold = 0
        self.hasAI = False
        # Entity's attack and armor values:
        self.basePower = 1
        self.atk = self.basePower
        self.armor = 0
        # Entity's equipment:
        # The list will have 4 objects.
        # 0 - Head
        # 1 - Chest
        # 2 - Legs
        # 3 - Weapon
        self.equipment = [leatherPants(),  # Filling the Entity's equipment slots with
                          leatherChest(),  # an 'empty' item, known as item_null.
                          leatherHat()]

    def view_stats(self):
        print('==========')
        print('Name:   {0}'.format(self.name))
        print('Level:  {0}'.format(self.level))
        print('Exp:    {0}/{1}'.format(self.currentexp, self.neededexp))
        print('HP:     {0}/{1}'.format(self.currenthp, self.maxhp))
        print('Mana:   {0}/{1}'.format(self.currentmana, self.maxmana))
        print('Luck:   {0}'.format(self.luck))
        print('Armor:  {0}'.format(self.armor))
        print('Attack: {0}'.format(self.atk))
        print('==========')

    def update(self):
        #if we have armor and weapons, apply their attributes
        self.armor = 1
        self.atk = self.basePower
        for i in self.equipment:
            if i.type == "armor":
                self.armor += i.armorValue
            if i.type == "weapon":
                self.atk += i.power
        """ Method used to check and player_update player status."""
        #Death checks and overflow checks that will be universal
        if self.currentexp >= self.neededexp:  # Check to see if player has enough exp to level up.
            self.lvlup()
        if self.currenthp <= 0:  # Check to see if player is dead.
            self.death()
        if self.currenthp > self.maxhp:  # Check if player has more HP than maximum
            self.currenthp = self.maxhp
        if self.currentmana > self.maxmana:  # Check if player has more Mana than maximum
            self.currentmana = self.maxmana

    def lvlup(self):
        """ Method used if player_update() detects enough experience to level up. """
        self.currentexp -= self.neededexp
        self.neededexp += 10
        self.level += 1
        print('-*-*-*You have gained a level!*-*-*-\n')
        while True:
            try:
                spendpoint = input("Would you like to increase HP, Mana, or Luck?"
                                   "('hp', 'mana', 'luck'.\n")
                if spendpoint == 'hp':
                    self.maxhp += 1
                    print('You now have {0} HP!'.format(self.maxhp))
                    break
                elif spendpoint == 'mana':
                    self.maxmana += 1
                    print('You now have {0} Mana!'.format(self.maxmana))
                    break
                elif spendpoint == 'luck':
                    self.luck += 1
                    print('You now have {0} Luck!'.format(self.luck))
                    break
                elif spendpoint != 'hp' or 'mana' or 'luck':
                    print('Invalid input.\n')
            except ValueError:
                print('Invalid Input\n')

    def view_inventory(self):
        """ Views the player's gold and inventory. """
        print('==============================')
        for i in self.inventory:
            if i.type == "head":
                head = self.equipment[i]
                print('Head:   {0} --- {1} Armor'.format(head.name, head.armorValue))
            elif i.type == "chest":
                chest = self.equipment[i]
                print('Chest:  {0} --- {1} Armor'.format(chest.name, chest.armorValue))
            elif i.type == "legs":
                legs = self.equipment[i]
                print('Legs:   {0} --- {1} Armor'.format(legs.name, legs.armorValue))
        #print('Weapon: {0} --- {1} Attack')#.format(weapon.name, weapon.power)
        print('\n$$$$$ Gold: {0} $$$$$\n'.format(self.gold))
        if self.inventory:
            x = -1
            for i in self.inventory:
                x += 1
                print('( ' + str(x) + ' ) ' + i.name)
        else:
            print('\nYour inventory is empty! :(')
        print('==============================')

    def use_item(self,item):
        """ Views the inventory, and then asks the player what item they would like to use. """
        self.inventory[item].use()

    def add_item(self, item):
        """ Adds an item to the inventory. """
        self.inventory.append(item)
        print('--You acquired {0}!--\n'.format(item.name))

        #
        #
        # Combat methods
        #
        #
    def hurt(self,damage):
        armor = self.armor/10
        self.update()
        if(self.armor > 3):
            self.currenthp -= damage*armor
        else:
            self.currenthp -= damage
    def attack(self, enemy):
        if self.currenthp > 0:
            enemy.hurt(self.atk)
            if enemy.currenthp < 0:
                enemy.currenthp = 0
            print(str('&&& {0} attacked {1} for {2} points of damage! &&&'
                  .format(self.name, enemy.name, self.atk)))
            time.sleep(0.5)
            print("========================================")
            print("{0}: {1}/{2}".format(enemy.name, enemy.currenthp, enemy.maxhp))
            print("========================================")

    def flee(self, enemy):
        """ Attempt to flee. Utilizes Luck. """
        print('{0} attempts to flee!'.format(self.name))
        x = random.randint(0, 20)
        if self.luck >= x:
            print('\n{0} has successfully ran away from {1}!'
                  .format(self.name, enemy.name))  # Player does not get exp or gold if fleeing is successful.
            for i in combatenemy:
                combatenemy.remove(i)
        # Clears the enemy list, this will have to be handled differently with multiple enemies and players"""


class Player(Character):
    def __init__(self,creation):
        super(Player, self).__init__()
        # Each player object will have their own unique 'identifier' attribute. This identifier will be 1 for Player 1,
        # 2 for Player 2, etc. This will allow easier multi-player support.
        self.identifier = creation[0]
        self.name = creation[1]
        self.maxhp = creation[2]
        self.maxmana = creation[3]
        self.luck = creation[4]
        # Attributes from character creation:
        # Attributes generated using the ones above:
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        self.level = self.maxhp + self.maxmana + self.luck - 24
        self.neededexp = 15
        self.currentexp = 0
        self.inventory = []
        self.gold = 0
        self.type = "NULL"
        self.atk = 1
        self.armor = 0
        self.add_item(medHealth())
        self.add_item(steelPants())
        self.add_item(healthPotion())
        self.add_item(woodSword())
        self.add_item(steelSword())

    def use_item(self):
        """ Views the inventory, and then asks the player what item they would like to use. """
        self.view_inventory()
        x = len(self.inventory)
        while self.inventory:
            try:
                useitem = abs(int(input("\nWhat do you use? (# for item, anything else to go back.)\n")))
                if useitem <= x:
                    self.inventory[useitem].use(self)
                    self.view_inventory()
                elif useitem > x:
                    print('\nInvalid item number.')
            except ValueError:
                break
        else:
            print('==============================')
            print('Your inventory is empty! :(')
            print('==============================')

    def death(self):
        """ Method used if player_update() detects that the player's HP has reached 0. """
        points = self.level
        print('\n\n,_,_,_You have died._,_,_,\n'
              'Points: {0}'.format(points))
        sys.exit()

    def add_item(self, item):
        self.inventory.append(item)
        print('--You acquired {0}!--\n'.format(item.name))
    pass
#
#
# End of Player class.
#
#


def character_creation():
    """ Character creation function. """
    attributes = 25
    name = input('What is your name?\n')
    global number_of_players
    number_of_players += 1
    while True:
        try:
            maxhp = abs(int(input("{0} points remaining.\nHow many points of HP would you like?\n".format(attributes))))
            if maxhp >= attributes:
                print('You have attempted to assign too many points.\n')
            elif maxhp == 0:
                print('You cannot assign 0 points to HP\n')
            else:
                attributes -= maxhp
                print('You now have {0} HP.\n'.format(maxhp))
                break
        except ValueError:
            print('Invalid input.\n')
    while True:
        try:
            maxmana = abs(int(input("{0} points remaining.\nHow many points of Mana would you like?\n"
                                    .format(attributes))))
            if maxmana > attributes:
                print('You have attempted to assign too many points.\n')
            else:
                attributes -= maxmana
                luck = attributes
                print('You now have {0} Mana.\n'
                      'Remaining points have been converted into {1} Luck\n'.format(maxmana, luck))
                return number_of_players, name, maxhp, maxmana, luck
        except ValueError:
            print('Invalid input.\n')

#
#
# Game initialization
# Game is started by creating a player object with
# attributes generated with character_creation()
#
#


# Starts the game.
player1 = Player(character_creation())


# Give the player a potion.



# TESTING TESTING TESTING
# Giving the player some gear for testing purposes. Play around with these and then remove them as needed.
