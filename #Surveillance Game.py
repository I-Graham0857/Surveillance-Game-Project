#Surveillance Game

#Threats:
#3 threats
#Proximity:
#Every tick, get closer by Speed
#If proximity = 0 , player loses
#Starts at 100
#Speed:
#Each character has unique speed
#Maybe increases over time
#Risk:
#Increases as known proximity decrease
#Increases the more time since last scan

#Resource:
#Power:
#Drained by looking
#If look - Drain x power
#Drained by repelling
#If repel - Drain x power

#Player:
#Can look at everything
#Player learns proximity, costs less power
#Can repel one
#Repel sets proximity to 100, costs more power
#Can idle

#Evaluates utility of each action
#Utility:
#Added Safety - cost
#Cost = power + opportunity cost
#Safety = -Risk

#Must survive for 50 ticks

#Per tick:
#Update game state for all threats
#Calculate utility for all choices
#Choose highest utility choice
#Remove power and update status accordingly
#Check if game end
#Advance tick

#Threat class
class Threat:
    proximity = 100
    knownProximity = 100
    scanTime = 0
    risk = 0
    def __init__(self, speed, name):
        self.name = name
        self.speed = speed
    
    def GetScan(self):
        self.scanTime = 0
        self.knownProximity = self.proximity

    def Update(self):
        self.proximity = self.proximity - self.speed
        self.scanTime = self.scanTime + 1
        self.risk = .25 * (100 - self.knownProximity) + 2 * (self.scanTime)
        print(self.name + "'s proximity = " + str(self.proximity))
        print(self.name + "'s risk = " + str(self.risk))


#Player class
class Player:
    power = 100
    def Scan(self, threat):
        threat.GetScan()
        self.power = self.power - 3

    def Repel(self, threat):
        threat.proximity = 100
        threat.knownProximity = 100
        threat.scanTime = 0
        self.power = self.power - 10


def Utility(t1, t2, t3, player):
    #Find utility of each action
    scan1Util = .25 * (t1.risk) + t1.scanTime - (6 + .5 * (t2.risk + t3.risk))
    scan2Util = .25 * (t1.risk) + t2.scanTime - (6 + .5 * (t3.risk + t1.risk))
    scan3Util = .25 * (t1.risk) + t3.scanTime - (6 + .5 * (t2.risk + t1.risk))

    repel1Util = t1.risk - (20 + .5 * (t2.risk + t3.risk))
    repel2Util = t2.risk - (20 + .5 * (t3.risk + t1.risk))
    repel3Util = t3.risk - (20 + .5 * (t2.risk + t1.risk))

    idleUtil = -1 * (.33 * (t1.risk) + .33 * (t2.risk) + .33 * (t3.risk))

    #Find highest utility action
    if (scan1Util >= scan2Util and scan1Util >= scan3Util and scan1Util >= idleUtil and scan1Util >= repel1Util and scan1Util >= repel2Util and scan1Util >= repel3Util):
        print("Scan 1: Utility = " + str(scan1Util))
        player.Scan(t1)
    elif (scan2Util >= scan1Util and scan2Util >= scan3Util and scan2Util >= idleUtil and scan2Util >= repel1Util and scan2Util >= repel2Util and scan2Util >= repel3Util):
        print("Scan 2: Utility = " + str(scan2Util))
        player.Scan(t2)
    elif (scan3Util >= scan1Util and scan3Util >= scan2Util and scan3Util >= idleUtil and scan3Util >= repel1Util and scan3Util >= repel2Util and scan3Util >= repel3Util):
        print("Scan 3: Utility = " + str(scan3Util))
        player.Scan(t3)

    elif (repel1Util >= repel2Util and repel1Util >= repel3Util and repel1Util >= scan1Util and repel1Util >= scan2Util and repel1Util >= scan3Util and repel1Util >= idleUtil):
        print("Repel 1: Utility = " + str(repel1Util))
        player.Repel(t1)
    elif (repel2Util >= repel1Util and repel2Util >= repel3Util and repel2Util >= scan1Util and repel2Util >= scan2Util and repel2Util >= scan3Util and repel2Util >= idleUtil):
        print("Repel 2: Utility = " + str(repel2Util))
        player.Repel(t2)
    elif (repel3Util >= repel1Util and repel3Util >= repel2Util and repel3Util >= scan1Util and repel3Util >= scan2Util and repel3Util >= scan3Util and repel3Util >= idleUtil):
        print("Repel 3: Utility = " + str(repel3Util))
        player.Repel(t3)
    elif (idleUtil >= scan1Util and idleUtil >= scan2Util and idleUtil >= scan3Util and idleUtil >= repel1Util and idleUtil >= repel2Util and idleUtil >= repel3Util):
        print("Idle: Utility = " + str(idleUtil))
    else:
        print("Error")


Joel = Threat(3, "Joel")
Jeff = Threat(5, "Jeff")
John = Threat(8, "John")

Ai = Player()


#Ticks
for x in range(50):
    print("Tick " + str(x + 1))
    #Update game state for all threats
    Joel.Update()
    Jeff.Update()
    John.Update()
    #Calculate utility for all choices
    #Choose highest utility choice
    #Remove power and update status accordingly
    Utility(Joel, Jeff, John, Ai)

    #Check if game end
    if (Joel.proximity <= 0 or Jeff.proximity <= 0 or John.proximity <= 0):
        print("You died")
        break

    if (Ai.power < 0):
        print("You ran out of power")
        break