# Author: suewcho

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return Cards("Cards")


class Heart(Unit):
    
    HP = 17 # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 3 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
        
class Diamond(Unit):
    
    HP = 24 # Hit Points (health points)    
    ATT = 4  # Attack
    ARM = 5 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
        
class Spade(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 8  # Attack
    ARM = 7 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
        
class Joker(Unit):
    
    HP = 25 # Hit Points (health points)    
    ATT = 16  # Attack
    ARM = 0 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
        
class King(Unit):
    
    HP = 25 # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 13 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
        
class Jack(Unit):
    
    HP = 19 # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 6 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Queen(Unit):
    
    HP = 19 # Hit Points (health points)    
    ATT = 15  # Attack
    ARM = 3 # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Cards(Team):
    
    def initialize(self):
        for i in range(0, 2):
            unit = Heart(self, "Heart-%02d"%(i+1), i)
            self.units.append(unit)
            
        for i in range(2, 4):
            unit = Diamond(self, "Diamond-%02d"%(i+1), i)
            self.units.append(unit)
            
        for i in range(4, 6):
            unit = Spade(self, "Spade-%02d"%(i+1), i)
            self.units.append(unit)
            
        self.units.append(Joker(self,"Joker", 6))
        self.units.append(King(self,"King", 7))
        self.units.append(Jack(self,"Jack", 8))
        self.units.append(Queen(self,"Queen", 9))
       

class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))