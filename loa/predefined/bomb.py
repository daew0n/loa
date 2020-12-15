# Author: gh-BumsooKim

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return Bomb("Bomb")


class MiniBomb(Unit):
    HP = 1
    ATT = 10
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


class BigBomb(Unit):
    HP = 9
    ATT = 2
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


class AttackBomb(Unit):
    HP = 2
    ATT = 30
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


class ArmorBomb(Unit):
    HP = 16
    ATT = 0
    ARM = 15
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


class Bomb(Team):
    def initialize(self):
        pos = 0
        for i in range(4):
            unit = MiniBomb(self, "MiniBombUnit-%02d"%(i+1), pos)
            self.units.append(unit)
            pos += 1
            
        for i in range(4):
            unit = BigBomb(self, "BigBombUnit-%02d"%(i+1), pos)
            self.units.append(unit)
            pos += 1
            
        unit = AttackBomb(self, "AttackBombUnit", pos)
        self.units.append(unit)
        pos += 1
            
        unit = ArmorBomb(self, "ArmorBombUnit", pos)
        self.units.append(unit)


class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))