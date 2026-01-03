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
    def __init__(self, speed):
        self.speed = speed
    
    def GetScan(self):
        self.scanTime = 0
        self.knownProximity = self.proximity

    def Update(self):
        self.proximity = self.proximity - self.speed
        self.scanTime = self.scanTime + 1
        self.risk = 2(100 - self.knownProximity) + (self.scanTime)


#Player class
class Player:
    def __init__(self, power):
        self.power = power
    
    def Scan(self, threat):
        threat.GetScan()
        self.power = self.power - 4

    def Repel(self, threat):
        threat.proximity = 100
        self.power = self.power - 10



Joel = Threat(1)
Jeff = Threat(2)
John = Threat(3)


#Ticks
for x in range(50):
    pass