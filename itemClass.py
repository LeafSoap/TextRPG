from spellClass import *


class Item:
    """This class creates healing potion items. Each potion is an object."""
    def __init__(self, itemtype, itemsubtype, name, value, price):
        self.itemtype = itemtype
        self.itemsubtype = itemsubtype
        self.name = name
        self.value = value
        self.price = price

    def description(self):
        if self.itemtype == 'potion':
            if self.itemsubtype == 'hppot':
                return 'Restores {1} HP.'.format(self.name, self.value)
            elif self.itemsubtype == 'manapot':
                return 'Restores {1} Mana.'.format(self.name, self.value)
            elif self.itemsubtype == 'rejuvpot':
                return 'Restores {1} HP and Mana.'.format(self.name, self.value)
        elif self.itemtype == 'equip':
            if self.itemsubtype == 'head':
                return 'Helmet that provides {1} armor.'.format(self.name, self.value)
            elif self.itemsubtype == 'chest':
                return 'Chest piece that provides {1} armor.'.format(self.name, self.value)
            elif self.itemsubtype == 'legs':
                return 'Leg armor that provides {1} armor.'.format(self.name, self.value)
            elif self.itemsubtype == 'weapon':
                return 'Weapon that provides {1} attack.'.format(self.name, self.value)
        elif self.itemtype == 'tome':
            return 'Tome that teaches the {0} spell.'.format(self.value.name)

    def activate(self, player):  # Uses same method to use basic items (potions for now) and basic equipment

        #
        # Check to see if item is a potion.
        #

        if self.itemtype == 'potion':
            player.inventory.remove(self)  # Remove the potion from inventory.
            if self.itemsubtype == 'hppot':  # Checks to see if the item is a healing potion.
                player.currenthp += self.value
                print('{0} drank a {1}.'.format(player.name, self.name))
                player.update()
            elif self.itemsubtype == 'manapot':  # Checks to see if the item is a mana potion.
                player.currentmana += self.value
                print('{0} drank a {1}.'.format(player.name, self.name))
                player.update()
            elif self.itemsubtype == 'rejuvpot':  # Checks to see if the item is a rejuvenation potion.
                player.curenthp += self.value
                player.currentmana += self.value
                print('You drank a {0}.'.format(self.name))
                player.update()

        #
        # Check to see if item is equipment.
        #

        elif self.itemtype == 'equip':
            player.inventory.remove(self)  # Remove the equipment from player inventory.
            if self.itemsubtype == 'head':  # Checks to see if the item is a helmet.
                if player.equipment[0] == item_null:  # If the slot is 'empty' (occupied by item_null),
                    player.equipment.remove(item_null)  # we remove a item_null from the equipment list,
                    player.equipment.insert(0, self)  # add the new equipment to the correct slot,
                    player.armor += self.value  # and finally add armor from new equipment to the player.
                else:  # If the slot is not empty, we...........
                    previous_equipment = player.equipment[0]  # create a local variable of the equipment being replaced,
                    player.equipment.remove(previous_equipment)  # remove the previous equipment from equipment slot,
                    player.inventory.append(previous_equipment)  # add previous equipment to player's inventory,
                    player.armor -= previous_equipment.value  # subtract the previous equipment's armor,
                    player.equipment.insert(0, self)  # add the new equipment to correct equipment slot,
                    player.armor += self.value  # and finally add armor from new equipment to the player.
            if self.itemsubtype == 'chest':  # Checks to see if the item is a chest piece.
                if player.equipment[1] == item_null:
                    player.equipment.remove(item_null)
                    player.equipment.insert(1, self)
                    player.armor += self.value
                else:
                    previous_equipment = player.equipment[1]
                    player.equipment.remove(previous_equipment)
                    player.inventory.append(previous_equipment)
                    player.armor -= previous_equipment.value
                    player.equipment.insert(1, self)
                    player.armor += self.value
            if self.itemsubtype == 'legs':  # Checks to see if the item is a leg piece.
                if player.equipment[2] == item_null:
                    player.equipment.remove(item_null)
                    player.equipment.insert(2, self)
                    player.armor += self.value
                else:
                    previous_equipment = player.equipment[2]
                    player.equipment.remove(previous_equipment)
                    player.inventory.append(previous_equipment)
                    player.armor -= previous_equipment.value
                    player.equipment.insert(2, self)
                    player.armor += self.value
            if self.itemsubtype == 'weapon':  # Checks to see if the item is a weapon.
                if player.equipment[3] == item_null:
                    player.equipment.remove(item_null)
                    player.equipment.insert(3, self)
                    player.atk += self.value  # Weapons add to atk, not armor.
                else:
                    previous_equipment = player.equipment[3]
                    player.equipment.remove(previous_equipment)
                    player.inventory.append(previous_equipment)
                    player.atk -= previous_equipment.value
                    player.equipment.insert(3, self)
                    player.atk += self.value
            print('You equipped {0}.\n'.format(self.name))  # Tells the player if they successfully equipped an item.

        #
        # Check to see if item is a tome.
        #

        elif self.itemtype == 'tome':
            player.add_spell(self.value)
            player.inventory.remove(self)


#
# Creating an 'empty slot' item. All equipment slots must be filled.
# So when the player's equipment slot is 'empty', it will be filled with this.
# DO NOT DELETE ITEM_NULL!
#


item_null = Item('equip', ' ', 'Nothing equipped.', 0, 0)


#
# Creating potion objects.
# Then adding them to tier lists.
# # item_object = Item('itemtype', 'itemsubtype', 'name', points, gold
#


potion_lesser_healing_potion = Item('potion', 'hppot', 'Lesser Healing Potion', 4, 10)
potion_healing_potion = Item('potion', 'hppot', 'Healing Potion', 7, 15)
potion_greater_healing_potion = Item('potion', 'hppot', 'Greater Healing Potion', 10, 20)
potion_lesser_mana_potion = Item('potion', 'manapot', 'Lesser Mana Potion', 4, 10)
potion_mana_potion = Item('potion', 'manapot', 'Mana Potion', 7, 15)
potion_greater_mana_potion = Item('potion', 'manapot', 'Greater Mana Potion', 10, 20)
potion_lesser_rejuv_potion = Item('potion', 'rejuvpot', 'Lesser Rejuvenation Potion', 3, 15)
potion_rejuv_potion = Item('potion', 'rejuvpot', 'Rejuvenation Potion', 6, 20)
potion_greater_rejuv_potion = Item('potion', 'rejuvpot', 'Greater Rejuvenation Potion', 9, 25)


tier1potion = (potion_lesser_healing_potion,
               potion_lesser_mana_potion,
               potion_lesser_rejuv_potion)

tier2potion = (potion_healing_potion,
               potion_mana_potion,
               potion_rejuv_potion)

tier3potion = (potion_greater_healing_potion,
               potion_greater_mana_potion,
               potion_greater_rejuv_potion)


#
# Creating equipment objects
# Then adding them to tier lists.
# item_object = Item('itemtype', 'itemsubtype', 'name', atk/armor, gold
#

npc_wand = Item('equip', 'weapon', 'wand', 1, 1)
equip_broken_straight_sword = Item('equip', 'weapon', 'Broken Straight Sword', 3, 30)
equip_steel_sword = Item('equip', 'weapon', 'Steel sword', 5, 60)
equip_silver_blade = Item('equip', 'weapon', 'Silver Blade', 8, 120)
equip_bronze_helmet = Item('equip', 'head', 'Bronze Helmet', 1, 30)
equip_bronze_chest = Item('equip', 'chest', 'Bronze Chest Plate', 3, 60)
equip_bronze_legs = Item('equip', 'legs', 'Bronze Leggings', 2, 45)
equip_steel_helmet = Item('equip', 'head', 'Steel Helmet', 2, 60)
equip_steel_chest = Item('equip', 'chest', 'Steel Chest Plate', 6, 120)
equip_steel_legs = Item('equip', 'legs', 'Steel Leggings', 4, 90)
equip_silver_helmet = Item('equip', 'head', 'Silver Engraved Helmet', 4, 120)
equip_silver_chest = Item('equip', 'chest', 'Silver Engraved Chest Plate', 12, 240)
equip_silver_legs = Item('equip', 'legs', 'Silver Engraved Leggings', 8, 180)


tier1equipment = (equip_broken_straight_sword,
                  equip_bronze_helmet,
                  equip_bronze_chest,
                  equip_bronze_legs)


tier2equipment = (equip_steel_sword,
                  equip_steel_helmet,
                  equip_steel_chest,
                  equip_steel_legs)


tier3equipment = (equip_silver_blade,
                  equip_silver_helmet,
                  equip_silver_chest,
                  equip_silver_legs)


#
# Creating tome objects
# item_object = Item('tome', 'null', 'name', spell to teach, gold
#


tome_greaterheal = Item('tome', 'null', 'Tome of Greater Healing', spell_greater_heal, 50)