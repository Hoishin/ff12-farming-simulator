import random

l = 0 # chain level
m = 0 # 1 if it is in Chance mode, otherwise 0
c = -1 # chain counter (=/= chains)
cc = -1 # chain counter for chance mode
b = 0 # books in a loot
s = 0 # staves in a loot
book = 0 # total drops in one set of dustia farming
staff = 0 # total drops in one set of dustia farming
gil = 0 # gil in one set of dustia farming
booksum = 0 # to be devided by sample size
staffsum = 0 # to be devided by sample size
gilsum = 0 # to be devided by sample size

# input area
wait = 3 # level you start picking up from. LEVEL 0 = FIRST LEVEL, LEVEL 1 = BLUE LEVEL
dustiamax = 164 # number of dustia you farm
test = 10000 # sample size

# dictionaries
bdrop = { 0: 0.4, 1: 0.45, 2: 0.50, 3: 0.55 }
sdrop = { 0: 0.03, 1: 0.06, 2: 0.08, 3: 0.12 }
lvlchance = {
    0: { 6: 0.4, 7: 0.6, 8: 0.8, 9: 0.9 },
    1: { 6: 0.2, 7: 0.3, 8: 0.5, 9: 0.6 },
    2: { 6: 0.1, 7: 0.2, 8: 0.3, 9: 0.4 }
}
forcedlvl = { 0: 31, 1: 51, 2: 81}

#functions
def levelup(): # executed when leveling up
    global l, c, cc
    l = l + 1
    c = 0
    cc = 0

def pickup(): # executed when picking up a loot
    global book, staff, b, s
    book = book + b
    staff= staff + s

def level(x): # checks if it levels up or not
    global l, cc, r
    if x <= 5:
        pass
    elif x >= 10 or cc >= forcedlvl[l]:
        return levelup()
    elif r < lvlchance[l][x]:
        return levelup()

for dustia in range (1, dustiamax + 1):
    booksum = staffsum = gilsum = 0
    for t in range (1, test + 1): # 1 set of dustia farming

        l = 0 # resetting variables for new dustia farming
        c = -1
        cc = -1
        m = 0
        book = 0
        staff = 0
        gil = 0
        
        for n in range (1, dustia + 1): # one dustia kill
            
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
            r1 = random.random() # RNG for book
            r2 = random.random() # RNG for staff
            rr1 = random.random() # amount of books
            rr2 = random.random() # amount of staff

            if r1 < bdrop[l]:
                if n <= 10:
                    b = 1
                elif n <= 18:
                    if rr1 < 0.35:
                        b = 2
                    else: b = 1
                elif n <= 26:
                    if rr1 < 0.2:
                        b = 3
                    elif rr1 < 0.7:
                        b = 2
                    else: b = 1
                else:
                    if rr1 < 0.1:
                        b = 4
                    elif rr1 < 0.4:
                        b = 3
                    else: b = 2
                    
            if r2 < sdrop[l]:
                if n <= 18:
                    s = 1
                elif n <= 26:
                    if rr2 < 0.2:
                            s = 2
                    else: s = 1
                elif n >= 27:
                    if rr2 < 0.05:
                            s = 4
                    elif rr2 < 0.15:
                            s = 3
                    elif rr2 < 0.4:
                            s = 2
                    else: s = 1

            # if you pick up or not. if you do, subtracts certain number from c, not cc
            if b > 0 or s > 0:
                if wait <= l:
                    pickup()
                    if l <= 2:
                        c = c - l - 1
            
            b = 0
            s = 0

        booksum = booksum + book
        staffsum = staffsum + staff

        if staff == 0:
            sellstaff = -2
        elif staff == 1:
            sellstaff = 0
        else:
            sellstaff = staff - 1

        gil = book * 532 + sellstaff * 1200

        booksum = booksum + book
        staffsum = staffsum + staff
        gilsum = gilsum + gil

        #print(book, staff, gil)
        #print(gil)
            

    avgbook = booksum / test
    avgstaff = staffsum / test
    avggil = gilsum / test

    #print (avgbook)
    #print (avgstaff)
    print(avggil)
