import random

l = 0 # chain level
m = 0 # 1 if it is in Chance mode, otherwise 0
c = -1 # chain counter (=/= chains)
cc = -1 # chain counter for chance mode
d1 = d2 = d3 = d4 = 0 # in a loot
bone = stone = antidote = helm = gil = 0 # one skeleton farming
gilsum = 0 # for average

# input area
wait = 0 # level you start picking up from. LEVEL 0 = FIRST LEVEL, LEVEL 1 = BLUE LEVEL
skele = 8 # number of dustia you farm
test = 1000 # sample size

# dictionaries

drop = {  # drop[chainlv][item]
    0: {1: 0.4, 2: 0.25, 3: 0.03, 4: 0.01},
    1: {1: 0.45, 2: 0.3, 3: 0.06, 4: 0.02},
    2: {1: 0.5, 2: 0.35, 3: 0.08, 4: 0.03},
    3: {1: 0.55, 2: 0.4, 3: 0.12, 4: 0.05}
}

lvlchance = {
    0: {6: 0.4, 7: 0.6, 8: 0.8, 9: 0.9},
    1: {6: 0.2, 7: 0.3, 8: 0.5, 9: 0.6},
    2: {6: 0.1, 7: 0.2, 8: 0.3, 9: 0.4}
}
forcedlvl = {0: 31, 1: 51, 2: 81}

#functions
def levelup(): # executed when leveling up
    global l, c, cc
    l = l + 1
    c = 0
    cc = 0

def pickup(): # executed when picking up a loot
    global d1, d2, d3, d4, bone, stone, antidote, helm
    bone = bone + d1
    stone = stone + d2
    antidote = antidote + d3
    helm = helm + d4

def level(x): # checks if it levels up or not
    global l, cc, r
    if x <= 5:
        pass
    elif x >= 10 or cc >= forcedlvl[l]:
        return levelup()
    elif r < lvlchance[l][x]:
        return levelup()

for t in range (test): # 1 set of dustia farming

    l = 0 # resetting variables for new dustia farming
    c = cc = -1
    m = 0
    bone = stone = antidote = helm = gil = 0
    
    for n in range (1, skele + 1): # one skeleton steal & kill

        # steal
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        if r1 >= 0.03: # ignores Dark Mote chance (3%)
            if r2 < 0.1:
                gil = gil + 10
            elif r3 < 0.55:
                bone = bone + 1
        
        # kill
        c = c + 1 # first, increase the chain counter
        cc = cc + 1 # and, increase this too

        # chain level up or not
        r = random.random()
        if l <= 2:
            if m == 1: # if in chance mode, use cc instead of c
                level(cc)            
            else: # not in chance mode, using c
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
        rr1 = random.random()
        rr2 = random.random()
        rr3 = random.random()
        rr4 = random.random()

        if r1 < drop[l][1]:
            if n <= 10:
                d1 = 1
            elif n <= 18:
                if rr1 < 0.35:
                    d1 = 2
                else: d1 = 1
            elif n <= 26:
                if rr1 < 0.2:
                    d1 = 3
                if rr1 < 0.7:
                    d1 = 2
                else: d1 = 1
            else:
                if rr1 < 0.1:
                    d1 = 4
                elif rr1 < 0.4:
                    d1 = 3
                else: d1 = 2

        if r2 < drop[l][2]:
            if n <= 10:
                d2 = 1
            elif n <= 18:
                if rr2 < 0.3:
                    d2 = 2
                else: d2 = 1
            elif n < 26:
                if rr2 < 0.1:
                    d2 = 3
                elif rr2 < 0.6:
                    d2 = 2
                else: d2 = 1
            else:
                if rr2 < 0.5:
                    d2 = 4
                elif rr2 < 0.2:
                    d2 = 3
                else: d2 = 2
                
        if r3 < drop[l][3]:
            if n <= 18:
                d3 = 1
            elif n <= 26:
                if rr3 < 0.2:
                        d3 = 2
                else: d3 = 1
            else:
                if rr3 < 0.05:
                        d3 = 4
                elif rr3 < 0.15:
                        d3 = 3
                elif rr3 < 0.4:
                        d3 = 2
                else: d3 = 1

        if r4 < drop[l][4]:
            if n <= 18:
                d4 = 1
            elif n <= 26:
                if rr4 < 0.05:
                    d4 = 2
            else:
                if rr4 < 0.1:
                    d4 = 2
                else: d4 = 1

        # if you pick up or not. if you do, subtracts certain number from c, not cc
        if d1 > 0 or d2 > 0 or d3 > 0 or d4 > 0:
            if wait <= l:
                pickup()
                if l <= 2:
                    c = c - l - 1
        
        d1 = d2 = d3 = d4 = 0

    gil = gil + bone * 193 + stone * 35 + antidote * 25 + helm * 700
    gilsum = gilsum + gil
    #print(bone)
    #print(gil)
    
avggil = gilsum / test

print(avggil)
