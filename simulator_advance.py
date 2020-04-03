import random 
import matplotlib.pyplot as plt
import numpy as np
import time

class human:
    def __init__(self,x,y,status=0):
        self.x = random.randint(0,x-1)
        self.y = random.randint(0,y-1)
        self.status=status
        self.xspeed = random.randint(xs*-1, xs)
        self.yspeed = random.randint(ys*-1, ys)

def setup():
    for x in range(width):
        temp = {}
        for y in range(height):
            temp[y] = [0]
        map[x] = temp

    for p in range(samples-sicksamples):
        t = human(width,height)
        mapIndex[p+1] = t
        map[t.x][t.y].append(p+1)

    for p in range(sicksamples):
        t = human(width, height, status=1)
        mapIndex[samples-sicksamples+1+p] = t
        map[t.x][t.y].append(samples-sicksamples+p)

def move(id, h):
    map[h.x][h.y].remove(id)
    h.x += h.xspeed
    h.y += h.yspeed
    if h.x <= 0:
        h.x = 1
        h.xspeed = random.randint(1, xs)
    if h.x >=width:
        h.x = width-1
        h.xspeed = random.randint(0-xs, -1)
    if h.y <= 0 :
        h.y = 1
        h.yspeed = random.randint(1, ys)
    if h.y >= height:
        h.y = height-1
        h.yspeed = random.randint(0-ys, -1)
    map[h.x][h.y].append(id)



    

mapIndex = {}
map = {}

width = 10
height = 10
samples = 10 # number of people
sicksamples = 0
xs = 3  
ys = 3
setup()

while True:
    for id in mapIndex.keys():
        h = mapIndex[id]
        move(id, h)
    for h in mapIndex.keys():
        f = mapIndex[h]
        print('ID: {}; x: {}; y: {}; status: {}'.format(h,f.x,f.y,f.status))


    time.sleep(1)
    





# for h in mapIndex.keys():
#     f = mapIndex[h]
#     print('ID: {}; x: {}; y: {}; status: {}'.format(h,f.x,f.y,f.status))



for x in range(width):
    for y in range(height):
        print("width: {}; height: {}; List: {}".format(x,y,str(map[x][y])))