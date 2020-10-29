from graphics import *
import random
from User_Input import *
from User_choices import *
from Classes import *
from Hero_Selector import *


# An random enemy function that chooses between these enemies to encounter in battle
def enemy_selection(orc, goblin, vampire):
    enemylist = [Orc(), Goblin(), Vampire()]
    chance = random.randint(0,2)
    enemy = enemylist[chance]
    return enemy
   
#The battle function that opens up 2 Battle windows. A main one called battle box and another one if there isnt anymore space.
def battle(win,win2,win4,win5,win6,hero):
    enemy = enemy_selection(Orc,Goblin,Vampire)
    message31 = Text(Point(350,230),"You leave the kingdom and after a long journey you reach Mount Shriek.")
    message31.draw(win)
    message32 = Text(Point(210,40),f"An enemy {enemy.getname()} has appeared before you.")
    message32.draw(win5)

    

    while enemy.health > 0:
        choice = userinput("You have 2 options:\n2. Magic \n3. Run",win2)
        if choice == "2":
            message39 = Text(Point(210,80),f"(Casting spell)..Perish {enemy.getname()}!\n The flames of this spell will render you useless.")
            message39.draw(win5)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - hero.strength
                message40 = Text(Point(210,200),f"You hurt the {enemy.getname()} Their health is {enemy.health}")
                message40.draw(win5)
                if enemy.health > 0:
                    hero.health = hero.health - (enemy.strength / hero.defense)
                    message41 = Text(Point(210,140),f"The {enemy.getname()}, attack you. \nYou have {hero.health}, health remaining.")
                    message41.draw(win6)
                else:
                    if enemy.getname() == "goblin":
                        enemy.health = 30
                    elif enemy.getname() == "orc":
                        enemy.health = 20
                    elif enemy.getname() == "vampire":
                        enemy.health = 60
                    message42 = Text(Point(210,200),f"You have defeated the {enemy.getname()}")
                    message42.draw(win6)
                    message80 = Text(Point(300,100),"Click to continue: ")
                    message80.draw(win2)
                    win2.getMouse()
                    message80.undraw()
                    win5.close()
                    win6.close()
                    break
            else:
                message43 = Text(Point(210,140),f"For some reason you forgot how to cast your spell,\n the enemy {enemy.getname()} takes this chance to attack you.") 
                message43.draw(win5)   
                hero.health = hero.health - enemy.strength
                message44 = Text(Point(210,170),f"Because of this, you have {hero.health} health remaining.")
                message44.draw(win5)

        elif choice == "3":
            message45 = Text(Point(210,60),f"I must flee... {enemy.getname()}'s power is overwhelming")
            message45.draw(win5)
            flee = random.randint(1,10)
            if flee > 4:
                message46 = Text(Point(210,80),f"You got away")
                message46.draw(win5)
                message83 = Text(Point(300,100),"Click to continue: ")
                message83.draw(win2)
                win2.getMouse()
                message83.undraw()
                win5.close()
                win6.close()
                break
            else:
                message46 = Text(Point(210,90),f"You tried to flee but smacked the wall behind you. The {enemy.getname()} attacks.")
                message46.draw(win5)
                hero.health = hero.health -  enemy.strength
                message47 = Text(Point(210,110),f"Your health is now {hero.health}")
                message47.draw(win5)
        else:
            message48 = Text(Point(210,110),"Number not allowed, must be between 1, 2, or 3")
            message48.draw(win5)