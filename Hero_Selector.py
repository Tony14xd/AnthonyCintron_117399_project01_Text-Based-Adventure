from graphics import*
from User_Input import *
from User_choices import *
from Classes import *



def select_hero(win,win2,win4):
    selector = userinput("Select your hero: 1. Human \n2. Dragoon \n3. Elf \n",win2)
    if selector == "1":
        character = Human()
        message20 = Text(Point(220,80),"You have chosen to be a Human. \nA human's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {character.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {character.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {character.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {character.magic}")
        message24.draw(win4)
 
    elif selector == "2":
        character = Dragoon()
        message20 = Text(Point(220,100),"You have chosen to be a Dragoon. A Dragoon's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {character.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {character.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {character.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {character.magic}")
    elif selector == "3":
        character = Elf()
        message20 = Text(Point(220,100),"You have chosen to be an Elf. A human's statistics are the following: ")
        message20.draw(win4)
        message21 = Text(Point(220,130),f"Health -> {character.health}") 
        message21.draw(win4)
        message22 = Text(Point(220,150),f"Strength -> {character.strength}")
        message22.draw(win4)
        message23 = Text(Point(220,170),f"Defense ->  {character.defense}")
        message23.draw(win4)
        message24 = Text(Point(220,190),f"Magic ->  {character.magic}")
    else:
        print("Only press 1,2,3") 
        select_hero()
    return character

character = select_hero