import random
import math
import operator
def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=4
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
                   neighbors.append(distances[x][0])
    return neighbors
    








def convert_str_to_float(x,n):
    for i in range(n):
        x[i]=float(x[i])
    return x

def load_split_data(split,training_data=[],test_data=[]):
    for line in open("iris.txt","r"):
        temp = convert_str_to_float(line[0:-1].split(','),4)
        if random.random()<=split:
            training_data.append(temp)
        else:
            test_data.append(temp)
    return(training_data,test_data)
def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
