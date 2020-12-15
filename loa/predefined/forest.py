# Author: RubADuckDuck

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return RainForest("RainForest")


class PoisonDartFrog(Unit):
    
    HP = 1
    ATT = 50
    ARM = 0
    EVS = 0  
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class GreenAnaconda(Unit):
    
    HP = 5
    ATT = 4
    ARM = 4
    EVS = 0  
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Capybara(Unit):
    
    HP = 15
    ATT = 3
    ARM = 3
    EVS = 0  
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class Jaguar(Unit):
    
    HP = 10
    ATT = 6
    ARM = 2
    EVS = 0  
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)


class MountainGorilla(Unit):
    
    HP = 20
    ATT = 1
    ARM = 2
    EVS = 0  
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
    

class RainForest(Team):
    
    def initialize(self):
        for i in range(0,2):
            unit = PoisonDartFrog(self,"PoisonDartFrog" , i)
            self.units.append(unit)
        
        for i in range(2,4):
            unit = GreenAnaconda(self,"GreenAnaconda" , i)
            self.units.append(unit)
         
        for i in range(4,6):
            unit = Capybara(self,"Capybara" , i)
            self.units.append(unit)
         
        for i in range(6,8):
            unit = Jaguar(self,"Jaguar" , i)
            self.units.append(unit)
       
        for i in range(8,10):
            unit = MountainGorilla(self,"MountainGorilla" , i)
            self.units.append(unit)


class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))            