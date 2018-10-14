# My basic strategy to solve this question is to find the utility value or expectation value of each successor.
# The total sum of the utility value of each successor will give us the utility value of the chance node.
# The node with the highest utility value will be the favourable move.
# Keeping this in mind I have calculated the utility value of 'one dice throw' (3 cases), 'two dice throw' (3 cases),
# 'three dice throw' (1 case) and 'no dice throw' such that the successor state will always have the sum of the digits greater than the
# initial state. The maximum utility value of the state will be whose sum of the digits will be the maximum and hence that will be our favorable move.
# VARIABLE DESCRIPTION:
# PiVi0 = Expected Utility value of throwing zero dice
# PiViA, PiViB, and PiViC = Expected Utility value of throwing dice A, B and C
# PiViab, PiVibc, PiViac = Expected Utility value of throwing dice AB, AC and BC
# PiViabc = Expected Utility values of throwing all dice
# list_of_expect= This is a dictionary which will contain all the utility values. The key denotes the dice while value is the utility.

list_of_expect = {}

# Method to calculate the utility value of zero dice throw
def nodicethrow(a,b,c):
    PiVi0=1
    PiVi0v0=PiVi0*(a+b+c)
    list_of_expect["ZERO"]=PiVi0v0

# Method to calculate the utility value of one dice throw
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

# Method to calculate the utility value of two dice throw
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

# Method to calculate the utility value of three dice throw
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

# Calling methods if and only if it is a valid dice throw.
if a>=1 and a<=6 and b>=1 and b<=6 and c>=1 and c<=6:
    nodicethrow(a,b,c)
    onedicethrow(a,b,c)
    twodicethrow(a,b,c)
    threedicethrow(a,b,c)

# The maxium of the utility values is the favorable move.
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





