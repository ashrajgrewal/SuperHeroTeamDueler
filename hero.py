import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
# We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
    # we know the name of our hero, so we assign it here
        self.name = name
    # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block =  0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


    def take_damage(self, damage):
        defense = self.defend(damage)
        self.current_health -= (damage - defense)


    def is_alive(self):
        if (self.current_health <= 0):
            return False
        else:
            return True

    

    def fight(self, opponent):
        if (len(self.abilities) == 0 and len(opponent.abilities) == 0):
            print("Draw")
        else:
            while (self.is_alive() and opponent.is_alive()):
                opponent.take_damage(self.attack())
                if opponent.is_alive():
                    self.take_damage(opponent.attack())
                else:
                    pass
            if self.current_health <= 0:
                print(f"{opponent.name} won!")
                opponent.add_kill(1)
                self.add_death(1)
            else:
                print(f"{self.name} won!")
                self.add_kill(1)
                opponent.add_death(1)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())


    #COULDN'T INSTALL PYTEST