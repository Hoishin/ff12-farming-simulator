import random
"""
import numpy
import matplotlib.pyplot as plt
"""

# kill a jelly: n
# kill certain amount of jellies in a room: jellyperroom
# do certain amount of rooms in a round: rooms

l = m = 0 # chain level and chance mode
c = cc = -1 # chain counter. c is for non-chance mode, cc is for chance mode (ignores how many you pick up).
jelly = 0 # total jelly kill counter for multiple drop
dropcount = 0 # just a counter
yl = 0 # in a room
liquid = 0 # in a round

cl = 0 # when you start picking up
rooms = 5
test = 100000

yldic = []

r1drop = {0: 0.4, 1: 0.45, 2: 0.50, 3: 0.55}
r2drop = {0: 0.25, 1: 0.30, 2: 0.35, 3: 0.40}
r3drop = {0: 0.03, 1: 0.06, 2: 0.08, 3: 0.12}
r4drop = {0: 0.01, 1: 0.02, 2: 0.03, 3: 0.05}
lvchance = {
    0: {6: 0.4, 7: 0.6, 8: 0.8, 9: 0.9},
    1: {6: 0.2, 7: 0.3, 8: 0.5, 9: 0.6},
    2: {6: 0.1, 7: 0.2, 8: 0.3, 9: 0.4}
}
forcedlv = {0: 31, 1: 51, 2: 81}

#f = open('%srooms_cl%s.dat'%(rooms, cl),'w')

def level(x):
    global l, c, cc, r
    if x >= 6:
        if x >= 10 or cc >= forcedlv[l]:
            l += 1
            c = cc = 0
        elif r < lvchance[l][x]:
            l += 1
            c = cc = 0

def count_matching(condition, seq):
    return sum(1 for item in seq if item==condition)
    
for t in range (test): # each test

    for room in range (rooms): # each room
        
        r = random.random()
        if r < 0.0561:
            jellyperroom = 12
        elif r < 0.1308:
            jellyperroom = 13
        elif r < 0.243:
            jellyperroom = 14
        elif r < 0.4019:
            jellyperroom = 15
        elif r < 0.6542:
            jellyperroom = 16
        elif r < 0.8318:
            jellyperroom = 17
        elif r < 0.8785:
            jellyperroom = 18
        elif r < 0.9159:
            jellyperroom = 19
        elif r < 0.972:
            jellyperroom = 20
        else:
            jellyperroom = 22
            
        for n in range (jellyperroom):
            c += 1
            cc += 1
            jelly += 1

            # chain level up
            r = random.random()
            if l <= 2:
                if m == 1:
                    level(cc)
                else:
                    level(c)

            # chance mode
            r = random.random()
            if m == 1 and r < 0.4:
                m = 0
            elif m == 0 and r < 0.05:
                m = 1

            # drops
            r1 = random.random()
            r2 = random.random()
            r3 = random.random()
            r4 = random.random()
            rr2 = random.random()

            drop = 0 # 1 if dropped, 0 if not

            if r2 < r2drop[l]:
                drop = 1
                if jelly <= 10:
                    yl += 1
                elif jelly <= 18:
                    if rr2 < 0.3:
                        yl += 2
                    else:
                        yl += 1
                elif jelly <= 26:
                    if rr2 < 0.1:
                        yl += 3
                    elif rr2 < 0.6:
                        yl += 2
                    else:
                        yl += 1
                elif rr2 < 0.05:
                    yl += 4
                elif rr2 < 0.2:
                    yl += 3
                else:
                    yl += 2
            elif r1 < r1drop[l]:
                drop = 1
            elif r3 < r3drop[l]:
                drop = 1
            elif r4 < r4drop[l]:
                drop = 1

            dropcount += drop
                
        if cl <= l:
            liquid += yl
            if l <= 2:
                c -= dropcount*(l + 1)
        
        wm = yl = 0

    if liquid > 99:
        liquid = 99
    yldic += [liquid]

    #f.write(str(liquid)+"\n")
    liquid = 0
    l = m = 0
    c = cc = -1
    jelly = 0

#print(numpy.mean(yldic))
"""
ylbin = []
for nnn in range(100):
    ylbin += [nnn]
"""
"""
plt.hist(yldic, bins=ylbin)
plt.title("%s rooms CL%s"%(rooms, cl))
plt.show()
"""
#print(numpy.histogram(yldic, bins=ylbin))

for xx in range (100):
    print(xx, count_matching(xx, yldic))
