
list_of_expect = {}
def nodicethrow(a,b,c):
    PiVi0=1
    PiVi0v0=PiVi0*(a+b+c)
    list_of_expect["ZERO"]=PiVi0v0

def onedicethrow(a,b,c):
    PiViA=0
    PiViB=0
    PiViC=0
    for j in range(1, 7):
        PiViA = PiViA + (1 / 6.0) * (j+b+c)
        PiViB = PiViB + (1 / 6.0) * (a+j+c)
        PiViC = PiViC + (1 / 6.0) * (a+b+j)
    list_of_expect["A"]=PiViA
    list_of_expect["B"]=PiViB
    list_of_expect["C"]=PiViC

def twodicethrow(a,b,c):
    PiViab = 0
    PiVibc = 0
    PiViac = 0
    for i in range(1, 7):
        for j in range(1, 7):
            PiViab = PiViab + (1 / 36.0) * (i+j+c)
            PiVibc = PiVibc + (1 / 36.0) * (a+i+j)
            PiViac = PiViac + (1 / 36.0) * (i+b+j)
    list_of_expect["AB"] = PiViab
    list_of_expect["BC"] = PiVibc
    list_of_expect["AC"] = PiViac

def threedicethrow(a,b,c):
    PiViabc = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                PiViabc = PiViabc + (1 / 216.0) * (i+j+k)
    list_of_expect["ABC"] = PiViabc



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
        print "SUGGESTION:"
        print "ROLL DICE A"
    elif name == "B":
        print "SUGGESTION:"
        print "ROLL DICE B"
    elif name == "C":
        print "SUGGESTION:"
        print "ROLL DICE C"
    elif name == "AB":
        print "SUGGESTION:"
        print "ROLL DICE A and B"
    elif name == "BC":
        print "SUGGESTION:"
        print "ROLL DICE B and C"
    elif name == "AC":
        print "SUGGESTION:"
        print "ROLL DICE A and C"
    elif name == "ABC":
        print "SUGGESTION:"
        print "ROLL DICE A,B AND C"
    elif name == "ZERO":
        print "SUGGESTION:"
        print "STOP: DO NOT ROLL ANYMORE"

else:
    print "INVALID INPUT"





