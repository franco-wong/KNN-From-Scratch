'''
@author: francowong
'''
import csv
import random
from math import sqrt
from operator import itemgetter
from collections import Counter


def loadDataSet(fileName,k,trainingData,testData):
    
    with open(fileName, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        
        k_size=len(dataset)/k
          
        for i in range(k):
            k_start=i*k_size
            k_end=k_start+k_size
            for j in range(k_size):
                if(k_start <=i and i < k_end):
                    testData.append(dataset[j])
                else:
                    trainingData.append(dataset[j])


def euclidean_distance(p_one,p_two):
    distance=0;
    
    for i in range(1,10):
        distance += pow((float(p_one[i])-float(p_two[i])),2)
    
    return sqrt(distance)

    
def get_neighbor(training_model,test_model,knn):
    predictions=[]
    
    for j in range(len(test_model)):
        targets=[]
        distances=[]
        
        for i in range(len(training_model)):
            distance=euclidean_distance(test_model[j],training_model[i])
            
            distances.append([distance,i])
        
        distances=sorted(distances, key=itemgetter(0));
        
        for i in range(knn):
            targets.append(training_model[distances[i][1]][10])
            
        data=Counter(targets)

        n=data.most_common(1)
        mode=n[0][1]
        
        if(mode == (knn/2)):
            predictions.append([random.randint(1,2)*2,j])
        else:
            predictions.append([n[0][0],j])
        
    accuracies=+accu(predictions,test_model)
    
    return accuracies

def accu(predictions,test_model):
    count = 0
    
    pred_length=len(test_model)
    for i in range(pred_length):
        if(predictions[i][0] == test_model[i][10]):
            count=count+1

    percentage=count/pred_length
    
    return percentage

def main():
    
    trainingData = []
    testData = []
    fileName = 'breast-cancer-wisconsin.data.webarchive'

    loadDataSet(fileName,10,trainingData, testData)
    print 'Training Data: '+repr(len(trainingData))
    print 'Test Data: '+repr(len(testData))
    for i in range(1,31):
        print(get_neighbor(trainingData, testData, i))

    pass

main()