import random
from playerClass import *


class AI(Character):
    def update(self, opponent):
        """ Similar to Player.update(). """
        if self.currenthp <= 0:  # Checks to see if the enemy is dead.
            self.death(opponent)
        if self.currenthp <= 5:
            self.flee(opponent)

    def death(self, opponent):
        combatenemy.remove(self)  # Removes the enemy from the combatenemy list.
        self.currenthp = self.maxhp  # Brings the enemy object back up to full hp so it can be used later.
        opponent.currentexp += self.level  # Gives the player exp.
        opponent.gold += self.gold  # Gives the player gold.
        print('\n**** You have defeated {0}! You gain {1} experience and {2} gold! ***\n'
              .format(self.name, self.level, self.gold))


class Beast(AI):
    def attack(self, enemy):
        if self.currenthp > 0:
            combatroll = random.randint(1, 100)
            damage = int(self.atk/2)
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


combatenemy = []

#
#
# Creating enemies
#
#


enemy_rat = Beast([-1, 'Giant Rat', 15, 0, 2, 10, 2])
enemy_ghoul = AI([-1, 'Ghoul', 9, 2, 1, 15, 3])
enemy_livingmushroom = AI([-1, 'Living Mushroom', 5, 4, 5, 20, 2])
enemy_beast = Beast([-1, "Humanoid Beast", 15, 5, 2, random.randint(15, 25), 4])
enemy_zombie = AI([-1, "Zombified Peasant", 50, 0, 0, random.randint(15, 25), 1])
enemy_wolf = Beast([-1, "Direwolf", 8, 5, 5, 5, 8])


# Identifier, name, maxHP, maxMana, luck, gold, strength
#
#
# Adding enemies to tier lists
#
#
tier1enemy = (enemy_rat,
              enemy_ghoul,
              enemy_livingmushroom)
tier2enemy = (enemy_beast,
              enemy_zombie,
              enemy_wolf)
tier1gold = random.randint(10, 20)


#
#
# Combat function
#
#

# Throughout the combat function, you will see the variable 'e'
# e is the randomly selected enemy object
# In order to understand this a bit easier, imagine e = zombie


def combat(player):
    combatRoll = random.randint(1, player.level)
    if combatRoll <= 10:
        e = random.choice(tier1enemy)  # Choose a random enemy from a tier based on player level
    elif combatRoll <= 25:
        e = random.choice(tier2enemy)
    combatenemy.append(e)  # Add the random enemy to the combatenemy list.
    print('You have encountered a {0}!'.format(e.name))
    e.view_stats()
    while combatenemy:
        combatcommand = input("\nYou are in combat! ('help' for commands)\n")
        if combatcommand == 'help':  # Help command
            for key in combat_commands:  # 'key' throws a weak warning. Ignore it for now. Works fine.
                print(str(key) + ": " + str(combat_commands[key]))
        elif combatcommand == 'stats':  # ---Stats command
            player.view_stats()
        elif combatcommand == 'inven':  # ---Inventory command
            player.view_inventory()
        elif combatcommand == 'use':  # ---Use item command
            player.use_item()
            if combatenemy:  # If the enemy is still alive....
                e.attack(player)  # The enemy attacks after the player uses an item.
        elif combatcommand == 'enemy':  # ---View enemy stats command
            e.view_stats()
        elif combatcommand == 'attack':  # ---Attack command
            player.attack(e)
            if combatenemy:  # If the enemy is still alive...
                e.attack(player)  # The enemy counterattacks the player.
        elif combatcommand == 'flee':  # ---Flee command
            Player.flee(player, e)
            if combatenemy:  # Check to see if enemy is still alive, because successfully fleeing 'kills' enemy.
                e.attack(player)  # If fleeing is unsuccessful, the enemy attacks the player.
        player.update()  # Updates the player every loop
        e.update(player)  # Updates the enemy every loop for good measure. May be useless.

combat_commands = {
    'stats': 'View your current stats.',
    'inven': 'View your current inventory and gold.',
    'use': 'Use an item in your inventory.',
    'enemy': "View the current enemy's stats.",
    'attack': 'Attack the current enemy.',
    'flee': 'Attempt to run away.'
}
