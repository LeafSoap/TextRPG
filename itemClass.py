class Item:
    """This class creates healing potion items. Each potion is an object."""
    def __init__(self):
        self.name = "Null Item"
        self.points = 0
        self.price = 0
        self.description = "A Null Item"
    def use(self, player):  # Uses same method to use basic items (potions for now) and basic equipment
        pass


class healthPotion():
    def __init__(self):
        self.type = "potion"
        self.name = "Small Health Potion"
        self.points = 3
        self.price = 15
        self.uses = 3
        self.description = "{0} restores {1} health.".format(self.name, self.points)
    def use(self,user):
        user.currenthp += self.points
        print("{0} used a {1}, healing {2} points".format(user.name, self.name, self.points))
        self.uses -= 1
        if(self.uses > 0):
            print("{0} uses left".format(self.uses))
        if(self.uses <= 0):
            user.inventory.remove(self)
            print("{0} drained the last bit of {0} and leave the flask on the ground.".format(user.name, self.name))


class manaPotion():
    def __init__(self):
        self.type = "potion"
        self.name = "Small Mana Potion"
        self.points = 15
        self.price = 15
        self.description = "{0} restores {1} mana.".format(self.name, self.points)
    def use(self,user):
        user.currentmana += self.points


class medHealth(healthPotion):
    def __init__(self):
        super(medHealth, self).__init__()
        self.uses = 3
        self.type = "potion"
        self.name = "Medium Health Potion"
        self.points = 30
        self.price = 30
        self.description = "{0} restores {1} health.".format(self.name, self.points)


class Equipable(Item):
    def __init__(self):
        self.type = "equipable"
        self.name = "A Null Item"
        self.slot = 0
        self.armorValue = 0


    def use(self,user):
        for i in user.equipment:
            if i.type == self.type:
                previous_equipment = i  # create a local variable of the equipment being replaced,
                user.equipment.remove(previous_equipment)  # remove the previous equipment from equipment slot,
                user.inventory.append(previous_equipment)
                print("You remove " + str(previous_equipment.name))
        user.equipment.append(self)
        user.inventory.remove(self)
        print("{0} equipped {1}".format(user.name, self.name))


class leatherChest(Equipable):
    def __init__(self):
        super(leatherChest, self).__init__()
        self.type = "chest"
        self.name = "a Leather Chest Piece"
        self.armorValue = 3


class leatherHat(Equipable):
    def __init__(self):
        super(leatherHat, self).__init__()
        self.type = "head"
        self.name = "a Leather Coif"
        self.armorValue = 1


class leatherPants(Equipable):
    def __init__(self):
        super(leatherPants, self).__init__()
        self.type = "pants"
        self.name = "Studded Leather Pants"
        self.armorValue = 3


class steelPants(leatherPants):
    def __init__(self):
        super(steelPants, self).__init__()
        self.name = "Steel Greaves"


class steelChest(leatherChest):
    def __init__(self):
        super(steelChest, self).__init__()
        self.name = "Steel Greaves"


class woodSword(Equipable):
    def __init__(self):
        self.type = "weapon"
        self.name = "Wooden Sword"
        self.slot = 4
        self.power = 2

class steelSword(woodSword):
    def __init__(self):
        super(steelSword, self).__init__()
        self.name = "Steel Sword"
        self.power = 4


def useItem(player):
    """ Views the inventory, and then asks the player what item they would like to use. """
    player.view_inventory()
    x = len(player.inventory)
    while player.inventory:
        try:
            useitem = abs(int(input("\nWhat do you use? (# for item, anything else to go back.)\n")))
            if useitem <= x:
                player.inventory[useitem].use(player)
                player.view_inventory()
            elif useitem > x:
                print('\nInvalid item number.')
        except ValueError:
            break
    else:
        print('==============================')
        print('Your inventory is empty! :(')
        print('==============================')




tier1potion = (healthPotion(), manaPotion())
tier2potion = (medHealth,medHealth)