import numpy.random as npr
from ROOT import TText
import itertools
import codecs
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

    @staticmethod
    def showNdX(N,X,exploding=False):
        myText=TText(0.4,0.4,str(die.rollNdX(N,X,exploding=False)))
        myText.SetTextSize(1.1)
        return myText
        
        
    
class weapon:
    def __init__(self,name,str,ndice,dietype,damagebonus=0,fightingbonus=0):
        self.str=str
        self.ndice=ndice
        self.dietype=dietype
        self.fightingbonus=fightingbonus
        self.damagebonus=damagebonus
        self.name=name
        

class swWeapon():
    def __init__(self,name,damage=[],fixed=0,atkb=0,wildcard=True):
        self.name=name
        self.damage=damage
        self.fixed=fixed
        self.atkb=atkb
        self.current=False
        self.wildcard=wildcard
    def attack(self,TN=4,Skill=4,Toughness=4):
        self.current=False
        damage=0
        if self.wildcard:
            atk=max(die.roll1dX(Skill,True)+self.atkb,die.roll1dX(6,True)+self.atkb)
        else:
             atk=die.roll1dX(Skill,True)+self.atkb
        if atk<TN:
            return -1
        if atk>=TN:
            damage=self.do_damage()
        if atk>TN+3:
            self.current=True
            damage=self.do_damage(True)
        if (damage-Toughness)<0:
            return -1
        else:
            #print int((damage-Toughness)/4)
            return int((damage-Toughness)/4)
        
    def rapid_attack(self,TN=4,Skill=4,Toughness=4):
        dam=[]
        for i in range(3):
            dam.append(self.attack(TN+4,Skill,Toughness))
        if reduce(lambda x,y:max(x,y),dam)==-1:
            return -1
        else:
            return reduce(lambda x,y:x+y,map(lambda x:max(0,x),dam))
    def double_tap(self,TN=4,Skill=4,Toughness=4):
        return self.attack(TN-1,Skill,Toughness-1)
    
    def auto(self,TN=4,Skill=4,Toughness=4,ROF=3):
        dam=[]
        for i in range(ROF):
            dam.append(self.attack(TN+2,Skill,Toughness))
        if reduce(lambda x,y:max(x,y),dam)==-1:
            return -1
        else:
            return reduce(lambda x,y:x+y,map(lambda x:max(0,x),dam))
    def burst(self,TN=4,Skill=4,Toughness=4):
        return self.attack(TN-2,Skill,Toughness-2)
    def do_damage(self,Raise=False):
        dam=0
        for ddie in self.damage:
            dam+=die.roll1dX(ddie,True)
        if Raise == True:
            dam+=die.roll1dX(6,True)
        dam+=self.fixed
        return dam
    def reroll_damage(self):
        return self.do_damage(self.current)
        

def cumulative_damage(histo):
    return
def multiple_attacks(dam):
    if reduce(lambda x,y:max(x,y),dam)==-1:
        return -1
    else:
        return reduce(lambda x,y:x+y,map(lambda x:max(0,x),dam))
    
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

class card:
    # Define the suits
    DIAMONDS = 1
    CLUBS = 4
    HEARTS = 2
    SPADES = 3
    SUITS = {
        CLUBS: 'Clubs',
        HEARTS: 'Hearts',
        DIAMONDS: 'Diamonds',
        SPADES: 'Spades'
    }
 
    # Define the names of special cards
    VALUES = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace',
        15: 'Joker'
    }
 
    def __init__(self, suit, value):
        # Save the suit and card value
        self.suit = suit
        self.value = value
 
    def __lt__(self, other):
        # Compare the card with another card
        # (return true if we are smaller, false if
        # we are larger, 0 if we are the same)
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        return 0

    def __gt__(self,other):
        if(self.__lt__(other)==0):
            return 0
        else:
            return (not self.__lt(other))

    def __eq__(self,other):
        return self.__gt__(other)==0
    
    def __str__(self):
        # Return a string description of ourself
        if(self.value==15):
            if self.suit==1:
                return "Red Joker"
            else:
                return "Black Joker"
        if self.value in self.VALUES:
            buf = self.VALUES[self.value]
        else:
            buf = str(self.value)
        buf = buf + ' of ' + self.SUITS[self.suit]
        return buf
    
class deck:
    def __init__(self):
        self.cards=[]
    def draw(self,shuffle=False):
        if(len(self.cards)==0):
            print "No cards left on deck"
            return
        num=npr.randint(0,self.n)
        card=self.cards.pop(num)
        self.n-=1
        if shuffle:
            self.shuffle()
        return card
    def drawN(self,N=1):
        cards=[]
        for i in range(N):
            cards.append(self.draw())
        return cards
    def shuffle(self):
        self.__init__()

class deck32(deck):
    def __init__(self):
        deck.__init__(self)
        suits=range(1,4)
        ranks=range(7,15)
        for prod in itertools.product(suits,ranks):
             self.cards.append(card(prod[0],prod[1]))
        self.n=len(self.cards)

class deck52(deck):
    def __init__(self):
        deck.__init__(self)
        suits=range(1,5)
        ranks=range(2,15)
        for prod in itertools.product(ranks,suits):
            self.cards.append(card(prod[1],prod[0]))
        self.cards.append(card(1,15))
        self.cards.append(card(3,15))
        self.n=len(self.cards)
