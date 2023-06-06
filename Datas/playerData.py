from weaponData import Weapon
from armorData import Armor

class Player:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = Armor("", 0)
        self.weapon = Weapon("", 0)
        self.inv = []