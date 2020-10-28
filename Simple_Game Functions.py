import time 
import random
from graphics import*
from Welcome import *
from Classes import *
from Hero_Selector import *



def enemy_selection(orc, goblin,vampire):
    enemylist = [orc, goblin, vampire]
    chance = random.randint(0,2)
    enemy = enemylist[chance]
    return enemy


def main():
    intro(GraphWin('Text_Based_Adventure', 690,800), GraphWin('Second Window of Adventure', 580,300), GraphWin('Hero', 400,300), GraphWin('BattleBox',300,300))
    

main()
