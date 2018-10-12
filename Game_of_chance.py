
list_of_expect = {}
def nodicethrow(a,b,c):
    p0=1
    v0=a+b+c
    p0v0=p0*v0
    list_of_expect["ZERO"]=p0v0

def onedicethrow(a,b,c):

    # CASE A: FIRST DICE IS THROWN
    vA = 0
    pvA = 0
    for j in range(1, 7):
        vA = j + b + c
        pvA = pvA + (1 / 6.0) * vA
    list_of_expect["A"]=pvA

    # CASE B: SECOND DICE IS THROWN
    vB = 0
    pvB = 0
    for j in range(1, 7):
        vB = a + j + c
        pvB = pvB + (1 / 6.0) * vB
    list_of_expect["B"]=pvB

    # CASE C: THIRD DICE IS THROWN
    vC = 0
    pvC = 0
    for j in range(1, 7):
        vC = a + b + j
        pvC = pvC + (1 / 6.0) * vC
    list_of_expect["C"] = pvC

def twodicethrow(a,b,c):
    p = 0
    sum = 0
    pab = 0
    pbc = 0
    pac = 0

    for i in range(1, 7):
        for j in range(1, 7):
            #CASE 1: A AND B ARE THROWN
            sumab = i + j + c
            pab = pab + (1 / 36.0) * sumab
    list_of_expect["AB"] = pab
    for i in range(1, 7):
        for j in range(1, 7):
            #CASE 2: B AND C ARE THROWN
            sumbc = a + i + j
            pbc = pbc + (1 / 36.0) * sumbc
    list_of_expect["BC"] = pbc

    for i in range(1, 7):
        for j in range(1, 7):
            #CASE 3: A AND C ARE THROWN
            sumac = i + b + j
            pac = pac + (1 / 36.0) * sumac
    list_of_expect["AC"] = pac

def threedicethrow(a,b,c):
    sumabc = 0
    pabc = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                sumabc = i + j + k
                pabc = pabc + (1 / 216.0) * sumabc
    list_of_expect["ABC"] = pabc



a=input("Enter first dice roll")
b=input("Enter second dice roll")
c=input("Enter third dice roll")
print "YOU ENTERED A={}, B={}, C={}".format(a,b,c)

if a>=1 and a<=6 and b>=1 and b<=6 and c>=1 and c<=6:
    nodicethrow(a,b,c)
    onedicethrow(a,b,c)
    twodicethrow(a,b,c)
    threedicethrow(a,b,c)

    maxvalue = max(list_of_expect.values())
    for key,value in list_of_expect.items():
        if value==maxvalue:
            name=key
            break

    if a == b == c:
        print "YOU WON"
    elif name == "A":
        print "ROLL DICE A"
    elif name == "B":
        print "ROLL DICE B"
    elif name == "C":
        print "ROLL DICE C"
    elif name == "AB":
        print "ROLL DICE A and B"
    elif name == "BC":
        print "ROLL DICE B and C"
    elif name == "AC":
        print "ROLL DICE A and C"
    elif name == "ABC":
        print "ROLL DICE A,B AND C"
    elif name == "ZERO":
        print "STOP: DO NOT ROLL ANYMORE"

else:
    print "INVALID INPUT"





