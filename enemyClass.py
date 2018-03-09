import random
from playerClass import *
from itemClass import *



class AI(Character):
    def death(self, opponent):
        combatenemy.remove(self)  # Removes the enemy from the combatenemy list.
        self.currenthp = self.maxhp  # Brings the enemy object back up to full hp so it can be used later.
        opponent.currentexp += self.level  # Gives the player exp.
        opponent.gold += self.gold  # Gives the player gold.
        print('\n**** You have defeated {0}! You gain {1} experience and {2} gold! ***\n'
              .format(self.name, self.level, self.gold))

    def combatTurn(self, e):
        if self.currenthp <= e.atk:
            self.flee()
        else:
            self.attack(e)

class Humanoid(AI):
    def __init__(self):
        super(Humanoid, self).__init__()
        self.name = "Peasant"
        self.maxhp = 10
        self.currenthp = self.maxhp
        self.currentmana = self.maxmana
        self.equipment.append(equip_broken_straight_sword)
        self.inventory.append(potion_lesser_healing_potion)
    def update(self):
        if self.currenthp > self.maxhp:
            self.currenthp = self.maxhp
        self.armor = 0
        self.atk = 0
        for i in self.equipment:
            if i.itemsubtype == "chest":
                self.armor = i.value
            elif i.itemsubtype == "legs":
                self.armor = i.value
            elif i.itemsubtype == "head":
                self.armor = i.value
            elif i.itemsubtype == "weapon":
                self.atk = i.value
    def combatTurn(self, e):
        usedTurn = False
        if self.currenthp <= e.atk:
            self.flee()
            usedTurn = True
        elif self.currenthp <= (self.maxhp/2):
            x = -1
            for i in self.inventory:
                x += 1
                if i.itemtype == "potion":
                    if self.currenthp <= (self.maxhp - i.value):
                        self.inventory[x].activate(self)
                        usedTurn = True
        if usedTurn == False:
            self.attack(e)
        self.update()


class Knight(Humanoid):
    def __init__(self):
        super(Humanoid, self).__init__()
        self.name = "Black Knight"
        self.maxhp = 20
        self.currenthp = self.maxhp
        self.equipment= [equip_steel_chest, equip_steel_legs, equip_steel_helmet, equip_steel_sword]
        self.inventory.append(potion_greater_healing_potion)


class spellCaster(Humanoid):
    def __init__(self):
        super(spellCaster, self).__init__()
        self.name = "Magician"
        self.maxhp = 15
        self.currenthp = self.maxhp
        self.maxmana = 10
        self.currentmana = self.maxmana
        self.inventory.append(potion_lesser_healing_potion)
        self.equipment = []
        self.equipment.append(npc_wand)
        self.spellbook.append(spell_lesser_fireball)

    def combatTurn(self, e):
        usedTurn = False
        if self.currenthp <= e.atk:
            self.flee()
            usedTurn = True
        elif self.currenthp <= (self.maxhp/2):
            x = -1
            for i in self.inventory:
                x += 1
                if i.itemtype == "potion":
                    if self.currenthp < self.maxhp:
                        self.inventory[x].activate(self)
                        usedTurn = True
        if usedTurn == False:
            for i in self.spellbook:
                x = -1
                if i.mana < self.currentmana:
                    x+=1
                    self.cast_spell(x, e)
                    usedTurn = True
        if usedTurn == False:
            self.attack(e)

class Wizard(spellCaster):
    def __init__(self):
        super(spellCaster, self).__init__()
        self.name = "Magician"
        self.maxhp = 15
        self.currenthp = self.maxhp
        self.maxmana = 10
        self.currentmana = self.maxmana
        self.inventory.append(potion_greater_healing_potion)
        self.equipment = []
        self.equipment.append(npc_wand)
        self.spellbook.append(spell_greater_fireball)

class mirrorMatch(Wizard):
    def __init__(self, player):
        super(mirrorMatch, self).__init__()
        self.name = player.name
        self.maxhp = player.maxhp
        self.currenthp = self.maxhp
        self.maxmana = player.maxmana
        self.currentmana = self.maxmana
        self.equipment = player.equipment
        self.spellbook = player.spellbook
        self.inventory = player.inventory




class Rat(AI):
    def __init__(self):
        super(Rat, self).__init__()
        self.name = "Giant Rat"
        self.maxhp = 10
        self.currenthp = self.maxhp
        self.maxmana = 10
        self.luck = 1
        self.atk = 4

    def attack(self, enemy):
        if self.currenthp > 0:
            combatroll = random.randint(1, 100)
            damage = int(self.atk/2)
            if combatroll > 65:
                print(str('&&& {0} attacked {1} for {2} points of damage with his right paw! &&&'
                          .format(self.name, enemy.name, damage)))
                enemy.currenthp -= damage
            else:
                print("{0} missed his right paw attack!".format(self.name,))
            combatroll = random.randint(1, 100)
            if combatroll < 65:
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


class Bear(Rat):
    def __init__(self):
        super(Rat, self).__init__()
        self.hasAI = True
        self.name = "Black Bear"
        self.maxhp = 30
        self.currenthp = self.maxhp
        self.luck = 5
        self.atk = 6



#
#
# Adding enemies to tier lists
#
#
tier1enemy = (Rat(), Humanoid(), spellCaster())
tier2enemy = (Knight(), Wizard(), Bear())
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
    if combatRoll == 1:
        e = mirrorMatch(player)
    if combatRoll <= 10:
        e = random.choice(tier1enemy)  # Choose a random enemy from a tier based on player level
    elif combatRoll <= 25:
        e = random.choice(tier2enemy)
    combatenemy.append(e)  # Add the random enemy to the combatenemy list.
    print('You have encountered a {0}!'.format(e.name))
    e.view_stats()
    e.update()
    while e.currenthp > 0:
        player.combatTurn(e)
        e.combatTurn(player)
combat_commands = {
    'stats': 'View your current stats.',
    'inven': 'View your current inventory and gold.',
    'use': 'Use an item in your inventory.',
    'enemy': "View the current enemy's stats.",
    'attack': 'Attack the current enemy.',
    'flee': 'Attempt to run away.'
}
