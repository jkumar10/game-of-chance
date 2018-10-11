import sys

# INPUTTING THE INITIAL ROLL
a=5
b=5
c=1
sum=a+b+c


for i in range(1,3):
    # THROWING ONLY ONE DICE
    if i==1:
        l1=[]
        # CASE A: FOR THROWING DICE A
        vA=0
        pvA=0
        for j in range(a,7):
            vA=j+b+c
            pvA=pvA+(1/6.0)*vA
        l1.append(pvA)


        # CASE B: FOR THROWING DICE B
        vB=0
        pvB=0
        for j in range(b,7):
            vB=a+j+c
            pvB=pvB+(1/6.0)*vB
        l1.append(pvB)

        # CASE C: FOR THROWING DICE C
        vC=0
        pvC=0
        for j in range(c,7):
            vC=a+b+j
            pvC=pvC+(1/6.0)*vC
        l1.append(pvC)

    # THROWING TWO DICES
    if i==2:

        p = 0
        sum = 0
        l = []
        pab = 0
        pbc = 0
        pac = 0

        for i in range(1, 7):
            for j in range(1, 7):
                sumab = i + j + c
                if sumab > a + b + c:
                    pab = pab + (1 / 36.0) * sumab
                    l1.append(pab)

                sumbc = a + i + j
                if sumbc > a + b + c:
                    pbc = pbc + (1 / 36.0) * sumbc
                    l1.append(pbc)

                sumac = i + b + j
                if sumac > a + b + c:
                    pac = pac + (1 / 36.0) * sumac
                    l1.append(pac)


        maxPiVi=max(l1)
        if a==b==c:
            print "YOU WON"
        else:
            if maxPiVi == pvA:
                print "THROW DICE A"
            elif maxPiVi == pvB:
                print "THROW DICE B"
            elif maxPiVi == pvC:
                print "THROW DICE C"

            elif maxPiVi == pab:
                print "THROW DICE AB"

            elif maxPiVi == pbc:
                print "THROW DICE BC"

            else:
                print "THROW DICE AC"











