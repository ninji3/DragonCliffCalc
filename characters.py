import attack

class BaseCharacter():

    def __init__(self):
        self.name = "Base Boi"
        self.level = 1
        self.attack = attack.AttackBase()
        self.passive = "Chilling"
        self.skill = "Base Bolt"
        self.main_stat = 100
        self.CRT = 0.05
        self.CRD = 2
        self.dmg_enhance = 0

class StreetMan(BaseCharacter):

    def __init__(self, level=1, attack_level=1, main_stat=10, CRT=0.05, CRD = 2, dmg_enhance=0):
        self.name = "Street Man"
        self.level = level
        self.attack = attack.Swordsmanship(attack_level=attack_level)
        self.passive = None
        self.skill = None
        self.main_stat = main_stat
        self.CRT = CRT
        self.CRD = CRD
        self.dmg_enhance = dmg_enhance

