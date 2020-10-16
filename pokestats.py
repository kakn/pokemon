import pandas as pd

def read_csv(filename):
    infile = open(filename, 'r').read()
    lines = infile.split('\n')[:-1]
    lines = [line.split(',') for line in lines]
    return lines[1:]

filename = "Pokemon.csv"
lines = read_csv(filename)

def pokedexter(lines):
    pokedex = {}
    for line in lines:
        pokedex[line[1]] = line[2:]
    return pokedex

pokedex = pokedexter(lines)

def genx(pokedex):
    genx = {}
    for pkmn in pokedex:
        stats = pokedex[pkmn]
        if stats[9] == "1":
            genx[pkmn] = stats
    return genx

PokeString = []
gen_one = genx(pokedex)
MyPokemon = []


class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = 0

    def __repr__(self):
        return "Your level {level} {name} has {health} health out of {max_health} total health.".format(level=self.level, name=self.name, max_health=self.max_health, health=self.health)

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
            return self.health
        else:
            self.health = self.max_health
            print('You used your potion on {name}! {name} now has {health} health'.format(name=self.name, health=self.health))
            return self.health

    def revive(self):
        if self.is_knocked_out == 1:
            self.is_knocked_out = 0
            self.health = 1
            print("Your pokemon was revived! {name} now has {health} HP.".format(name=self.name, health=self.health))
            return self.health
        else:
            print("Your pokemon is not dead!")

    def attack(self, enemy):
        prob = random.randint(1, 10)
        if prob == 1:
            damaged = random.randint(int((3*self.level) - (1.5*self.level)), int((3*self.level) + (1.5*self.level)))
            print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
            time.sleep(0.5)
            print("A critical hit!")
            time.sleep(0.5)
            enemy.lose_health(damaged)
            return enemy.health
        else:
            if (self.type == "Fire" and enemy.type == "Grass") or (self.type == "Water" and enemy.type == "Fire") or (self.type == "Grass" and enemy.type == "Water") or (self.type == "Electric" and enemy.type == "Water") or (self.type == "Grass" and enemy.type == "Electric"):
                damaged = random.randint(int((2*self.level) - self.level), int((2*self.level) + self.level))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                print("It's super effective!")
                time.sleep(0.5)
                enemy.lose_health(damaged)
                return enemy.health
            if (self.type == "Fire" and enemy.type == "Water") or (self.type == "Water" and enemy.type == "Grass") or (self.type == "Grass" and enemy.type == "Fire") or (self.type == "Electric" and enemy.type == "Grass") or (self.type == "Water" and enemy.type == "Electric"):
                damaged = random.randint(int((0.5*self.level) - (0.25*self.level)), int((0.5*self.level) + (0.25*self.level)))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                print("It's not very effective...")
                time.sleep(0.5)
                enemy.lose_health(damaged)
                return enemy.health
            else:
                damaged = random.randint(int((self.level) - (0.5*self.level)), int((self.level) + (0.5*self.level)))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                enemy.lose_health(damaged)
                return enemy.health

for pkmn in gen_one.items():
    name = pkmn[0]
    level = (int(pkmn[1][2]) / 60)
    type = pkmn[1][0]
    PokeString.append(name)
    nayme = Pokemon(name, int(level), type)
    MyPokemon.append(nayme.name)
        #return Pokemon(name, int(level), type)

#print(nayme)
#print(MyPokemon)
#print(PokeString)
BotPokemon = []
for pkmn in MyPokemon:
    BotPokemon.append(pkmn + "1")
print(BotPokemon)
# for pkmn in PokeString:
#     #print(pkmn)
#     BotString.append(str(pkmn + "1"))

#print(BotString)
