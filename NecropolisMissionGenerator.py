#!/usr/bin/python
import sys
import getopt
import dice
def RollGuns():
    sup=dice.die.roll1dX(8,False)
    if sup==1 or sup==2:
        return "Support fire from a Judea medium tank is available.\n"
    elif sup==3 or sup==4:
        return "A Constantine SPA is available.\n"
    elif sup==5 or sup==6:
        return "Basilica SPA fire is available.\n"
    elif sup==7:
        return "A Goliath 200mm MLRS is available.\n"
    elif sup==8:
        return "A Goliath 300mm MLRS is available.\n"
    
def RollAir():
    sup=dice.die.roll1dX(10,False)
    if sup==1 or sup==2:
        return "Support fire from an Archangel assault craft is available.\n"
    elif sup==3 or sup==4 or sup==5:
        return "An Angel dropship is on standby.\n"
    elif sup==6 or sup==7:
        return "A Deliverance bomber is available for fire support missions.\n"
    elif sup==8:
        return "A Scourge bomber is available.\n"
    elif sup==9 or sup==10:
        return "A Crown fighter is available.\n"

    

def RollSupport(mod=0):
    sup=dice.die.roll1dX(8)+mod
    if sup<=4:
        return ""
    elif sup<=6:
        return RollGuns()
    elif sup>=7:
        return RollAir()
    
def RollAllies(mod=0):
    ally=dice.die.roll1dX(10,False)+mod
    avs="is available.\n"
    avp="are available.\n"
    if ally<=2:
        return ""
    elif ally==3:
        return "A dog team (sergeant+dog) "+avs
    elif ally<=6:
        return "A lance of sergeants "+avs
    elif ally==7:
       r=dice.die.roll1dX(2,False)
       if r==1:
           return "A lance of sergeants "+avs
       else:
           return "Two lances of sergeants "+avp
    elif ally==8:
         r=dice.die.roll1dX(4,False)
         if r==1:
             return "A lance of sergeants "+avs
         else:
             return str(r)+" lances of sergeants "+avp
    elif ally==9:
        return "A fire support knight "+avs
    elif ally==10:
        return "A close artillery team "+avs
    elif ally==11:
        return "A prophet apc "+avs
    elif ally==12:
        return "A light tank "+avs
    elif ally==13:
        return "A medium tank "+avs
    elif ally>=14:
        return "A heavy tank "+avs

def RollRephaim(mod=0):
    reph=dice.die.roll1dX(10,False)+mod
    if reph<=1:
        return "A corrupt priest and "+str(dice.die.rollNdX(2,4,False))+" disciples are in the area."
    elif reph==2:
        num=dice.die.roll1dX(3,False)
        res=""
        if num==1:
            res+="One changeling is"
        else:
            res+=str(num)+" changelings are"
        res+=" in the area."
        return res
    elif reph==3 or reph==4:
        return "A patrol of "+str(dice.die.rollNdX(2,6,False))+" skeletons or zombies is combing the area."
    elif reph==5:
        return "A number of exploding corpses equal to the number of heroes are patrolling the area."
    elif reph==6 or reph==7:
        res="A number of zombies or skeletons twice the number of allied characters and led by a young vampire patrols the area."
        if dice.die.roll1dX(2,False)==1:
            res+=" They have a necromantic Weapon."
        return res
    elif reph==8:
        res="A unit of "+str(dice.die.roll1dX(4,False)+1)+" zombies led by a young vampire and carrying a necromantic special weapon are in the area."
        if dice.die.roll1dX(2,False)==1:
            res+=" A patrol of "+str(dice.die.rollNdX(2,6,False))+" skeletons or zombies is supporting them."
        return res
    elif reph==9:
        return "The group comes up against one of the horrors from the bestiary." 
    elif reph==10:
        res="A nazareth light tank is operating in the area."
        if dice.die.roll1dX(2,False)==1:
            res+=" A patrol of "+str(dice.die.rollNdX(2,6,False))+" skeletons or zombies is supporting them."
        return res
    elif reph>=11:
        res="A mummy or ancient vampire is in the area along with his bodyguards. "
        res+=str(RollRephaim(0))+"\n"
        res+=str(RollRephaim(0))
        return res

def RollCorporate(mod=0):
    corp=dice.die.roll1dX(6,False)+mod
    if corp<=1:
        return "A patrol of "+str(dice.die.rollNdX(2,6,False))+" soldiers roams the area."
    elif corp==2:
        return "A lone scout lurks the area."
    elif corp==3 or corp==4:
        return "A force of "+str(dice.die.rollNdX(3,6,False))+" soldiers led by an officer and supported by a roadrunner apc is operating in the area."
    elif corp==5:
        return "A force of "+str(dice.die.roll1dX(3,False))+" scientists and "+ str(dice.die.rollNdX(2,6,False))+" veteran soldiers is in the area."
    elif corp>=6:
        return "A squad of "+str(dice.die.rollNdX(2,6,False))+" veteran soldiers led by "+str(dice.die.roll1dX(3,False))+" officers and supported by a brigand medium tank maneuver in the area."
    
def RollComplication(mod=0):
    res=""
    comp=dice.die.roll1dX(20,False)+mod
    if comp<=1:
        return ""
    elif comp==2 or comp==3:
        res+="The locals are upset at the church. They treat the knights with contempt, refuse them hospitality and make anti-church comments."
    elif comp==4 or comp==5:
        res+="An unexpected solar flare hits Salus. Comms are down for "+str(dice.die.roll1dX(4,False))+ " hours."
    elif comp==6:
        res+="The group stumbles upon a small fortification. The fortification is camouflaged and requires a notice roll at -1 to spot before the guard opens fire from "+str(dice.die.rollNdX(2,12,False)+12)+"\" away. The group comprises of "+str(dice.die.roll1dX(6,False))+" skeletons or zombies supported by a necromantic special weapon."
    elif comp==7 or comp==8:
        res+="A media news group is assigned to follow the unit. The group consists of "+str(dice.die.roll1dX(6,False))+" members. If the mission is succesful, award +1 xp. If are journalist is killed or the characters are caught committing un-knightly acts, subtract 2 xp."
    elif comp==9:
        res+="At some point during the mission the group receives a call from the preceptory. The current mission is scrapped and a new one is given. Do not reroll allies and support."
    elif comp>=10 and comp<=13:
        return ""
    elif comp==14:
        res+="The group wanders into an area containing corpse mines. The minefield covers an area of "+str(dice.die.rollNdX(2,10,False)+20)+"\" and is of medium density"
    elif comp==15 or comp==16:
        res+=str(RollCorporate(1))+"\n"
        res+="They are on an illegal mission and attack on sight."
    elif comp==17 or comp==18:
        res+="An important piece of equipment has a malfunction. Fixing it in the field requires a repair roll at -2 and "+str(dice.die.rollNdX(2,10,False))+" minutes."
    elif comp==19:
        res+="The group discovers an assembly area for Rephaim preparing for an attack on a nearby settlement. The force consists of "+str(dice.die.roll1dX(10,False)*10)+" zombies and/or skeletons with one young vampire per 20 soldiers. In addiction, the force has "+str(dice.die.roll1dX(2,False)+1)+" captured Nazareth tanks. The group should encounter several patrols before finding the staging area."
    elif comp>=20:
        res+="Some incorrect intelligence is given to the unit. Maybe the opposition is stronger than expected or the target is in another area."
    return res+"\n"

def RollAssault(mod=0):
    Reph=""
    for ii in range(1,dice.die.roll1dX(4,False)+1):
        Reph+=str(RollRephaim(2))+"\n"
    target=dice.die.roll1dX(3,False)
    if target==1:
        tar="building"
    elif target==2:
        tar="fortification"
    elif target==3:
        tar="fixed position"
    return "The mission is an assault on a "+tar+".\n"+RollAllies(5)+RollSupport(2)+Reph+RollComplication(2)+"\n"

def RollParticipate():
    Reph=""
    for ii in range(1,dice.die.roll1dX(4,False)+1):
        Reph+=str(RollRephaim(2))+"\n"
    target=dice.die.roll1dX(6,False)
    tar="The group participates in"
    if target==1:
        tar+=" an air assault."
    elif target==2:
        tar+=" an amphibious landing."
    elif target==3:
        tar+=" a bridgehead operation."
    elif target==4:
        tar+=" a counterattack."
    elif target==5:
        tar+=" an evacuation."
    elif target==6:
        tar+=" street fighting."
    return tar+"\n"+RollAllies(4)+RollSupport(2)+Reph+RollComplication()+"\n"

def RollProtect():
    Reph=""
    for ii in range(1,dice.die.roll1dX(4,False)+1):
        Reph+=str(RollRephaim(2))+"\n"
    target=dice.die.roll1dX(8,False)
    tar="The group has to protect "
    if target==1:
        tar+="a bridge, road, railway, port, or other strategic site. "
    elif target==2:
        tar+="a city, town or village. "
    elif target==3:
        tar+="a church official. "
    elif target==4:
        tar+="a dignitary from another ordo. "
    elif target==5:
        tar+="a factory/production site. "
    elif target==6:
        tar+="position lacking supplies. "
    elif target==7:
        tar+="the main body of the fighting force in a retreat. "
    elif target==8:
        tar+="a secret base. "
    tar+="Retreat is only permitted on explicit order."
    return tar+"\n"+RollAllies(3)+RollSupport(2)+Reph+RollComplication()+"\n"
        
def RollCapture():
    Reph=""
    Corp=""
    tar=""
    target=dice.die.roll1dX(8,False)
    if target==1:
        tar+="The group has to capture a"
        if dice.die.roll1dX(2,False)==1:
            tar+=" corporate"
            for ii in range(1,dice.die.roll1dX(4,True)+1):
                Corp+=str(RollCorporate(1))+"\n"
        else:
            tar+=" rephaim"
            for ii in range(1,dice.die.roll1dX(4,True)+1):
                Reph+=str(RollRephaim())+"\n"
        tar+=" agent and bring him in for questioning."
    elif target==2:
        for ii in range(1,dice.die.roll1dX(4,True)+1):
            Reph+=str(RollRephaim())+"\n"
        tar+="Intelligence has revealed the location of rephaim headquarters. The lance is ordered to infiltrate the base and retrieve battle plans."
    elif target==3:
        tar+="Rephaim have still not mastered watercraft. The group must retake a bridge without destroying it"
        for ii in range(1,dice.die.roll1dX(4,False)+1):
            Reph+=str(RollRephaim())+"\n"
    elif target==4:
        tar+="A city, town or village has to be retaken from the rephaim."
        for ii in range(1,dice.die.roll1dX(4,False)+1):
            Reph+=str(RollRephaim())+"\n"
    elif target==5:
        tar+="The church suspects a corporate scientist to be in collusion with the rephaim. Unwilling to wage open war on two fronts, the Vatican has ordered a covert raid to bring the suspect in for interrogation."
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                Corp+=str(RollCorporate(1))+"\n"
        for ii in range(1,dice.die.roll1dX(4,False)-2):
                Reph+=str(RollRephaim())+"\n"        
    elif target==6:
        tar+="The testing of a brand new weapon by "
        if dice.die.roll1dX(2,False)==1:
            tar+=" corporate"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                Corp+=str(RollCorporate(1))+"\n"
        else:
            tar+=" rephaim"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                Reph+=str(RollRephaim())+"\n"
        tar+=" forces has not gone unnoticed."
    elif target==7:
        tar+="Greater Rephaim only rarely venture out of their mausoleums and the chance to grab one for interrogation or research is just to good to pass."
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                Reph+=str(RollRephaim())+"\n"
    elif target==8:
        tar+="In a bid to better understand the foe and its weapons. The group must secure one or more items of necromantic science"
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                Reph+=str(RollRephaim())+"\n"
    return tar+"\n"+RollSupport()+RollAllies(2)+Reph+Corp+RollComplication()+"\n"

def RollDestroy():
    tar=""
    OpFor=""
    target=dice.die.roll1dX(6,False)
    if target==1 or target==2:
        tar+="A greater repha has been located far behind enemy lines and the Field Master has ordered it assassinated."
    elif target==3:
        tar+="A "
        if dice.die.roll1dX(2,False)==1:
            tar+= "rephaim "
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim())+"\n"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim())+"\n"
        else:
            tar+="corporate"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollCorporate(1))+"\n"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollCorporate(1))+"\n"
        tar+="research facility needs to be destroyed. It is located far behind enemy lines."
    elif target==4:
        tar+="A secret weapon is being tested by the "
        if dice.die.roll1dX(2,False)==1:
            tar+= "Rephaim "
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim())+"\n"
        else:
            tar+="Union"
            for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollCorporate(1))+"\n"
        tar+=". It needs to be destroyed. The testing takes place far behind enemy lines."
    elif target==5:
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim())+"\n"
        tar+="A supply depot needs to be destroyed to deny the enemy vital ressources."
    elif target==6:
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim())+"\n"
        tar+="One or more vehicles, wether in a lager or on the move, need to be destroyed."
    return tar+"\n"+RollSupport()+RollAllies()+OpFor+RollComplication()+"\n"

def RollInvestigate():
    target=""
    tar=dice.die.roll1dX(6,False)
    if tar==1:
        target+="The group is sent out to investigate the appearance of a new form of repha"
    elif tar==2:
        target+="The group is sent to investigate cultist activity. Rooting them out requires a mix of social skill and investigation. "
    elif tar==3:
        loc=dice.die.roll1dX(3,False)
        if loc==1:
            target+="Villagers "
        elif loc==2:
            target+="Units "
        elif loc==3:
            target+="Persons "
        target+="have vanished. They may suffer from communication failure, or something more sinister may have happened."
    elif tar==4:
        target+="A friendly unit has stopped reporting in and the group has to search the location of their last transmission for clues."
    elif tar==5:
        target+="A mysterious sound, smell or glow has to be investigated."
    elif tar==6:
        target+="A new form of necromantic weird science has appeared. The characters have to track it to its origin."
    OpFor=""
    for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim(-2))+"\n"
    return target+"\n"+RollSupport(-2)+RollAllies()+OpFor+RollComplication()+"\n"

def RollRescue():
    tar=""
    OpFor=""
    if dice.die.roll1dX(2,False)==1:
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollRephaim(-2))+"\n"
    else:
        for ii in range(1,dice.die.roll1dX(4,False)+1):
                OpFor+=str(RollCorporate())+"\n"
    target=dice.die.roll1dX(4,False)
    if target==1:
        tar+="A downed pilot needs to be rescued."
    elif target==2:
        tar+="A church official has gone missing and needs to be rescued."
    elif target==3:
        tar+="Equipment needs to be retrieved."
    elif target==4:
        tar+="A unit has gone missing and needs to be rescued."
    return tar+"\n"+RollSupport()+RollAllies()+OpFor+RollComplication()+"\n"

def RollScout():
    tar=""
    OpFor=""
    tar+="A "
    target=dice.die.roll1dX(4,False)        
    if dice.die.roll1dX(2,False)==1:
        tar+="Rephaim "
        for ii in range(1,dice.die.roll1dX(4,False)+1):
            OpFor+=str(RollRephaim(-2))+"\n"
    else:
        tar+="Corporate "
        for ii in range(1,dice.die.roll1dX(4,False)+1):
            OpFor+=str(RollCorporate())+"\n"     
    if target==1:
        tar+="action "
    elif target==2:
        tar+="facility "
    elif target==3 or target==4:
        tar+="position "
    tar+="needs to be scouted. The heroes have to look around and report back. Contact with the enemy has to be avoided."
    return tar+"\n"+RollSupport(-2)+RollAllies(-2)+OpFor+RollComplication()+"\n"

def RollHeartsAndMinds():
    target=dice.die.roll1dX(4,False)
    OpFor=""
    for ii in range(1,dice.die.roll1dX(4,False)+1):
        OpFor+=str(RollRephaim(-4))+"\n"
    tar="The group is ordered to show church presence and conduct recruitment operations in a nearby "
    if target==1 or target==2:
        tar+="small village."
    elif target==3:
        tar+="town."
    elif target==4:
        tar+="city"
    return tar+"\n"+RollAllies(-4)+OpFor+RollComplication(-2)+"\n"

def GenerateMission(mod=0):
    type=dice.die.roll1dX(10,False)+mod
    if type<=1:
        return RollAssault()
    elif type==2:
        return RollParticipate()
    elif type==3:
        return RollProtect()
    elif type==4:
        return RollCapture()
    elif type==5:
        return RollDestroy()
    elif type==6:
        return RollInvestigate()
    elif type==7:
        return RollRescue()
    elif type==8:
        return RollScout()
    elif type>=9:
        return RollHeartsAndMinds()

def main():

    import argparse
    parser = argparse.ArgumentParser(description='Generate some missions for a Necropolis 2350 group.')
    parser.add_argument("-o","--ordo",type=str,default="burners",help="Choose your ordo. Recognized are: templars, burners, impalers, preachers, lazarites. Default is burners")
    parser.add_argument("-r","--rank",type=str,default="seasoned",help="Choose your rank. Recognized are: novice, seasoned, veteran, heroic, legendary. Default is seasoned.")
    parser.add_argument("-n",type=int,default=1,help="Number of missions to be generated. Default is 1")
    parser.add_argument("-f","--file",type=str,default="stdout",help="Choose output file. If not specified, output is written to stdout.")
    args = parser.parse_args()
    if args.ordo=="templars":
        ordo=-2
    elif args.ordo=="impalers":
        ordo=-1
    elif args.ordo=="preachers":
        ordo=1
    elif args.ordo=="burners" or args.rank=="lazarites":
        ordo=0
    else:
        print "Ordo not recognized."
        parser.print_help()
        exit(2)
    if args.rank=="novice":
        rank=1
    elif args.rank=="seasoned":
        rank=0
    elif args.rank=="veteran" or args.rank=="heroic" or args.rank=="legendary":
        rank=-1
    else:
        print "Rank not recognized."
        parser.print_help()
        exit(2)
    if args.file=="stdout":
        for ii in range(args.n):
            if args.n>1:
                print "-"*10
            print GenerateMission(ordo+rank)
    else:
        try:
            file=open(args.file,'w')
            for ii in range(args.n):
                if args.n>1:
                    print "-"*10
                    file.write("-"*10+"\n")
                file.write(GenerateMission(ordo+rank))
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    exit(0)

if __name__ == "__main__":
    main()
