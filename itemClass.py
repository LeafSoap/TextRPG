class Item:
    """This class creates healing potion items. Each potion is an object."""
    def __init__(self, itemtype, itemsubtype, name, points):
        self.itemtype = itemtype
        self.itemsubtype = itemsubtype
        self.name = name
        self.points = points

    def description(self):
        if self.itemsubtype == 'hppot':
            return 'Restores {1} HP.'.format(self.name, self.points)
        elif self.itemsubtype == 'manapot':
            return 'Restores {1} Mana.'.format(self.name, self.points)
        elif self.itemsubtype == 'rejuvpot':
            return 'Restores {1} HP and Mana.'.format(self.name, self.points)

    def use(self, player):
        player.inventory.remove(self)
        if self.itemtype == 'potion':
            if self.itemsubtype == 'hppot':
                player.currenthp += self.points
                print('You drank a {0}.'.format(self.name))
                player.update()
            elif self.itemsubtype == 'manapot':
                player.currentmana += self.points
                print('You drank a {0}.'.format(self.name))
                player.update()
            elif self.itemsubtype == 'rejuvpot':
                player.curenthp += self.points
                player.currentmana += self.points
                print('You drank a {0}.'.format(self.name))
                player.update()
        else:
            pass


#
# Creating potion objects
#


potion_lesser_healing_potion = Item('potion', 'hppot', 'Lesser Healing Potion', 4)
potion_healing_potion = Item('potion', 'hppot', 'Healing Potion', 7)
potion_greater_healing_potion = Item('potion', 'hppot', 'Greater Healing Potion', 10)
potion_lesser_mana_potion = Item('potion', 'manapot', 'Lesser Mana Potion', 4)
potion_mana_potion = Item('potion', 'manapot', 'Mana Potion', 7)
potion_greater_mana_potion = Item('potion', 'manapot', 'Greater Mana Potion', 10)
potion_lesser_rejuv_potion = Item('potion', 'rejuvpot', 'Lesser Rejuvenation Potion', 3)
potion_rejuv_potion = Item('potion', 'rejuvpot', 'Rejuvenation Potion', 6)
potion_greater_rejuv_potion = Item('potion', 'rejuvpot', 'Greater Rejuvenation Potion', 9)


#
# Adding potions to tier lists
#


tier1potion = (potion_lesser_healing_potion,
               potion_lesser_mana_potion,
               potion_lesser_rejuv_potion)

tier2potion = (potion_healing_potion,
               potion_mana_potion,
               potion_rejuv_potion)

tier3potion = (potion_greater_healing_potion,
               potion_greater_mana_potion,
               potion_greater_rejuv_potion)
