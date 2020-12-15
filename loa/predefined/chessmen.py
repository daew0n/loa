# Author: chxhyxn

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return Chessmen("Chessmen")


class Pawn(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 2  # Attack
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


class Rook(Unit):
    
    HP = 26 # Hit Points (health points)    
    ATT = 4  # Attack
    ARM = 2 # Armor
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


class Knight(Unit):
    
    HP = 24 # Hit Points (health points)    
    ATT = 6  # Attack
    ARM = 1 # Armor
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


class Bishop(Unit):
    
    HP = 22 # Hit Points (health points)    
    ATT = 8  # Attack
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


        
class Queen(Unit):
    
    HP = 30 # Hit Points (health points)    
    ATT = 8  # Attack
    ARM = 2 # Armor
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
    
    HP = 30 # Hit Points (health points)    
    ATT = 2  # Attack
    ARM = 8 # Armor
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
        

class Chessmen(Team):
    def initialize(self):
        for i in range(2):
            unit = Pawn(self, "Pawn%02d"%(i+1), i)
            self.units.append(unit)
            
        for i in range(2):
            unit = Rook(self, "Rook%02d"%(i+1), i+2)
            self.units.append(unit)
            
        for i in range(2):
            unit = Knight(self, "Knight%02d"%(i+1), i+4)
            self.units.append(unit)
            
        for i in range(2):
            unit = Bishop(self, "Bishop%02d"%(i+1), i+6)
            self.units.append(unit)
            
        for i in range(1):
            unit = Queen(self, "Queen", i+8)
            self.units.append(unit)
            
        for i in range(1):
            unit = King(self, "King", i+9)
            self.units.append(unit)


class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))