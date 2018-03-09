import sys
import os
import random
import pickle
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
    'book': 'View your spell book.',
    'cast': 'Cast a spell in your spell book.',
    'explore': 'Travel to a new place.',
    'save': 'Save the current game.'
}


def start_game():
    """ Starting the game. Can load previous savefiles from here."""
    print('\n.-*-.-*-.-*Welcome to TextRPG!*-.-*-.-*-.\n')
    while True:
        try:
            start = abs(int(input('( 1 ) Start Fresh\n( 2 ) Load game\n')))
            if start == 2:
                if os.path.exists('savefile'):  # Searches for save file
                    with open('savefile', 'rb') as f:  # If one exists, we open it.
                        global player1
                        player1 = pickle.load(f)  # Gotta use the pickle.
                    print("{0} has been loaded!".format(player1.name))
                    break
                else:
                    print('You have no save file.\n')
            elif start == 1:
                player1 = Player(character_creation())
                player1.add_item(potion_lesser_healing_potion)
                player1.add_item(equip_broken_straight_sword)
                player1.add_item(equip_silver_chest)
                Item.activate(equip_broken_straight_sword, player1)
                player1.add_item(tome_greaterheal)
                break
            else:
                print('Invalid input.\n')
        except ValueError:
            print('Invalid input.\n')


start_game()  # This starts the game.


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
        Player.use_item(player1)
    elif maincommand == 'book':
        Player.view_spellbook(player1)
    elif maincommand == 'cast':
        player1.cast_spell()
    elif maincommand == 'equip':
        Player.equip_item(player1)
    elif maincommand == 'explore':
        x = random.randint(1, 1)
        if x == 1:
            combat(player1)
    elif maincommand == 'save':
        with open('savefile', 'wb') as f:
            pickle.dump(player1, f)
            print('[[[GAME SAVED]]]')
    else:
        print('Invalid command.')
