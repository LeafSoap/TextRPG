import sys
import random
import time
from enemyClass import *
from itemClass import *
from spellClass import *


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
        self.identifier = -1
        self.name = "NULL"
        self.maxhp = 0
        self.maxmana = 0
        self.luck = 0
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        # Experience/Level attributes:
        self.level = self.maxhp + self.maxmana + self.luck
        # Inventory/Gold attributes:
        self.inventory = []
        self.gold = 0
        # Entity's attack and armor values:
        self.atk = 0
        self.armor = 0
        # Entity's equipment:
        # The list will have 4 objects.
        # 0 - Head
        # 1 - Chest
        # 2 - Legs
        # 3 - Weapon
        self.equipment = [item_null,  # Filling the Entity's equipment slots with
                          item_null,  # an 'empty' item, known as item_null.
                          item_null,
                          item_null]
        self.spellbook = []  # Giving the player a spellbook

    def view_stats(self):
        print('==========')
        print('Name:   {0}'.format(self.name))
        print('HP:     {0}/{1}'.format(self.currenthp, self.maxhp))
        print('Mana:   {0}/{1}'.format(self.currentmana, self.maxmana))
        print('Luck:   {0}'.format(self.luck))
        print('Armor:  {0}'.format(self.armor))
        print('Attack: {0}'.format(self.atk))
        print('==========')

    def update(self):


        """ Method used to check and player_update player status."""
        if self.currentexp >= self.neededexp:  # Check to see if player has enough exp to level up.
            self.lvlup()
        if self.currenthp <= 0:  # Check to see if player is dead.
            self.death()
        if self.currenthp > self.maxhp:  # Check if player has more HP than maximum
            self.currenthp = self.maxhp
        if self.currentmana > self.maxmana:  # Check if player has more Mana than maximum
            self.currentmana = self.maxmana

    def hurt(self, damage):
        self.currenthp -= damage

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
        x = -1
        head = self.equipment[0]
        chest = self.equipment[1]
        legs = self.equipment[2]
        weapon = self.equipment[3]
        print('==============================')
        print('Head:   {0} --- {1} Armor'.format(head.name, head.value))
        print('Chest:  {0} --- {1} Armor'.format(chest.name, chest.value))
        print('Legs:   {0} --- {1} Armor'.format(legs.name, legs.value))
        print('Weapon: {0} --- {1} Attack'.format(weapon.name, weapon.value))
        print('\n$$$$$ Gold: {0} $$$$$\n'.format(self.gold))
        if self.inventory:
            for i in self.inventory:
                x += 1
                print('( ' + str(x) + ' ) ' + i.name + ' - ' + i.description())
        else:
            print('\nYour inventory is empty! :(')
        print('==============================')


    def use_item(self, item):
        self.item.activate()

    def cast_spell(self, spell):
        self.spellbook[spell].activate_spell()

    def add_item(self, item):
        """ Adds an item to the inventory. """
        self.inventory.append(item)
        print('--You acquired {0}!--\n'.format(item.name))

    def add_spell(self, spell):
        """ Adds a spell to the spell book. """
        self.spellbook.append(spell)
        print('--You learned {0}!--\n'.format(spell.name))

        #
        #
        # Combat methods
        #
        #
    def combatTurn(self, e):
        self.attack(e)
        e.update()
        self.update()
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
    def __init__(self, creation):
        """ Constructs an object using the stats from character_creation()"""
        # Attributes from character creation:
        # Each player object will have their own unique 'identifier' attribute. This identifier will be 1 for Player 1,
        # 2 for Player 2, etc. This will allow easier multi-player support.
        self.identifier = creation[0]
        self.name = creation[1]
        self.maxhp = creation[2]
        self.maxmana = creation[3]
        self.luck = creation[4]
        # Attributes generated using the ones above:
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        # Experience/Level attributes:
        self.level = self.maxhp + self.maxmana + self.luck - 24
        self.neededexp = 15
        self.currentexp = 0
        # Inventory/Gold attributes:
        self.inventory = []
        self.gold = 0
        # Entity's attack and armor values:
        self.atk = 0
        self.armor = 0
        # Entity's equipment:
        # The list will have 4 objects.
        # 0 - Head
        # 1 - Chest
        # 2 - Legs
        # 3 - Weapon
        self.equipment = [item_null,  # Filling the Entity's equipment slots with
                          item_null,  # an 'empty' item, known as item_null.
                          item_null,
                          item_null]
        self.spellbook = []  # Giving the player a spellbook
    def combatTurn(self, e):

        usedTurn = False
        while usedTurn == False:
            combatcommand = input("\nYou are in combat! ('help' for commands)\n")
            if combatcommand == 'help':  # Help command
                for key in combat_commands:  # 'key' throws a weak warning. Ignore it for now. Works fine.
                    print(str(key) + ": " + str(combat_commands[key]))
            elif combatcommand == 'stats':  # ---Stats command
                self.view_stats()
            elif combatcommand == 'inven':  # ---Inventory command
                self.view_inventory()
            elif combatcommand == 'use':  # ---Use item command
                self.use_item()
                usedTurn = True
            elif combatcommand == 'enemy':  # ---View enemy stats command
                e.view_stats()
            elif combatcommand == 'cast':
                self.cast_spell()
                usedTurn = True
            elif combatcommand == 'attack':  # ---Attack command
                self.attack(e)
                usedTurn = True
            elif combatcommand == 'flee':  # ---Flee command
                self.flee(self, e)
                usedTurn = True
    def death(self):
        """ Method used if player_update() detects that the player's HP has reached 0. """
        points = self.level
        print('\n\n,_,_,_You have died._,_,_,\n'
              'Points: {0}'.format(points))
        sys.exit()
    pass

    def use_item(self):
        """ Views the inventory, and then asks the player what item they would like to use. """
        self.view_inventory()
        x = len(self.inventory)
        while self.inventory:
            try:
                useitem = abs(int(input("\nWhat do you use? (# for item, anything else to go back.)\n")))
                if useitem <= x and self.inventory[useitem].itemtype != 'equip':  # Trying to use equipment?
                    self.inventory[useitem].activate(self)  # No? Good.
                    break
                elif useitem <= x and self.inventory[useitem].itemtype == 'equip':  # Trying to use equipment?
                    print("\nYou can't use equipment! Try 'equip' command.")  # Yes? You can't do that!
                elif useitem > x:
                    print('\nInvalid item number.')
            except ValueError:
                break

    def cast_spell(self):
        self.view_spellbook()
        x = len(self.spellbook)
        while self.spellbook:
            try:
                usespell = abs(int(input("\nWhat spell do you cast? (# for item, anything else to go back.)\n")))
                if usespell <= x:
                    if combatenemy and self.spellbook[usespell].incombat == 1:  # Is spell combat only?
                        e = combatenemy[0]  # We are in combat! Set the current enemy to a local variable.
                        self.spellbook[usespell].activate_spell(self, e)  # and pass it to the spell's method.
                        break
                    elif not combatenemy and self.spellbook[usespell].incombat == 1:  # Is spell combat only?
                        print('Can only cast {0} in combat!'.format(self.spellbook[usespell].name))
                    else:  # This is for spells that can be used both in and out of combat.
                        self.spellbook[usespell].activate_spell(self)  # Spells that can be used in/out of combat.

                elif usespell > x:
                    print('\nInvalid spell number.')
            except ValueError:
                break

    def view_spellbook(self):
        """ Views the spell book. Very similar to viewing the inventory."""
        x = -1
        print('==============================')
        print('Mana: {0}/{1}\n'.format(self.currentmana, self.maxmana))
        if self.spellbook:
            for i in self.spellbook:
                x += 1
                print('( ' + str(x) + ' ) Mana: [ ' + str(i.mana) + ' ] ' + i.name + ' - ' + i.description)
        else:
            print('Your spell book is empty! :(')
        print('==============================')

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
#player1 = Player(character_creation())


# Give the player a potion.
#player1.add_item(potion_lesser_healing_potion)


# Giving the player a starter weapon.
#player1.add_item(equip_broken_straight_sword)


# Equipping the player with the starter weapon.
#Item.activate(equip_broken_straight_sword, player1)


# TESTING TESTING TESTING
# Giving the player some gear for testing purposes. Play around with these and then remove them as needed.
#player1.add_item(equip_silver_blade)
#player1.add_item(equip_steel_helmet)
#player1.add_item(potion_greater_rejuv_potion)
#player1.add_item(equip_silver_chest)
#player1.add_spell(spell_lesser_heal)
#player1.add_spell(spell_greater_fireball)
#player1.add_item(tome_greaterheal)