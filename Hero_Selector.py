from graphics import*
from User_Input import *
from User_choices import *
from Classes import *


#Hero Selector and shows their values in Hero Window
def select_hero(win,win2,win4,win5,win6):
    selector = userinput("Select your hero:\n 1. Human \n2. Dragoon \n3. Elf \n",win2)
    if selector == "1":
        hero = Human()
        message20 = Text(Point(220,80),"You have chosen to be a Human. \nA human's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {hero.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {hero.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {hero.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {hero.magic}")
        message24.draw(win4)
 
    elif selector == "2":
        hero = Dragoon()
        message20 = Text(Point(220,100),"You have chosen to be a Dragoon. \nA Dragoon's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {hero.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {hero.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {hero.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {hero.magic}")
    elif selector == "3":
        hero = Elf()
        message20 = Text(Point(220,100),"You have chosen to be an Elf. \nA human's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {hero.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {hero.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {hero.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {hero.magic}")
    else:
        print("Only press 1,2,3") 
        select_hero()
    return hero

