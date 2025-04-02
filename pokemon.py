import time
import random
import os

# My first game

"""
                         G A M E  I M P R O V E M E N T S


Lowercase letters for pokemon choices
Press enter to continue in the UI
Look into pygame
Movesets
EXP

"""

""" P O K E M O N  D A T A """
#reads the csv of all pokemon
def read_csv(filename):
    infile = open(filename, 'r').read()
    lines = infile.split('\n')[:-1]
    lines = [line.split(',') for line in lines]
    return lines[1:]

filename = "Kanto Pokemon Spreadsheet.csv"
lines = read_csv(filename)

#initializes a dictionary with the pokemon and their stats
def pokedexter(lines):
    pokedex = {}
    for line in lines:
        pokedex[line[1]] = line[2:]
    return pokedex

pokedex = pokedexter(lines)

#chooses only the first generation of pokemon
def genx(pokedex):
    genx = {}
    for pkmn in pokedex:
        stats = pokedex[pkmn]
        if " " not in pkmn:
            if stats[9] == "1":
                genx[pkmn] = stats
    return genx

gen_one = genx(pokedex)

""" G A M E  E N G I N E """

#pokemon class with their functionalities
class Pokemon:
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
            print("Your pokemon was revived! {name} now has {health} HP.".format(name=self.name, health=self.health))
            return self.health
        else:
            print("Your pokemon is not dead!")

    # def moveset(self):
    #     if self.type == "Fire":
    #         if self.level < 5:
    #             move = input()
    #             print("Press '1' to use Tackle")
    #             if self.level <= 5
    #                 print("Press '2' to use Ember")
    #                 if self.level >= 8:
    #                     print("Press '3' to use Flamethrower")
    #             if move == "1":
    #             if move == "2":
    #             if move == "3":

    def attack(self, enemy):
        prob = random.randint(1, 10)
        if prob == 1:
            damaged = random.randint(int((2.5*self.level) - (1.25*self.level)), int((2.5*self.level) + (1.25*self.level)))
            print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
            time.sleep(0.5)
            print("A critical hit!")
            time.sleep(1)
            enemy.lose_health(damaged)
            return enemy.health
        else:
            if ((self.type == "Fire" and enemy.type == "Grass") or (self.type == "Water" and enemy.type == "Fire") or (self.type == "Grass" and enemy.type == "Water")
                or (self.type == "Electric" and enemy.type == "Water") or (self.type == "Grass" and enemy.type == "Electric") or (self.type == "Fire" and enemy.type == "Ice")
                or (self.type == "Fire" and enemy.type == "Bug") or (self.type == "Water" and enemy.type == "Rock") or (self.type == "Electric" and enemy.type == "Flying")
                or (self.type == "Grass" and enemy.type == "Ground") or (self.type == "Grass" and enemy.type == "Rock") or (self.type == "Ice" and enemy.type == "Grass")
                or (self.type == "Ice" and enemy.type == "Ground") or (self.type == "Ice" and enemy.type == "Flying") or (self.type == "Ice" and enemy.type == "Dragon")
                or (self.type == "Fighting" and enemy.type == "Normal") or (self.type == "Fighting" and enemy.type == "Ice") or (self.type == "Fighting" and enemy.type == "Rock")
                or (self.type == "Poison" and enemy.type == "Grass") or (self.type == "Poison" and enemy.type == "Bug") or (self.type == "Ground" and enemy.type == "Fire")
                or (self.type == "Ground" and enemy.type == "Electric") or (self.type == "Ground" and enemy.type == "Poison") or (self.type == "Ground" and enemy.type == "Rock")
                or (self.type == "Flying" and enemy.type == "Grass") or (self.type == "Flying" and enemy.type == "Fighting") or (self.type == "Flying" and enemy.type == "Bug")
                or (self.type == "Psychic" and enemy.type == "Fighting") or (self.type == "Psychic" and enemy.type == "Poison") or (self.type == "Bug" and enemy.type == "Grass")
                or (self.type == "Bug" and enemy.type == "Poison") or (self.type == "Bug" and enemy.type == "Psychic") or (self.type == "Rock" and enemy.type == "Fire")
                or (self.type == "Rock" and enemy.type == "Ice") or (self.type == "Rock" and enemy.type == "Flying") or (self.type == "Rock" and enemy.type == "Bug")
                or (self.type == "Ghost" and enemy.type == "Ghost") or (self.type == "Dragon" and enemy.type == "Dragon")):
                damaged = random.randint(int((2*self.level) - self.level), int((2*self.level) + self.level))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                print("It's super effective!")
                time.sleep(1)
                enemy.lose_health(damaged)
                return enemy.health
            if ((self.type == "Fire" and enemy.type == "Water") or (self.type == "Water" and enemy.type == "Grass") or (self.type == "Grass" and enemy.type == "Fire")
                or (self.type == "Electric" and enemy.type == "Grass") or (self.type == "Water" and enemy.type == "Electric") or (self.type == "Normal" and enemy.type == "Rock")
                or (self.type == "Fire" and enemy.type == "Fire") or (self.type == "Fire" and enemy.type == "Rock") or (self.type == "Fire" and enemy.type == "Dragon")
                or (self.type == "Water" and enemy.type == "Water") or (self.type == "Water" and enemy.type == "Dragon") or (self.type == "Electric" and enemy.type == "Electric")
                or (self.type == "Electric" and enemy.type == "Dragon") or (self.type == "Grass" and enemy.type == "Grass") or (self.type == "Grass" and enemy.type == "Poison")
                or (self.type == "Grass" and enemy.type == "Flying") or (self.type == "Grass" and enemy.type == "Bug") or (self.type == "Grass" and enemy.type == "Dragon")
                or (self.type == "Ice" and enemy.type == "Water") or (self.type == "Ice" and enemy.type == "Ice") or (self.type == "Fighting" and enemy.type == "Poison")
                or (self.type == "Fighting" and enemy.type == "Flying") or (self.type == "Fighting" and enemy.type == "Psychic") or (self.type == "Fighting" and enemy.type == "Bug")
                or (self.type == "Poison" and enemy.type == "Poison") or (self.type == "Poison" and enemy.type == "Ground") or (self.type == "Poison" and enemy.type == "Rock")
                or (self.type == "Poison" and enemy.type == "Ghost") or (self.type == "Ground" and enemy.type == "Grass") or (self.type == "Ground" and enemy.type == "Bug")
                or (self.type == "Flying" and enemy.type == "Electric") or (self.type == "Flying" and enemy.type == "Rock") or (self.type == "Psychic" and enemy.type == "Psychic")
                or (self.type == "Bug" and enemy.type == "Fire") or (self.type == "Bug" and enemy.type == "Fighting") or (self.type == "Bug" and enemy.type == "Flying")
                or (self.type == "Rock" and enemy.type == "Fighting") or (self.type == "Rock" and enemy.type == "Flying")):
                damaged = random.randint(int((0.5*self.level) - (0.25*self.level)), int((0.5*self.level) + (0.25*self.level)))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                print("It's not very effective...")
                time.sleep(1)
                enemy.lose_health(damaged)
                return enemy.health
            if ((self.type == "Normal" and enemy.type == "Ghost") or (self.type == "Ghost" and enemy.type == "Normal") or (self.type == "Ghost" and enemy.type == "Psychic")
                or (self.type == "Electric" and enemy.type == "Ground") or (self.type == "Fighting" and enemy.type == "Ghost") or (self.type == "Ground" and enemy.type == "Flying")):
                damaged = 0
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                print("It has no effect...")
                time.sleep(1)
                enemy.lose_health(damaged)
                return enemy.health
            else:
                damaged = random.randint(int((self.level) - (0.5*self.level)), int((self.level) + (0.5*self.level)))
                print("{name} attacked {enemyname} for {dmg} damage".format(name=self.name, enemyname=enemy.name, dmg=damaged))
                time.sleep(0.5)
                enemy.lose_health(damaged)
                return enemy.health

#class with trainers functionalities
class Trainer:
    def __init__(self, name, pokemons, num_potions):
        self.name = name
        self.pokemons = pokemons
        self.potions = num_potions
        self.current_pokemon = 0

    def __repr__(self):
        for i in range(len(self.pokemons)):
            print("{names}'s level {level} {name} has {health} health out of {max_health} total health".format(names=self.name, level=self.pokemons[i].level, name=self.pokemons[i].name, max_health=self.pokemons[i].max_health, health=self.pokemons[i].health))
            time.sleep(1)
        return "{name}'s active pokemon is {current_pokemon}.".format(name=self.name, current_pokemon=self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        if self.pokemons[new_active].is_knocked_out == 1:
            print("{name} is knocked out! They cannot be used for battle!".format(name=self.pokemons[new_active].name))
        else:
            #print("{name}, back in your ball, bitch!".format(name=self.pokemons[self.current_pokemon].name))
            print("Go {current_pokemon}!".format(current_pokemon=self.pokemons[new_active].name))
            self.current_pokemon = new_active
            time.sleep(0.5)
            #use_potion, attack_other_trainer

    def use_potion(self, which):
        if self.potions > 0:
            if which <= len(self.pokemons) and which >= 0:
                self.pokemons[which].gain_health()
                self.potions -= 1
        else:
            print("You don't have any potions left dummy!")

    def fightplayer(self, other_trainer):
        if len(self.pokemons) > 0 and len(other_trainer.pokemons) > 0:
            self.pokemons[self.current_pokemon].attack(other_trainer.pokemons[other_trainer.current_pokemon])
            time.sleep(1)
        else:
            if len(self.pokemons) > 0 and len(other_trainer.pokemons) == 0:
                print("Congratulations, you won the game!!!")
            if len(other_trainer.pokemons) > 0 and len(self.pokemons) == 0:
                print("Wow, you lost to a bot. You must be feeling really low...")

""" E X T R A S """
MyPokemon = []
BotPokemon = []
PokeString = []

for pkmn in pokedex.items():
    name = pkmn[0]
    level = (int(pkmn[1][2]) / 60)
    type = pkmn[1][0]
    PokeString.append(name)
    nayme = Pokemon(name, int(level), type)
    MyPokemon.append(nayme)
    BotPokemon.append(nayme)

BotNames = ['BOT Jasper', 'BOT Shrek', 'BOT Karen']

""" I N T R O """

def Intro():
    os.system('clear')
    print("""
                                  ___
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")
    time.sleep(0.5)
    print("Pokemon Trash edition, version 1.2")
    time.sleep(1)
    print("What is your name?")
    name = input()
    os.system('clear')
    print("Select your first Pokemon for battle by typing their name:...")
    time.sleep(1)
    print("Type 'l' to view a list of pokemon.")
    time.sleep(0.5)
    print("Type 'r' to choose a random Pokemon.")
    playerpkmn = []
    pokemon1 = input()
    while pokemon1 not in PokeString or pokemon1 == 'r':
        if pokemon1 != 'r':
            if pokemon1 == 'l':
                random.shuffle(PokeString)
                for pkmn in PokeString:
                    print(pkmn)
                    time.sleep(0.001)
            if pokemon1 == 'o':
                for pkmn in PokeString:
                    print(pkmn)
                    time.sleep(0.01)
            print("Please type a Pokemon from the list.")
            pokemon1 = input()
        else:
            pokemon1 = random.choice(PokeString)
    #print("Good!")
    playerpkmn.append(pokemon1)
    PokeString.remove(pokemon1)
    print("Choose your second Pokemon:...")
    time.sleep(1)
    print("Type 'l' to view a list of all original 151 pokemon.")
    time.sleep(0.5)
    print("Type 'r' to choose a random Pokemon.")
    pokemon2 = input()
    while pokemon2 not in PokeString or pokemon2 == 'r':
        if pokemon2 != 'r':
            if pokemon2 == 'l':
                random.shuffle(PokeString)
                for pkmn in PokeString:
                    print(pkmn)
                    time.sleep(0.01)
            if pokemon2 == 'o':
                for pkmn in PokeString:
                    print(pkmn)
                    time.sleep(0.01)
            print("Please type a Pokemon from the list.")
            pokemon2 = input()
        else:
            pokemon2 = random.choice(PokeString)
    #print("Good!")
    time.sleep(1)
    playerpkmn.append(pokemon2)
    PokeString.remove(pokemon2)
    os.system('clear')
    time.sleep(1)
    plpkmn = []
    for i in MyPokemon:
        for j in playerpkmn:
            if j == i.name:
                plpkmn.append(i)
    player1 = Trainer(name, plpkmn, 2)
    plstring = []
    for pkmn in plpkmn:
        pstring = str(pkmn.name)
        plstring.append(pstring)
    #print(plstring)
    #time.sleep(10)
    print(player1)
    time.sleep(2)
    BotName = random.choice(BotNames)
    BotP = random.sample(PokeString, 2)
    BotPkmn = []
    for i in MyPokemon:
        for j in BotP:
            if j == i.name:
                BotPkmn.append(i)
    print("{name} will be fighting against {BotNames}!".format(name=name, BotNames=BotName))
    BOT = Trainer(BotName, BotPkmn, 2)
    time.sleep(2)
    print(BOT)
    time.sleep(2)
    print("You and {BOT} decide a coin flip is the most fair way to choose who starts.".format(BOT=BotName))
    time.sleep(2)
    print("Heads or Tails?")
    hort = ("Heads", "Tails")
    win = random.choice(hort)
    guess = input()
    if guess == win:
        print("Lucky bastard.")
        time.sleep(1)
        return game(player1, plpkmn, plstring, BOT, BotPkmn, 0)
        os.system('clear')
    else:
        print("Rough".format(Bot=BotName))
        time.sleep(1)
        return game(player1, plpkmn, plstring, BOT, BotPkmn, 1)
        os.system('clear')


""" UI """
def updateInterface(player1):
    print("Pokemon Trash edition, v1.2")
    print("name : " + player1.name)
    print("active pokemon : " + player1.pokemons[player1.current_pokemon].name)
    print("potions : " + str(player1.potions))
    print("\n")

""" G A M E  T E S T I N G """
plpkmn = random.sample(MyPokemon, 2)
plstring = []
for i in plpkmn:
    for j in PokeString:
        if j == i.name:
            plstring.append(j)
BotPkmn = [random.sample(BotPokemon, 2)]
player1 = Trainer("Kappy", plpkmn, 2)
BOT = Trainer("BOT Charlie", BotPkmn, 2)

""" G A M E """

def game(player1, plpkmn, plstring, BOT, BotPkmn, start):
    os.system('clear')
    updateInterface(player1)
    if start == 0:
        print("It is your turn!")
        time.sleep(1)
        for pkmn in player1.pokemons:
            print(pkmn)
        time.sleep(1)
        print('\n')
        print(BOT)
        time.sleep(1.5)
        print('\n')
        print("What would you like to do?")
        time.sleep(0.5)
        print("Type 'a' to attack the enemy Pokemon, \nType 's' to switch active Pokemon, \nType 'u' to use a potion.")
        move = input()
        if move != 'u' and move != 's' and move != 'a':
            os.system('clear')
            updateInterface(player1)
            print("Please either type 'a' or 's' or 'u'")
            move = input()
        if move == 'a':
            os.system('clear')
            updateInterface(player1)
            player1.fightplayer(BOT)
        if move == 's':
            os.system('clear')
            updateInterface(player1)
            if len(player1.pokemons) > 1:
                if len(player1.pokemons) > 1:
                    print("What Pokemon would you like to switch to?")
                    time.sleep(0.5)
                    for pkmn in plstring:
                        print(pkmn)
                    pokemon1 = input()
                    while pokemon1 not in plstring:
                        print("Please type a Pokemon from the list.")
                        pokemon1 = input()
                    #print("Good!")
                    for i in range(len(player1.pokemons)):
                        if player1.pokemons[i].name == pokemon1:
                            time.sleep(1)
                            player1.switch_active_pokemon(i)
            else:
                print("You cannot switch active Pokemon.")
        if move == 'u':
            os.system('clear')
            updateInterface(player1)
            if len(player1.pokemons) > 1:
                if len(player1.pokemons) > 1:
                    print("What Pokemon would you like to heal?")
                    time.sleep(0.5)
                    for pkmn in plstring:
                        print(pkmn)
                    pokemon1 = input()
                    while pokemon1 not in plstring:
                        print("Please type a Pokemon from the list.")
                        pokemon1 = input()
                    print("Good!")
                    for i in range(len(player1.pokemons)):
                        if player1.pokemons[i].name == pokemon1:
                            time.sleep(1)
                            player1.use_potion(i)
            else:
                player1.use_potion(0)
        time.sleep(1)
    os.system('clear')
    updateInterface(player1)
    print("It is {Bot}'s turn!".format(Bot=BOT.name))
    time.sleep(1)
    for bt in BotPkmn:
        if bt.is_knocked_out == 1:
            BotPkmn.remove(bt)
            if len(player1.pokemons) > 0 and len(BOT.pokemons) == 0:
                print("Congratulations, you won the game!!!")
                time.sleep(1)
                return endcredits()
            if len(BOT.pokemons) > 0 and len(player1.pokemons) == 0:
                print("Wow, you lost to a bot. You must be feeling really low...")
                time.sleep(1)
                return endcredits()
            BOT.switch_active_pokemon(0)
    BOT.fightplayer(player1)
    time.sleep(0.5)
    turn = 0
    time.sleep(1)
    for i in range(50):
        if turn == 0:
            os.system('clear')
            updateInterface(player1)
            for pk in plpkmn:
                if pk.is_knocked_out == 1:
                    plpkmn.remove(pk)
                    if len(player1.pokemons) > 0 and len(BOT.pokemons) == 0:
                        print("Congratulations, you won the game!!!")
                        time.sleep(1)
                        return endcredits()
                    if len(BOT.pokemons) > 0 and len(player1.pokemons) == 0:
                        print("Wow, you lost to a bot. You must be feeling really low...")
                        time.sleep(1)
                        return endcredits()
                    player1.switch_active_pokemon(0)
            print("It is your turn!")
            time.sleep(1)
            for pkmn in player1.pokemons:
                print(pkmn)
            time.sleep(1)
            print('\n')
            print(BOT)
            time.sleep(1.5)
            print('\n')
            print("What would you like to do?")
            print("Type 'a' to attack the enemy Pokemon, \nType 's' to switch active Pokemon, \nType 'u' to use a potion.")
            move = input()
            if move != 'u' and move != 's' and move != 'a':
                os.system('clear')
                updateInterface(player1)
                print("Please either type 'a' or 's' or 'u'")
                move = input()
            if move == 'a':
                os.system('clear')
                updateInterface(player1)
                player1.fightplayer(BOT)
            if move == 's':
                os.system('clear')
                updateInterface(player1)
                if len(player1.pokemons) > 1:
                    if len(player1.pokemons) > 1:
                        print("What Pokemon would you like to switch to?")
                        time.sleep(0.5)
                        for pkmn in plstring:
                            print(pkmn)
                        pokemon1 = input()
                        while pokemon1 not in plstring:
                            print("Please type a Pokemon from the list.")
                            pokemon1 = input()
                        print("Good!")
                        for i in range(len(player1.pokemons)):
                            if player1.pokemons[i].name == pokemon1:
                                time.sleep(1)
                                player1.switch_active_pokemon(i)
                else:
                    print("You cannot switch active Pokemon.")
            if move == 'u':
                os.system('clear')
                updateInterface(player1)
                if len(player1.pokemons) > 1:
                    if len(player1.pokemons) > 1:
                        print("What Pokemon would you like to heal?")
                        time.sleep(0.5)
                        for pkmn in plstring:
                            print(pkmn)
                        pokemon1 = input()
                        while pokemon1 not in plstring:
                            print("Please type a Pokemon from the list.")
                            pokemon1 = input()
                        #print("Good!")
                        for i in range(len(player1.pokemons)):
                            if player1.pokemons[i].name == pokemon1:
                                time.sleep(1)
                                player1.use_potion(i)
                else:
                    player1.use_potion(0)
            turn = 1
            time.sleep(1)
        os.system('clear')
        updateInterface(player1)
        if turn == 1:
            for bt in BotPkmn:
                if bt.is_knocked_out == 1:
                    BotPkmn.remove(bt)
                    if len(player1.pokemons) > 0 and len(BOT.pokemons) == 0:
                        print("Congratulations, you won the game!!!")
                        time.sleep(1)
                        return endcredits()
                    if len(BOT.pokemons) > 0 and len(player1.pokemons) == 0:
                        print("Wow, you lost to a bot. You must be feeling really low...")
                        time.sleep(1)
                        return endcredits()
                    BOT.switch_active_pokemon(0)
            os.system('clear')
            updateInterface(player1)
            print("It is {Bot}'s turn!".format(Bot=BOT.name))
            time.sleep(1)
            BOT.fightplayer(player1)
            turn = 0
            time.sleep(1)

def endcredits():
    print("""
       \:.             .:/
        \``._________.''/
         \             /
 .--.--, / .':.   .':. "\"
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
           :-._____.-:
          `''       `''
    """)
    time.sleep(2)
    print("Thanks for playing my game!")
def main():
    Intro()
    #game(player1, plpkmn, plstring, BOT, BotPkmn, 0)
    #endcredits()
main()
