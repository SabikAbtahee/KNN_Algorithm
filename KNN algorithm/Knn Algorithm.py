import pandas as pd
from sklearn.model_selection import train_test_split
from math import sqrt
from operator import attrgetter
from collections import Counter


class distanceClass:
    def __init__(self,classCount,distance):
        self.classCount=classCount
        self.distance=distance
    def __repr__(self):
        return str(self.classCount)+" : "+str(self.distance)
    
def readData():
    dataframe = pd.read_csv("wine.csv") ##glass.csv , wine.csv ,  iris.csv
    return dataframe

def iterateRows(dataframe):
    rows=[]
    
    for index, row in dataframe.iterrows():
         
         rows.append(row)
    #print(rows[8][3])
    #print (dataframe)
    return rows

def splitDataframe(dataframe,splitSize):
    train , test = train_test_split(dataframe, test_size=splitSize)
    
    return train,test

def getHighCount(classes):
    cnt = Counter(classes)
    x=cnt.most_common(1)
    return (x[0][0])
def matchWithTest(GotClass,testClass):
    if(GotClass==testClass):
        return 1
    else:
        return 0
    
    
def distance(trainRows,testRows,pk):
    ClassOfTrain=0
    dimensions=len(trainRows[0])
    
    
    match=0
    
    for i in range(len(testRows)):
        distances=[]
        for j in range(len(trainRows)):
            a=0
            for k in range(dimensions):
                if (k!=0):
                    a+=(trainRows[j][k]-testRows[i][k])**2
                else:
                   ClassOfTrain=trainRows[j][k]
            
            distances.append(distanceClass(ClassOfTrain,sqrt(a)))
        
        MainK=0
        classes=[]
        for x in sorted(distances,key=attrgetter('distance')):
           
           if(MainK<pk):
               classes.append(x.classCount)
               MainK+=1
           else:
               break
        
        GotClass=getHighCount(classes)
        match+=matchWithTest(GotClass,testRows[i][0])
    
    return match
    
        #matchWithTest(GotClass,)
   
    
def CalculateAccuracy(matches,total):
    avg=sum(matches)/len(matches)
    
    #print(avg)
    #print(total)
    
    accuracy=(avg/total)*100
    print("\n\nACCURACY is {}%".format(accuracy))
def main():
    matches=[]
    k=3
    testRun=10
    splitSize=0.05
    dataframe=readData()
    for i in range(testRun):
        #print (i)
        train,test=splitDataframe(dataframe,splitSize)
        
        trainRows=iterateRows(train)
        
        testRows=iterateRows(test)
        #print(testRows[0][1])
        
        x=distance(trainRows,testRows,k)
        matches.append(x)
    
    CalculateAccuracy(matches,len(testRows))
    
    
if __name__=="__main__":
    main()