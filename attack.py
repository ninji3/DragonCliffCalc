class AttackBase():

    def __init__(self):
        self.name = "Base Bash"
        self.element = "Physical"
        self.base_capacity = 1
        self.caster_capacity = 1
        self.target = 1
        self.increase_rate = 0.25
        self.level = 1
        self.special = None

class Swordsmanship(AttackBase):

    def __init__(self, attack_level=1):
        self.name = "Swordsmanship"
        self.element = "Physical"
        self.base_capacity = 1
        self.caster_capacity = 1
        self.target = 1
        self.increase_rate = 0.25
        self.level = attack_level
        self.special = None

    def get_effective_capacity(self):

        increase = self.increase_rate*self.level-self.increase_rate
        effective_capacity = self.base_capacity + increase + self.caster_capacity+ increase
        return effective_capacity