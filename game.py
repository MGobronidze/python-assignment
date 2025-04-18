import random

class Character:
    def __init__(self, name, health, attack_power):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def attack_power(self):
        return self._attack_power

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack Power: {self.attack_power})"

class Player(Character):
    def __init__(self, name, health, attack_power, gold=0):
        super().__init__(name, health, attack_power)
        self._gold = gold

    @property
    def gold(self):
        return self._gold

    def collect_gold(self, amount):
        self._gold += amount
        print(f"{self.name} has collected {amount} gold!")

    def __str__(self):
        return super().__str__() + f" (Gold: {self.gold})"

