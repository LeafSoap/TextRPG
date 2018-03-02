import time
import random
import sys

main_commands = {
    'stats': 'View your current stats.',
    'inv': 'View your current inventory and gold.',
    'explore': 'Travel to a new place.'
}

combat_commands = {
    'stats': 'View your current stats.',
    'inv': 'View your current inventory and gold.',
    'attack': 'Attack the enemy.',
    'run': 'Attempt to run away.',
    'enemy': 'Show stats of current enemy.'
}


class Enemy:
    """Enemy values. Will be randomly generated"""
    def __init__(self, name, maxhp, currenthp, attack, exp, gold):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = currenthp
        self.attack = attack
        self.exp = exp
        self.gold = gold


class Player:
    """All of the information about the player."""
    def __init__(self, maxhp, currenthp, maxmana, currentmana, luck, level, currentexp, neededexp, gold, attack):
        self.maxhp = maxhp
        self.currenthp = currenthp
        self.maxmana = maxmana
        self.currentmana = currentmana
        self.luck = luck
        self.level = level
        self.currentexp = currentexp
        self.neededexp = neededexp
        self.gold = gold
        self.attack = attack


# These next functions are used when a fight encounter is rolled.
# encounter_fight() generates random values for an enemy.
# combat() is where all of the combat takes place.
# deathcheck() checks if the player or enemy is dead.
# lvlup() will run after deathcheck() if a slain enemy causes the player to level up.


def encounter_fight():
    """Monster encounter. This will randomly generate a monster based on player level."""
    names = ['Lesser Beast', 'Living Mushroom', 'Crustacean', 'Swarm of Bees', 'Angry Peasant']
    Enemy.name = random.choice(names)
    Enemy.maxhp = random.randint(int(Player.level + 5), int(Player.level + 10))
    Enemy.currenthp = Enemy.maxhp
    Enemy.exp = random.randint(int(Enemy.maxhp + 10), int(Enemy.maxhp + 20))
    Enemy.gold = int(Enemy.maxhp) + random.randint(0, int(Player.luck * 2))
    print('\nYou have encountered a {0}!\n'.format(Enemy.name))
    combat()


def combat():
    """This is combat."""
    print("========================================")
    print("HP: {0}/{1}           {2}: {3}/{4}".format(Player.currenthp, Player.maxhp, Enemy.name, Enemy.currenthp,
                                                      Enemy.maxhp))
    print("========================================")
    while Player.currenthp > 0 and Enemy.currenthp > 0:
        combatcommand = input("\nYou are in combat. What do you do next? ('help' for commands)'\n")
        if combatcommand == 'help':
            for key in combat_commands:
                print(str(key) + ": " + str(combat_commands[key]))
        elif combatcommand == 'stats':
            print('==========')
            print('Level: {0}\nExp:  {1}/{2}'.format(Player.level, Player.currentexp, Player.neededexp))
            print("HP:   {0}/{1}\nMana: {2}/{3}\nLuck: {4}".format(Player.currenthp, Player.maxhp, Player.currentmana,
                                                                   Player.maxmana, Player.luck))
            print('==========')
        elif combatcommand == 'enemy':
            print('====================')
            print("{0}'s HP: {1}/{2}".format(Enemy.name, Enemy.currenthp, Enemy.maxhp))
            print('====================')
            continue
        elif combatcommand == 'attack':
            Player.attack = 3
            Enemy.currenthp = Enemy.currenthp - Player.attack
            print("You have attacked the {0} for {1} damage!".format(Enemy.name, Player.attack))
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            if Enemy.currenthp > 0:
                Enemy.attack = random.randint(0, int(Player.level + 3))
                if Enemy.attack == 0:
                    print("{0} missed! You take no damage.".format(Enemy.name))
                    combat()
                else:
                    Player.currenthp = Player.currenthp - Enemy.attack
                    print("{0} attacks you for {1} points of damage!".format(Enemy.name, Enemy.attack))
                    deathcheck()
            else:
                deathcheck()
    else:
            deathcheck()


def deathcheck():
    if Player.currenthp > 0:
        pass
    else:
        player_death()
    if Enemy.currenthp <= 0:
        Player.gold = Player.gold + Enemy.gold
        Player.currentexp = Player.currentexp + Enemy.exp
        print("-*-*-*You have defeated a {0} and gained {1} experience!*-*-*-".format(Enemy.name, Enemy.exp))
        if Player.currentexp >= Player.neededexp:
            Player.currentexp = Player.currentexp - Player.neededexp
            lvlup()
        else:
            main()
    else:
        combat()


# lvlup() will run once the player's exp reaches the required exp to level up
# This will allow the player to increase HP or Mana by 1 point.


def lvlup():
    valid_input = True
    print("-*-*-*You have gained a level!*-*-*-")
    while valid_input:
        try:
            lvlup = input("Would you like to level up HP, Mana, or Luck? (hp, mana, luck.)\n")
            if lvlup == 'hp':
                Player.maxhp = Player.maxhp + 1
                print("You now have {0} HP!\nYou have recovered all HP and Mana.".format(Player.maxhp))
                Player.currenthp = Player.maxhp
                Player.currentmana = Player.maxmana
                Player.level = Player.level + 1
                main()
            elif lvlup == 'mana':
                Player.maxmana = Player.maxmana + 1
                print("You now have {0} Mana!\nYou have recovered all HP and Mana.".format(Player.maxmana))
                Player.currenthp = Player.maxhp
                Player.currentmana = Player.maxmana
                Player.level = Player.level + 1
                main()
            elif lvlup == 'luck':
                Player.luck = Player.luck + 1
                print("You now have {0} Luck!\nYou have recovered all HP and Mana.".format(Player.luck))
                Player.currenthp = Player.maxhp
                Player.currentmana = Player.maxmana
                Player.level = Player.level + 1
                main()
            else:
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")
            continue


# player_death() will run when the player's HP reaches 0 or less
# The player will then be able to choose to play again.

def player_death():
    points = int(Player.level * 10) + int(Player.gold * 2)
    print("You have died!")
    print("Points: {0}".format(points))
    playagain = input("Would you like to play again? (yes/no)\n")
    if playagain == 'yes':
        character_creation()
    else:
        print("\nThanks for playing!")
        sys.exit()


# The main() function is used between encounters.
# After every encounter, the player will return to main(), an 'idle' state.


def main():
    """This is the main loop that runs between each encounter"""
    global encounter_type
    Player.neededexp = 20 + int(Player.level * 10)
    while Player.currenthp > 0:  # Check to see if player is dead.
        maincommand = input("\nWhat would you like to do next? ('help' for commands)\n")
        if maincommand == 'help':  # help command
            for key in main_commands:
                print(str(key) + ": " + str(main_commands[key]))
        elif maincommand == 'stats':  # stats command
            print('==========')
            print('Level: {0}\nExp:  {1}/{2}'.format(Player.level, Player.currentexp, Player.neededexp))
            print("HP:   {0}/{1}\nMana: {2}/{3}\nLuck: {4}".format(Player.currenthp, Player.maxhp, Player.currentmana,
                                                                   Player.maxmana, Player.luck))
            print('==========')
        elif maincommand == 'explore':
            encounter_type = random.randint(1, 1)
            if encounter_type == 1:
                encounter_fight()
        else:
            print("Invalid command.\n")
            continue

    else:
        deathcheck()


# character_creation() is the first function called when the program runs.
# It allows the user to create a character by assigning different values to stats
# These stats are HP, Mana, and luck
#
# HP is health points
# Mana is magic juice
# Luck will give the player more gold and items during encounters.


def character_creation():
    """Creates character stats from player input, then runs main function"""
    genes = random.randint(25, 25)  # Amount of points are selected by random

    # Get HP from input
    valid_input = True
    Player.currentexp = 0
    Player.gold = 0
    while valid_input:
        try:
            print("Points remaining: {0}".format(genes))
            Player.maxhp = abs(int(input("How many points of HP would you like?\n")))
            if Player.maxhp > genes:
                # Runs the loop again if player attempts to assign too many points.
                print("You have attempted to assign too many points. Try again.")
                continue
            elif Player.maxhp == 0:
                print("You can not assign zero HP. Try again")  # Prevents zero hp
            else:
                print("You now have {0} HP\n".format(Player.maxhp))
                Player.currenthp = Player.maxhp
                genes = genes - Player.maxhp
                break
        except ValueError:
            print("Invalid input. Try again")
            continue

    # Get Mana from input, turn the remaining points to Luck
    while valid_input:
        try:
            print("Points remaining: {0}".format(genes))
            Player.maxmana = abs(int(input("How many points of Mana would you like?\n")))
            if Player.maxmana > genes:
                # Runs the loop again if player attempts to assign too many points.
                print("You have attempted to assign too many points. Try again.")
                continue
            else:
                genes = genes - Player.maxmana
                Player.currentmana = Player.maxmana
                Player.luck = genes
                print("You now have {0} points of HP and {1} points of Mana. Your remaining points have been turne"
                      "d into {2} points of Luck.\n".format(Player.maxhp, Player.maxmana, Player.luck))
                Player.level = Player.maxhp + Player.maxmana + Player.luck - 24
                Player.currentexp = 0
                Player.neededexp = 30
                break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    main()


character_creation()




