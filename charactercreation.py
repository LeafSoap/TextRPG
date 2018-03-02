import time
import random


main_commands = {
    'stats': 'View your current stats.',
    'inv': 'View your current inventory and gold.',
}


def main():
    """This is the main loop that runs between each encounter"""
    while currenthp > 0:  # Check to see if player is dead.
        whatnext = input("\nWhat would you like to do next? ('help' for commands)\n")
        if whatnext == 'help':  # help command
            for key in main_commands:
                print(str(key) + ": " + str(main_commands[key]))
        elif whatnext == 'stats':  # stats command
            print("HP:   {0}/{1}\nMana: {2}/{3}\nLuck: {4}".format(currenthp, maxhp, currentmana, maxmana, luck))
        else:
            print("Invalid command.\n")
            continue

    else:
        print("You have died.")


def character_creation():
    """Creates character stats from player input"""
    global maxhp  # Declaring variables globally
    global maxmana
    global currenthp
    global currentmana
    global stats
    global viewstats  # "clean" version of stats, used when viewed by player
    stats = {}
    genes = random.randint(15, 21)  # Amount of points are selected by random

    # Get HP from input
    valid_input = True
    while valid_input:
        try:
            print("Points remaining: {0}".format(genes))
            global maxhp
            maxhp = abs(int(input("How many points of HP would you like?\n")))
            if maxhp > genes:
                # Runs the loop again if player attempts to assign too many points.
                print("You have attempted to assign too many points. Try again.")
                continue
            elif maxhp == 0:
                print("You can not assign zero HP. Try again")  # Prevents zero hp
            else:
                print("You now have {0} HP\n".format(maxhp))
                currenthp = maxhp
                genes = genes - maxhp
                break
        except ValueError:
            print("Invalid input. Try again")
            continue

    # Get Mana from input, turn the remaining points to Luck
    while valid_input:
        try:
            print("Points remaining: {0}".format(genes))
            global maxmana
            maxmana = abs(int(input("How many points of Mana would you like?\n")))
            if maxmana > genes:
                # Runs the loop again if player attempts to assign too many points.
                print("You have attempted to assign too many points. Try again.")
                continue
            else:
                genes = genes - maxmana
                currentmana = maxmana
                global luck
                luck = genes
                print("You now have {0} points of HP and {1} points of Mana. Your remaining points have been turne"
                      "d into {2} points of Luck.\n".format(maxhp, maxmana, luck))
                break
        except ValueError:
            print("Invalid input. Try again.")
            continue

    # Adds hp, mana, and luck to stats
    stats['HP'] = maxhp
    stats['Mana'] = maxmana
    stats['Luck'] = luck
    main()


character_creation()




