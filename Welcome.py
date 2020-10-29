from graphics import*
from User_Input import *
from User_choices import *
from First_ask import *
from Hero_Selector import *
from Battle_mode import *

#The Text when being introduced to the game with its respective positioning in graphic

def intro(win,win2,win4,win5,win6):
    message1 = Text(Point(350,70),"Welcome Proud Knight, you have been chosen from a small gifted group of\n"
     " people to join our ranks. You have sworn an oath to protect the Kingdom\n"
     " of RossWell and its people from the maliciousness that dwells\n"
     " within the Kingdom. One must be wary of his surroundings, but as a qualified\n"
     " Knight, you already knew what trouble you would be facing. Now,\n"
     " please tell us your name to begin your journey..!\n")
    message1.draw(win)
    time.sleep(1)

    hero = select_hero(win,win2,win4,win5,win6)
    #select_hero(win,win2,win4)
   
    
    playername = userinput("Enter Your Name: ", win2)
    message2 = Text(Point(350,160),f"What a powerful name that is! We are proud to have you, {playername},\n Now" 
    " go out there and show the world what your capable of!\n")
    message2.draw(win)
    message25 = Text(Point(350,200),"""Your first Task is to head toward Mount Shriek and slay any beast
    you encounter. Make this quick.""")
    message25.draw(win)

    battle(win,win2,win4,win5,win6,hero)
    
    message7 = Text(Point(350,270),"After your daily sweep, you enter a bar to monitor\n"
    "the environment")
    message7.draw(win)
    message8 = Text(Point(350,350),"You see two men having a discussion. You approach the bartender and buy\n"
    "a drink to not seem suspiscious. From your current distance you can overhear their\n"
    "conversation. To your surprise, they are belittling the Knight Order\n"
    "and the Kingdom who you have sworn to protect. This frustrates you thus, \n"
    "you approach their table. You are looking at them from above while they are sitting\n"
    "down enjoying their hard earned alcohol. Do you: ")
    message8.draw(win)
    time.sleep(1)
    choice = userinput("A. Politely ask them why they speak in this manner about their Kingdom?\n"
    "B. Angrily bash their table and spill their alcohol, thus ensuing a potential\n"
    "conflict. C. Look at them menacingly.\n",win2)
    if choice in AnswerA:
        option_ask(win,win2)
    elif choice in AnswerB:
        message16 = Text(Point(350,400), "You break your arm from the force exerted upon the table. Everyone\n"
        "laughs at you as you walk out the front door. You retire from being an honorable Knight\n\n"
        "You Lose")
        message16.draw(win)
        win.getMouse()
    elif choice in AnswerC:
        message3 = Text(Point(350,400),"What am I? The man on the left replies saying: A Knight?. \nYou"
        "have the biggest smirk on your face behind your helmet and say: You're Goddamn Right.\n"
        "\n\nPretty quick ending but hey, you left the scene pretty cool.\n")
        message3.draw(win)
        win.getMouse()
    else:
        print(must)

