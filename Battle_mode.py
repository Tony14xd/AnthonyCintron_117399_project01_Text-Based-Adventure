from graphics import *
import random
from User_Input import *
from User_choices import *
from Classes import *
from Hero_Selector import *

def select_hero(win,win2,win4):
    selector = userinput("Select your hero: 1. Human \n2. Dragoon \n3. Elf \n",win2)
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
        message20 = Text(Point(220,100),"You have chosen to be a Dragoon. A Dragoon's statistics are the following: ")
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
        message20 = Text(Point(220,100),"You have chosen to be an Elf. A human's statistics are the following: ")
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



def enemy_selection(orc, goblin, vampire):
    enemylist = [orc(), goblin(), vampire()]
    chance = random.randint(0,2)
    enemy = enemylist[chance]
    return enemy

def battle(win,win2,win4,hero = Human()):
    enemy = enemy_selection(Orc,Goblin,Vampire)
    message31 = Text(Point(350,230),"You leave the kingdom and after a long journey you reach Mount Shriek.")
    message31.draw(win)
    message32 = Text(Point(350,250),f"An enemy {enemy.getname()} has appeared before you.")
    message32.draw(win)

    

    while enemy.health > 0:
        choice = userinput("You have 3 options:\n1. Sword \n2. Magic \n3. Run",win2)
        if choice == "1":
            message33 = Text(Point(350,360),f"(unsheathes sword)..Die {enemy.getname()}! Scum, I shall not let you plague our kingdom any further.")
            message33.draw(win)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - hero.strength
                message34 = Text(Point(350,380),f"You hurt the {enemy.getname()}, Their health is {enemy.health}")
                message34.draw(win)
                if enemy.health > 0:
                    hero.health = hero.health - (enemy.strength / hero.defense)
                    message35 = Text(Point(350,400),f"The {enemy.getname()}, attack you. You have {hero.health},health remaining.")
                    message35.draw(win)
                else:
                    if enemy.getname() == "goblin":
                        enemy.health = 30
                    elif enemy.getname() == "orc":
                        enemy.health = 50
                    elif enemy.getname() == "vampire":
                        enemy.health = 60
                    message36 = Text(Point(350,420),f"You have defeated the {enemy.getname()}")
                    message36.draw(win)
                    break
            else:
                message37 = Text(Point(350,440),f"You get an urge to sneeze, the enemy {enemy.getname()} takes this chance to attack you.")  
                message37.draw(win)  
                hero.health = hero.health - enemy.strength
                message38 = Text(Point(350,460),f"Because of this, you have {hero.health} health remaining.")
                message38.draw


        elif choice == "2":
            print("(Casting spell)..Perish", enemy.getname(),",! The flames of this spell will render you useless.")
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - hero.strength
                print("You hurt the", enemy.getname(), "Their health is",enemy.health)
                if enemy.health > 0:
                    hero.health = hero.health - (enemy.strength / hero.defense)
                    print ("The", enemy.getname(), "attack you. You have", hero.health,"health remaining.")
                else:
                    if enemy.getname() == "goblin":
                        enemy.health = 30
                    elif enemy.getname() == "orc":
                        enemy.health = 50
                    elif enemy.getname() == "vampire":
                        enemy.health = 60
                    print("You have defeated the", enemy.getname())
                    break
            else:
                print("For some reason you forgot how to cast your spell, the enemy", enemy.getname(),"takes this chance to attack you.")    
                hero.health = hero.health - enemy.strength
                print("Because of this, you have", hero.health, "health remaining.")

        elif choice == "3":
            print("I must flee...", enemy.getname(),"'s power is overwhelming")
            flee = random.randint(1,10)
            if flee > 4:
                print ("You got away")
                break
            else:
                print("You tried to flee but smacked the wall behind you. The", enemy.getname(), "attacks.")
                hero.health = hero.health -  enemy.strength
                print("Your health is now",hero.health)
        else:
            print("Number not allowed, must be between 1, 2, or 3")