from graphics import *
def userinput(message,win2):
    message1 = Text(Point(300,100), message)
    message1.draw(win2)
    inputBox = Entry(Point(300,150), 15)
    inputBox.draw(win2)
    win2.getMouse()
    choice = inputBox.getText()
    inputBox.undraw()
    message1.undraw()
    return choice