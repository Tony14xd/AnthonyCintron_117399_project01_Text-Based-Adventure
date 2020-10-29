import time 
import random
from graphics import*
from Welcome import *
from Classes import *
from Hero_Selector import *


def main():
    intro(GraphWin('Text_Based_Adventure', 690,800), GraphWin('Input Box', 580,300), GraphWin('Hero', 400,300), GraphWin('BattleBox',400,400),GraphWin('BattleBox 2',400,400))
    

main()
