import os

player = {
    "name" : "",
    "level": "",
    "health": 100,
    "pokemon": [
        "Charmander",
        "Squirtle"
    ],
    "active_pokemon": 0
}

map = [
    ["#","#","#"],
    ["#","#","#"],
    ["#","#","#"]
]

player_pos = [1,1]

def updateInterface():
    print("name  : " + player["name"])
    print("level : " + str(player["level"]))
    print("health: " + str(player["health"]))
    print("\n")
    for num in range(len(player["pokemon"])):
        temp = ""
        if num == player["active_pokemon"]:
            temp += "> "
        temp += player["pokemon"][num]
        print(temp)
    print("\n")
    print("\n")
    for n in range(0, len(map)):
        level = ""
        for i in range(0, len(map[0])):
            if i==player_pos[1] and n==player_pos[0]:
                level = level + "o"
            else :
                level = level + map[n][i]
        print(level)


def init():
    player["name"] = input("Enter name \n")
    player["level"] = 0

def startCombat():
    command = ""
    while(command != "stop"):
        os.system('clear')
        updateInterface()
        command = input("<a> Attack \t \t <s> Switch \n")
        if command=="s":
            player_pos[0] = player_pos[0]+1
        elif command=="w":
            player_pos[0] = player_pos[0]-1

init()
startCombat()
