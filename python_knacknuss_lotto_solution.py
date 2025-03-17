###############################################
#  Solution for ALGO Knacknuss : LOTTOZahlen  #
#  mike                                       #
###############################################

#empty dictionary is created. all posibilities are initialized with 0
def initializeDict():
    combDict = {}
    for i in range (21, 280):
        combDict.update({str(i): 0})
    return combDict

#printer function for dict
def printDict(dict):
    for i in dict:
        print(str(i) + ":", end=" ")
        print(dict[i], end="\t")
        if (int(i)%4 == 0):
            print()
    print()
    print()

#is called twice. first for collect all sum-posibilities. second for calculate all posibilites 
def incrementPosibilities(firstRound):
    result=0
    summe=0
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    while True:
        if(firstRound): #first round. collect all sum-posibilities
            combinationDict.update({str(a+b+c+d+e+f):combinationDict[str(a+b+c+d+e+f)]+1})
        else: #second round. calculate solution
            summe=a+b+c+d+e+f
            if (summe * combinationDict[str(summe)] == (a*b*c*d*e*f)):
                print(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f), end=" => ")
                print(str(summe))
                if(a*b*c*d*e*f > 2000000): #tasks says, that product of numbers counts multiple millions
                    print ("Number on paper is : " + str(summe))
                    print ("Used numbers are: " + str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f))
        f+=1
        if a<45 and b<46 and c<47 and d<48 and e<49 and f==50:
            e+=1
            f=e+1
        if a<45 and b<46 and c<47 and d<48 and e==49 and f==50:
            d+=1
            e=d+1
            f=e+1
        if a<45 and b<46 and c<47 and d==48 and e==49 and f==50:
            c+=1
            d=c+1
            e=d+1
            f=e+1
        if a<45 and b<46 and c==47 and d==48 and e==49 and f==50:
            b+=1
            c=b+1
            d=c+1
            e=d+1
            f=e+1
        if a<45 and b==46 and c==47 and d==48 and e==49 and f==50:
            a+=1
            b=a+1
            c=b+1
            d=c+1
            e=d+1
            f=e+1
        if a==45 and b==46 and c==47 and d==48 and e==49 and f==50:
            break;

combinationDict = initializeDict()
incrementPosibilities(True)
printDict(combinationDict)
incrementPosibilities(False)


        
                        
                        
