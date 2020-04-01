import random
from math import sqrt

#space of the community
width = 1000
height = 1000

#population in the community
participants = 20000

collectionOfParticipants = []


health = participants - 1
sick = 1
recovered = 0
death = 0

spread_radius = 50
infect_probability = 0.7
recover_probability = 0.09
dealth_probability = 0.01

# Healthy = 0
# Sick = 1
# Recovered = 3
# Death = 4

class coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,x,y):
        xDist = self.x - x
        yDist = self.y - y
        Distance = sqrt(xDist**2 + yDist**2)
        return Distance


class participant:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.uniform(0,width)
        self.y = random.uniform(0,height)
        self.status = 0
        self.xspeed = random.uniform(-10,10)
        self.yspeed = random.uniform(-10,10)
        # self.sickDay = 0
        # self.recover_probability = 0.4
        # self.

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x>self.width:
            self.x = self.width
            self.xspeed = random.uniform(-10,10)
        if self.x<0:
            self.x = 0
            self.xspeed = random.uniform(-10,10)
        if self.y>self.height:
            self.y=self.height
            self.yspeed = random.uniform(-10,10)
        if self.y<0:
            self.y=0
            self.yspeed = random.uniform(-10,10)
            
for x in range(participants-1):
    collectionOfParticipants.append(participant(width, height))

sickPerson = participant(width, height)
sickPerson.status = 1
collectionOfParticipants.append(sickPerson)

sickBoolean = True

while sickBoolean:
    collectionOfSick = []
    sickCount = 0

    count = {}
    count[0] = 0
    count[1] = 0
    count[3] = 0
    count[4] = 0

    for x in collectionOfParticipants:
        x.move()
        if x.status == 1:   #add to list
            collectionOfSick.append(coordinate(x.x, x.y))


    for x in collectionOfParticipants:
        if x.status == 0:
            for coor in collectionOfSick:
                if coor.distance(x.x,x.y)<spread_radius:
                    if random.random()<infect_probability:
                        x.status = 1
                        sickCount += 1
        if x.status == 1:
            if random.random()<dealth_probability:
                x.status = 4
            if random.random()<recover_probability:
                x.status = 3

    for x in collectionOfParticipants:
        count[x.status] +=1
    
    print(count)
    if count[1] == 0:
        sickBoolean = False


        

