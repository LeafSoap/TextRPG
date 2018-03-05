import sys
import random
from enemyClass import *
from playerClass import *
from itemClass import *

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
    player.update()  # Updates the player every loop
    e.update()  # Updates the enemy every loop for good measure. May be useless.
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
            useItem(player1)
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
        e.update()  # Updates the enemy every loop for good measure. May be useless.

combat_commands = {
    'stats': 'View your current stats.',
    'inven': 'View your current inventory and gold.',
    'use': 'Use an item in your inventory.',
    'enemy': "View the current enemy's stats.",
    'attack': 'Attack the current enemy.',
    'flee': 'Attempt to run away.'
}
