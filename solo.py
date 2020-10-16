# Minion class
class Minion:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 5
        self.health = level * 5
        self.is_knocked_out = 0

    def __repr__(self):
        return "Your level {level} {name} has {health} health out of {max_health} total health".format(level=self.level, name=self.name, max_health=self.max_health, health=self.health)

    def lose_health(self, n):
        self.health -= n
        if self.health <= 0:
            self.is_knocked_out += 1
            print('{name} fainted!'.format(name=self.name))
            return self.is_knocked_out
        else:
            print('{name} now has {health} health'.format(name=self.name, health=self.health))
        return self.health

    def gain_health(self):
        if 20 + self.health <= self.max_health:
            self.health += 20
            print('You used your potion on {name}! {name} now has {health} health'.format(name=self.name, health=self.health))
            time.sleep(0.5)
            return self.health
        else:
            self.health = self.max_health
            print('You used your potion on {name}! {name} now has {health} health'.format(name=self.name, health=self.health))
            time.sleep(0.5)
            return self.health

    def revive(self):
        if self.is_knocked_out == 1:
            self.is_knocked_out = 0
            self.health = 1
            print("Your minion was revived! {name} now has {health} HP.".format(name=self.name, health=self.health))
            return self.health
        else:
            print("Your minion is not dead!")
