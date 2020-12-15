# Author: sseong-mi

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return LoL("LoL")


class Leona(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 1  # Attack
    ARM = 19 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        

class Zed(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 14 # Attack
    ARM = 10 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class  DrMundo(Unit):
    
    HP = 40 # Hit Points (health points)    
    ATT = 1 # Attack
    ARM = 6 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Ezreal(Unit):
    
    HP = 15 # Hit Points (health points)    
    ATT = 14 # Attack
    ARM = 14 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Sett(Unit):
    
    HP = 35 # Hit Points (health points)    
    ATT = 10 # Attack
    ARM = 3 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Samira(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 18 # Attack
    ARM = 8 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)      
        
class Amumu(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 9 # Attack
    ARM = 14 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)    
        
class Blitzcrank(Unit):
    
    HP = 25 # Hit Points (health points)    
    ATT = 10 # Attack
    ARM = 10 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)     
        
class Shaco(Unit):
    
    HP = 30 # Hit Points (health points)    
    ATT = 18 # Attack
    ARM = 1 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)   

class Malphite(Unit):
    
    HP = 25 # Hit Points (health points)    
    ATT = 8 # Attack
    ARM = 11 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class LoL(Team):
    
    def initialize(self):
        unit = Leona(self, "Leona", 0)
        self.units.append(unit)
        
        unit = Zed(self, "Zed", 1)
        self.units.append(unit)
        
        unit =  DrMundo(self, " DrMundo", 2)
        self.units.append(unit)
        
        unit = Ezreal(self, "Ezreal", 3)
        self.units.append(unit)
        
        unit = Sett(self, "Sett", 4)
        self.units.append(unit)
        
        unit = Samira(self, "Samira", 5)
        self.units.append(unit)
        
        unit = Amumu(self, "Amumu", 6)
        self.units.append(unit)
        
        unit = Blitzcrank(self, "Blitzcrank", 7)
        self.units.append(unit)
        
        unit = Shaco(self, "Shaco", 8)
        self.units.append(unit)
        
        unit = Malphite(self, "Malphite", 9)
        self.units.append(unit)


class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))