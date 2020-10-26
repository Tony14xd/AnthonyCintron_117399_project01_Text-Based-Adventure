from graphics import *

class Human:
    def __init__(self,name = "Human", health = 200, s = 70, defense = 50, magic = 20):
        self.name = name
        self.health = health
        self.strength = s
        self.defense = defense
        self.magic = magic

    def getstrength(self):
        return self.strength

    def setstrength(self,s):
        self.strength = s


class Dragoon:
    def __init__(self,name = "Dragoon", health = 100, strength = 70, defense = 20, magic = 70):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic

    def getstrength(self):
        return self.strength

class Orc:
    def __init__(self,name= "Human", health = 150, strength = 100, defense = 20, magic = 0):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic

    def getname(self):
        return self.name
    
    def getstrength(self):
        return self.strength


class Elf:
    def __init__(self,name = "Elf", health = 120, strength = 50, defense = 60, magic = 60):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic

    def getname(self):
        return self.name
    
    def getstrength(self):
        return self.strength


class Goblin:
    def __init__(self,name = "Goblin", health = 30, strength = 50, defense = 50, magic = 50):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic

    def getname(self):
        return self.name

    def getstrength(self):
        return self.strength

class Vampire:
    def __init__(self,name = "Goblin", health = 60, strength = 80, defense = 20, magic = 5):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic
    
    def getstrength(self):
        return self.strength

    def getname(self):
        return self.name


