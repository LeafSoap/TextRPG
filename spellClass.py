from encounters import *


class Spell:
    def __init__(self, incombat, name, description, mana, gold, points1, points2, points3):
        self.incombat = incombat  # We use this to identify if a spell can be used outside of combat. 1 = only in combat
        self.name = name
        self.description = description
        self.mana = mana
        self.gold = gold
        self.points1 = points1  # All of these 'points' can be used for multiple things.
        self.point2 = points2  # Some item classes may only require 1 'points' attributes,
        self.points3 = points3  # others require multiple. I put 3 in for good measure to limit the need for "super".

    def description(self):
        return self.name, ': ', self.description, '. ', self.mana, ' Mana.'


class SpellHeal(Spell):
    def activate_spell(self, user):
        if user.currentmana >= self.mana and user.currenthp < user.maxhp:
            user.currentmana -= self.mana
            user.currenthp += self.points1
            print('{0} has cast {1}! {2} Recovers {3} HP!'
                  .format(user.name, self.name, user.name, self.points1))
        elif user.currenthp >= user.maxhp:
            print('You are already at maximum HP!')
        else:
            print('Not enough mana to cast {0}!'.format(self.name))


class SpellDamage(Spell):
    def activate_spell(self, user, opponent):
        if user.currentmana >= self.mana:
            user.currentmana -= self.mana
            opponent.currenthp -= self.points1
            print('{0} has cast {1}! {2} takes {3} points of damage!'
                  .format(user.name, self.name, opponent.name, self.points1))
        else:
            print('Not enough mana to cast {0}!'.format(self.name))


class SpellSmoke(Spell):
    def activate_spell(self, user, enemy):
        if user.currentmana >= self.mana:
            user.currentmana -= self.mana
            if combatenemy:
                combatenemy.remove(enemy)
                print('{0} cast {1} and successfully escaped from combat!'
                      .format(user.name, self.name))
        else:
            print('Not enough mana to cast {0}!'.format(self.name))


# Creating spells
# incombat, name, description, mana, gold, points1, points2, points3


spell_lesser_heal = SpellHeal(0, 'Lesser Heal', 'Heals yourself for 3 HP.',
                              3, 15, 3, 0, 0)
spell_medium_heal = SpellHeal(0, 'Heal', 'Heals yourself for 6 HP',
                              5, 30, 6, 0, 0)
spell_greater_heal = SpellHeal(0, 'Greater Heal', 'Heals yourself for 12 HP',
                               8, 50, 12, 0, 0)
spell_lesser_fireball = SpellDamage(1, 'Lesser Fireball', 'Shoot a fireball at your opponent. Deals 3 damage.',
                                    2, 15, 3, 0, 0)
spell_medium_fireball = SpellDamage(1, 'Fireball', 'Shoot a fireball at your opponent. Deals 6 damage.',
                                    4, 30, 6, 0, 0)
spell_greater_fireball = SpellDamage(1, 'Greater Fireball', 'Shoot a fireball at your opponent. Deals 12 damage.',
                                     7, 50, 12, 0, 0)
spell_thick_smoke = SpellSmoke(1, 'Ghostly Smoke', 'Creates a cloud of ghostly haze. Allows you to escape combat.',
                               4, 50, 0, 0, 0)
