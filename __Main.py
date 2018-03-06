import sys
import random
from enemyClass import *
from playerClass import *
from itemClass import *
from encounters import *


#
#
# Commands
#
#


main_commands = {
    'stats': 'View your current stats.',
    'inven': 'View your current inventory and gold.',
    'use': 'Use an item in your inventory.',
    'equip': 'Equip an item in your inventory.',
    'explore': 'Travel to a new place.'
}



#
#
# Main loop
# The main loop checks to see if player1 exists before starting.
# player1 is created in the playerClasses file.
# Check the bottom of playerClasses.py
#
#


while player1:
    Player.update(player1)
    maincommand = input("\nWhat would you like to do next? ('help' for commands)\n")
    if maincommand == 'help':
        for key in main_commands:
            print(str(key) + ": " + str(main_commands[key]))
    elif maincommand == 'stats':
        Player.view_stats(player1)
    elif maincommand == 'inven':
        Player.view_inventory(player1)
    elif maincommand == 'use':
        player1.use_item()
    elif maincommand == 'explore':
        x = random.randint(1, 1)
        if x == 1:
            combat(player1)
    else:
        print('Invalid command.')
