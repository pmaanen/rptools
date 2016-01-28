import dice
import cards

class swCharacter:
    def __init__(self,name,strength=6,agility=6,smarts=6,vigor=6,spirit=6,toughness=-1,charisma=0,pace=6,bennies=3):
        self.name=name
        self.weapons={}
        self.skills={}
        self.str=strength
        self.agi=agility
        self.sm=smarts
        self.vigor=vigor
        self.spirit=spirit
        
        if toughness==-1:
            self.toughness=2+self.vigor/2
        else:
            self.toughness=toughness
        self.charisma=charisma
        self.pace=pace
        self.wounds=0
        self.bennies=bennies
        self.shaken=False
        self.canAct=True
    def DrawInitiative(self,deck):
        self.inicard=deck.draw()
    def AddWeapon(self,weapon):
        self.weapons.update({weapon.name:weapon})
    def AddSkill(self,skill,die):
        self.skills.update({skill : die})
    def Attack(self,Weapon,Target):
        if not Weapon in self.weapons:
            print "Error: I have no such weapon!"
            return
        dam=self.weapons[Weapon].attack(4,6)
        print self.name+" attacks "+Target.name+" for " +str(dam)+" damage!"
        Target.Damage(dam)
        Target.wounds
        return
    def Shake(self):
        self.shaken=True
        self.canAct=False
    def UnShake(self,benny=False):
        if benny==False:
            roll=dice.die.roll1dX(self.spirit)-self.wounds
            if roll<4:
                return "Failure!"
            if roll>3 and roll<8:
                self.shaken=False
                self.canAct=False
                return "Success!"
            if roll>7:
                self.shaken=False
                self.canAct=True
                return "Raise!"
        else:
            self.shaken=False
            self.canAct=True
    def Damage(self,damage):
        if(damage<self.toughness):
            return
        if(damage>self.toughness and damage<self.toughness+4):
            if(self.shaken==False):
                self.Shake()
                return
            else:
                self.wounds+=1
                if self.wounds>3:
                    print self.name+" is incapacitated!"
                return
        self.wounds+=int((damage-self.toughness)/4)
        self.Shake()
        if self.wounds>3:
            print self.name+" is incapacitated!" 
