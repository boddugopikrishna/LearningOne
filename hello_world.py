from random import *
dict_bat = {"KOHLI":11,"ROHIT":10,"DHAWAN":9.5,"RAYUDU":9,"FINCH":9,"KAWAJA":8.5,"MARSH":9.5,"HANDSCOMB":8.5}
dict_All = {"JADHAV":8.5,"JADEJA":8.5,"STOINIS":9.5,"MAXWELL":9}
dict_bow = {"KULDEEP":9,"BUMRAH":9.5,"SHAMI":8.5,"CUMMINS":9,"COULTER":8.5,"ZAMPA":9.5,"JASON":8.5}
#dict_allplayers = dict_bat + dict_All + dict_All
list_bat = list(dict_bat.keys())
list_All = list(dict_All.keys())
list_bow = list(dict_bow.keys())
#print(dict_bat[choice(list_bat)])
selected_by = {"KOHLI":91.2,"ROHIT":77.21,"DHAWAN":25.37,"RAYUDU":28.4,"FINCH":27.17,"KAWAJA":81.32,"MARSH":6.47,"HANDSCOMB":24.79,"KULDEEP":66.84,"BUMRAH":72.89,"SHAMI":59.93,"CUMMINS":13.25,"COULTER":82.62,"ZAMPA":43.26,"JASON":8.99,"JADHAV":80,"JADEJA":11.68,"STOINIS":64.26,"MAXWELL":87.01}
credits = 0
val = 1

allPlayers_list = [list_bat,list_All,list_bow]
player_count = [5,2,3]
def player_picker(player_list,count):
    list_Team = []
    val = 1
    while val <= count:
        pick = choice(player_list)
        if pick not in list_Team:
            list_Team.append(pick)
            val = val + 1
    return list_Team

def random_players():
    Random_PlayersList = []
    for val in range(3):
        players = player_picker(allPlayers_list[val], player_count[val])
        Random_PlayersList += players
    return Random_PlayersList

def total_credits(players):
    credits = 0
    for val in players:
        if val in dict_bat:
            credits += dict_bat[val]
        elif val in dict_All:
            credits += dict_All[val]
        elif val in dict_bow:
            credits += dict_bow[val]
    return credits

count = 1
final_list = []
while count <= 6:
    players = random_players()
    if("STOINIS" in players and "DHAWAN" in players and "FINCH" in players and "MARSH" in players and "KOHLI" in players):
        if total_credits(players) <= 91.5:
            print(players)
            final_list.append(players)
            count = count + 1
import os
with open("teams2.txt",mode="w+") as f:
    for val in final_list:
        f.write("Team Details" + "\n")
        final_string = ""
        for name in val:
            final_string += name + ":" + str(selected_by[name]) + "\n"
        f.write(final_string)
        f.write("\n")



