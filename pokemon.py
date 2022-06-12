import random
import math

class Pokemon:
    def __init__(self, name, type, lvl, stats):
        self.name = name
        self.type = type
        self.stats = stats
        self.lvl = lvl
        
        self.hpStat = self.stats[0]
        self.attStat = self.stats[1]
        self.defcStat = self.stats[2]
        self.spattStat = self.stats[3]
        self.spdefcStat = self.stats[4]
        self.spdStat = self.stats[5]

        self.natureList = ["lonely (+att -defc)", "Adamant (+att -spatt)", "Naughty (+att -spdefc)", "Brave (+att -spd)", "Hardy (neutral)",
        "Bold (+defc -att)", "Impish (+defc -spatt)", "Lax (+defc -spdefc)", "Relaxed (+defc -spd)", "Docile (neutral)",
        "Modest (+spatt -att)", "Mild (+spatt -defc)", "Rash (+spatt -spdefc)", "Quiet (+spatt -spd)", "Bashful (neutral)",
        "Calm (+spdefc -att)", "Gentle (+spdefc -defc)", "Careful (+spdefc -spatt)", "Sassy (+spdefc -spd)", "Quirky (neutral)",
        "Timid (+spd -att)", "Hasty (+spd -defc)", "Jolly (+spd -spatt)", "Naive (+spd -spdefc)", "Serious (neutral)"]

        self.nature = random.choice(self.natureList)

        self.hpIV = random.randrange(0, 32)
        self.attIV = random.randrange(0, 32)
        self.defcIV = random.randrange(0, 32)
        self.spattIV = random.randrange(0, 32)
        self.spdefcIV = random.randrange(0, 32)
        self.spdIV = random.randrange(0, 32)

        self.attB = 1
        self.defcB = 1
        self.spattB = 1
        self.spdefcB = 1
        self.spdB = 1

        if self.nature == "lonely (+att -defc)":
            self.attB = 1.2
            self.defcB = 0.8

        elif self.nature == "Adamant (+att -spatt)":
            self.attB = 1.2
            self.spattB = 0.8
        
        elif self.nature == "Naughty (+att -spdefc)":
            self.attB = 1.2
            self.spdefcB = 0.8

        elif self.nature == "Brave (+att -spd)":
            self.attB = 1.2
            self.spdB = 0.8

        elif self.nature == "Bold (+defc -att)":
            self.defcB = 1.2
            self.attB = 0.8
        
        elif self.nature == "Impish (+defc -spatt)":
            self.defcB = 1.2
            self.spattB = 0.8
        
        elif self.nature == "Lax (+defc -spdefc)":
            self.defcB = 1.2
            self.spdefcB = 0.8

        elif self.nature == "Relaxed (+defc -spd)":
            self.defcB = 1.2
            self.spdB = 0.8
        
        elif self.nature == "Modest (+spatt -att)":
            self.spattB = 1.2
            self.attB = 0.8

        elif self.nature == "Mild (+spatt -defc)":
            self.spattB = 1.2
            self.defcB = 0.8

        elif self.nature == "Rash (+spatt -spdefc)":
            self.spattB = 1.2
            self.spdefcB = 0.8
        
        elif self.nature == "Quiet (+spatt -spd)":
            self.spattB = 1.2
            self.spdB = 0.8

        elif self.nature == "Calm (+spdefc -att)":
            self.spdefcB = 1.2
            self.attB = 0.8

        elif self.nature == "Gentle (+spdefc -defc)":
            self.spdefcB = 1.2
            self.defcB = 0.8
        
        elif self.nature == "Careful (+spdefc -spatt)":
            self.spdefcB = 1.2
            self.spattB = 0.8

        elif self.nature == "Sassy (+spdefc -spd)":
            self.spdefcB = 1.2
            self.spdB = 0.8
        
        elif self.nature == "Timid (+spd -att)":
            self.spdB = 1.2
            self.attB = 0.8
        
        elif self.nature == "Hasty (+spd -defc)":
            self.spdB = 1.2
            self.defcB = 0.8

        elif self.nature == "Jolly (+spd -spatt)":
            self.spdB = 1.2
            self.spattB = 0.8

        elif self.nature == "Naive (+spd -spdefc)":
            self.spdB = 1.2
            self.spdefcB = 0.8

    def statCalc(self):
        self.hp = math.ceil(((20 * self.hpStat) / 10) + self.lvl + 10 + self.hpIV)
        self.att = math.ceil(((20 * self.attStat) / 25) + self.lvl + self.attIV/3 + 5 * self.attB)
        self.defc = math.ceil(((20 * self.defcStat) / 25) + self.lvl + self.defcIV/3 + 5 * self.defcB)
        self.spatt = math.ceil(((20 * self.spattStat) / 25) + self.lvl + self.spattIV/3 + 5 * self.spattB)
        self.spdefc = math.ceil(((20 * self.spdefcStat) / 25) + self.lvl + self.spdefcIV/3 + 5 * self.spdefcB)
        self.spd = math.ceil(((20 * self.spdStat) / 25) + self.lvl + self.spdIV/3 + 5 * self.spdB)

    def printing(self):
        print(self.hp)
        print(self.att)
        print(self.defc)
        print(self.spatt)
        print(self.spdefc)
        print(self.spd)
