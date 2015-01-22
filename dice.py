import numpy.random as npr

class die:
    def __init__(self):
        print "only static methods"

    @staticmethod
    def roll(d,exploding=False):
        return roll1(d,exploding)
    
    @staticmethod    
    def roll1dX(d,exploding=False):
        result=0
        if not exploding:
            result=npr.randint(1,d+1)
        else:
            result=0
            while True:
                temp=npr.randint(1,d+1)
                result+=temp
                if temp<d:
                    break
        return result

    @staticmethod    
    def rollNdX(N,X,exploding=False):
        result=0
        for ii in range(N):
            result+=die.roll1dX(X,exploding)
        return result

    
class weapon:
    def __init__(self,name,str,ndice,dietype,damagebonus=0,fightingbonus=0):
        self.str=str
        self.ndice=ndice
        self.dietype=dietype
        self.fightingbonus=fightingbonus
        self.damagebonus=damagebonus
        self.name=name

class swWeapon():
    def __init__(self,name,damage=[],fixed=[],atkb=0):
        self.name=name
        self.damage=damage
        self.fixed=fixed
        self.atkb=atkb
    def attack(self,TN=4,Skill=4):
        atk=die.roll1dX(Skill,True)+self.atkb
        if atk>TN:
            return self.do_damage()
        if atk>TN+3:
            return self.do_damage(True)
        return 0
    def do_damage(self,Raise=False):
        dam=0
        for ddie in self.damage:
            dam+=die.roll1dX(ddie,True)
            if Raise == True:
                dam+=die.roll1dX(6,True)
            dam+=self.fixed
        return dam
  
class pfWeapon():
    def __init__(self,name,attacks=[],dice=[],fixeddamage=0,critrange=1,critmult=2,prec_dice=[]):
        self.name=name
        self.attacks=attacks
        self.dice=dice
        self.fixeddamage=fixeddamage
        self.critrange=critrange
        self.critmult=critmult
        self.prec_dice=prec_dice
    def attack(self,AC=10,AT=-999):
        if(AT==-999):
            atb=self.attacks[0]
        else:
            atb=AT
        at=die.roll1dX(20)
        atk=atb+at
        #print "Attack Roll against AC"+str(AC)+"... "+str(at)+"+"+str(atb)+"="+str(atk)
        if(at==1):
            return 0
        if at>=21-self.critrange and (atk>=AC or at==20):
            conf=die.roll1dX(20)+atb
            #print "confirmation roll "+str(conf)
            if conf>=AC or conf==20:
                return self.damage(True)
            else:
                return self.damage()
        else:
            if(atk>=AC):
                return self.damage()
            else:
                return 0
    def fullAttack(self,AC=10):
        dam=0
        for at in self.attacks:
            dam+=self.attack(AC,at)
        return dam
    def damage(self,crit=False):
        dam=0
        if crit == False:
            dam+=self.fixeddamage
            for iDie in self.dice:
                dam+=die.roll1dX(iDie)
        else:
            for ii in range(self.critmult):
                dam+=self.fixeddamage
                for iDie in self.dice:
                    dam+=die.roll1dX(iDie)
        for iDie in self.prec_dice:
            dam+=die.roll1dX(iDie)
        #print "Rolling Damage..."+str(dam)+"!"
        return dam
    
class fighter:
    def __init__(self,name="DefaultFighter"):
        self.name=name
        self.weapons=[]
    def add(self,weapon):
        self.weapons.append(weapon)
    def fullAttack(self,ac):
        dam=0
        for weapon in self.weapons:
            dam+=weapon.fullAttack(ac)
        return dam
    def fullAttack(self,ac,wname="nonsense"):
        for weapon in self.weapons:
            if weapon.name==wname:
                return weapon.fullAttack(ac)
        if(wname=="nonsense"):
            dam=0
            for weapon in self.weapons:
                dam+=weapon.fullAttack(ac)
            return dam
        print "weapon could not be found!"
        return 1
