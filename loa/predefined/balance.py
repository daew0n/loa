# Author: L-HK

import unittest
from loa.unit import Unit
from loa.team import Team, TeamExaminer


def get_team():
    return Balance("Balance")


class Assassin(Unit):
    HP = 17
    ATT = 18
    ARM = 10
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

class Warrior1(Unit):
    HP = 27
    ATT = 13
    ARM = 7
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

class Warrior2(Unit):
    HP = 24
    ATT = 12
    ARM = 11
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

class Fighter1(Unit):
    HP = 15
    ATT = 14
    ARM = 14
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

class Fighter2(Unit):
    HP = 15
    ATT = 14
    ARM = 14
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

class Fighter3(Unit):
    HP = 18
    ATT = 14
    ARM = 12
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

class Tanker1(Unit):
    HP = 11
    ATT = 12
    ARM = 17
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

class Tanker2(Unit):
    HP = 12
    ATT = 11
    ARM = 17
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

class Barrior1(Unit):
    HP = 44
    ATT = 2
    ARM = 1
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

class Barrior2(Unit):
    HP = 45
    ATT = 1
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

class Balance(Team):
    def initialize(self):
        unit1 = Assassin(self, "Assassine", 0)
        unit2 = Warrior1(self, "Warrior1", 1)
        unit3 = Warrior2(self, "Warrior2", 2)
        unit4 = Fighter1(self, "Fighter1", 3)
        unit5 = Fighter2(self, "Fighter2", 4)
        unit6 = Fighter3(self, "Fighter3", 5)
        unit7 = Tanker1(self, "Tanker1", 6)
        unit8 = Tanker2(self, "Tanker2", 7)
        unit9 = Barrior1(self, "Barrior1", 8)
        unit10 = Barrior2(self, "Barrior2", 9)
        self.units.append(unit1)
        self.units.append(unit2)
        self.units.append(unit3)
        self.units.append(unit4)
        self.units.append(unit5)
        self.units.append(unit6)
        self.units.append(unit7)
        self.units.append(unit8)
        self.units.append(unit9)
        self.units.append(unit10)


class TestTeam(unittest.TestCase):

    def test_team(self):
        team = get_team()
        examiner = TeamExaminer()
        self.assertTrue(examiner.check(team, "ROUND-03"))