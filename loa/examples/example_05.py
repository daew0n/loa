import time
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer
from loa.judge import MaxSurvivalJudge
from loa.simulator import BasicSimulator
from loa.logging import use_logging, finish_logging

class MyUnit1(Unit):
    
    HP = 72  # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 4 # Armor
    EVS = 8 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class MyUnit2(Unit):
    
    HP = 76 # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 12  # Armor
    EVS = 4  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class MyTeam1(Team):  
    def initialize(self):
        for i in range(10):
            unit = MyUnit1(self, "A-Unit%02d"%(i+1), i)
            self.units.append(unit)   
    
    def arrange(self, enemy: Team):   
        first_unit = self.units[0]
        for i in range(self.num_positions - 1):
            j = i + 1 
            self.units[i] = self.units[j]
            if self.units[i] != None:
               self.units[i].pos = i 
        # end of for
        self.units[-1] = first_unit
        if self.units[-1] != None:
            self.units[-1].pos = self.num_positions - 1
    
    
class MyTeam2(Team):
    def initialize(self):
        for i in range(10):
            unit = MyUnit2(self, "B-Unit%02d"%(i+1), i)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):
        pass
    
if __name__ == "__main__":
   
    use_logging("test",                
                stdout=False,
                fout=True,
                fpath="test.log",
                mode='w')
    
    simulator = BasicSimulator("ROUND-04")
    team1 = MyTeam1("Team#1")
    team2 = MyTeam2("Team#2")
  
    examiner = TeamExaminer()
    
    t_beg = time.perf_counter()    
    examiner.check(team1, "ROUND-04")
    examiner.check(team2, "ROUND-04")
    t_end = time.perf_counter()
    t_elapsed = t_end - t_beg
    print("Duration of checking team: %f (sec.)"%(t_elapsed))

    judge = MaxSurvivalJudge()
    t_beg = time.perf_counter()    
    n_team1, n_team2, n_draws = simulator.play(team1, team2, 40, 5, judge)
    t_end = time.perf_counter()
    t_elapsed = t_end - t_beg
    print("Number of Team1 wins:", n_team1)
    print("Number of Team2 wins:", n_team2)
    print("Number of draws:", n_draws)
    print()
    
    if n_team1 > n_team2:
        print("Team #1 wins!")
    elif n_team1 < n_team2:
        print("Team #2 wins!")        
    else:
        print("Two teams draw...")
    
    print()
    print("Duration of a single game: %f (sec.)"%(t_elapsed))
    finish_logging()
