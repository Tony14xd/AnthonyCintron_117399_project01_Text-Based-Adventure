from graphics import *
import random
from User_Input import *
from User_choices import *
from Classes import *
from Hero_Selector import *


def enemy_selection(orc, goblin, vampire):
    enemylist = [orc(), goblin(), vampire()]
    chance = random.randint(0,2)
    enemy = enemylist[chance]
    return enemy
   

def battle(win,win2,win4,win5,hero):
    enemy = enemy_selection(Orc,Goblin,Vampire)
    message31 = Text(Point(350,230),"You leave the kingdom and after a long journey you reach Mount Shriek.")
    message31.draw(win)
    message32 = Text(Point(350,250),f"An enemy {enemy.getname()} has appeared before you.")
    message32.draw(win)

    

    while enemy.health > 0:
        choice = userinput("You have 3 options:\n1. Sword \n2. Magic \n3. Run",win2)
        if choice == "1":
            message33 = Text(Point(260,60),f"(unsheathes sword)..Die {enemy.getname()}!\n Scum, I shall not let you plague our kingdom any further.")
            message33.draw(win5)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - hero.strength
                message34 = Text(Point(260,80),f"You hurt the {enemy.getname()}, Their health is {enemy.health}")
                message34.draw(win5)
                if enemy.health > 0:
                    hero.health = hero.health - (enemy.strength / hero.defense)
                    message35 = Text(Point(260,100),f"The {enemy.getname()}, attack you. You have {hero.health},health remaining.")
                    message35.draw(win5)
                else:
                    if enemy.getname() == "goblin":
                        enemy.health = 30
                    elif enemy.getname() == "orc":
                        enemy.health = 50
                    elif enemy.getname() == "vampire":
                        enemy.health = 60
                    message36 = Text(Point(260,120),f"You have defeated the {enemy.getname()}")
                    message36.draw(win5)
                    win2.getMouse()
                    win5.close()
                    
            else:
                message37 = Text(Point(260,440),f"You get an urge to sneeze, the enemy {enemy.getname()} takes this chance to attack you.")  
                message37.draw(win5)  
                hero.health = hero.health - enemy.strength
                message38 = Text(Point(260,460),f"Because of this, you have {hero.health} health remaining.")
                message38.draw(win5)
                



        elif choice == "2":
            message39 = Text(Point(240,50),f"(Casting spell)..Perish {enemy.getname()}! The flames of this spell will render you useless.")
            message39.draw(win5)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - hero.strength
                message40 = Text(Point(240,70),f"You hurt the {enemy.getname()} Their health is {enemy.health}")
                message40.draw(win5)
                if enemy.health > 0:
                    hero.health = hero.health - (enemy.strength / hero.defense)
                    message41 = Text(Point(240,90),f"The {enemy.getname()}, attack you. You have {hero.health}, health remaining.")
                    message41.draw(win5)
                else:
                    if enemy.getname() == "goblin":
                        enemy.health = 30
                    elif enemy.getname() == "orc":
                        enemy.health = 50
                    elif enemy.getname() == "vampire":
                        enemy.health = 60
                    message42 = Text(Point(240,120),f"You have defeated the {enemy.getname()}")
                    message42.draw(win2)
                    break
            else:
                message43 = Text(Point(240,140),f"For some reason you forgot how to cast your spell,\n the enemy {enemy.getname()} takes this chance to attack you.") 
                message43.draw(win5)   
                hero.health = hero.health - enemy.strength
                message44 = Text(Point(240,160),f"Because of this, you have {hero.health} health remaining.")
                message44.draw(win5)

        elif choice == "3":
            message45 = Text(Point(240,60),f"I must flee... {enemy.getname()}'s power is overwhelming")
            message45.draw(win5)
            flee = random.randint(1,10)
            if flee > 4:
                message46 = Text(Point(240,80),f"You got away")
                message46.draw(win5)
                break
            else:
                message46 = Text(Point(240,90),f"You tried to flee but smacked the wall behind you. The {enemy.getname()} attacks.")
                message46.draw(win5)
                hero.health = hero.health -  enemy.strength
                message47 = Text(Point(240,110),f"Your health is now {hero.health}")
                message47.draw(win5)
        else:
            message48 = Text(Point(240,110),"Number not allowed, must be between 1, 2, or 3")
            message48.draw(win5)