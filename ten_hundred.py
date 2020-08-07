# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:23:17 2020

@author: pulkit
"""
import csv
import math
import numpy as np
#import os

def load_data(filepath):
    ret = []
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            del row['Long']
            del row['Lat']
            ret.append(row)
    #print(ret[0])
    return ret

def calculate_x_y(time_series):
    latestCases = time_series[list(time_series.keys())[-1]]
    earliestCases = time_series[list(time_series.keys())[2]]
    retup =()
    x = 0
    y = 0
    #for k, v in reversed(time_series.items()):
        #print(k,"->",v)
    for k, v in reversed(time_series.items()):
        if(str.isdigit(v) == False):
            break
        val = int(v)
        if(val <= int(latestCases)/10):
            break
        else:
            x = x + 1
    for k, v in reversed(time_series.items()):
        if(str.isdigit(v) == False):
            break
        val = int(v)
        if(val <= int(latestCases)/100):
            break
        else:
            y = y + 1
    y = y - x
    if(int(earliestCases) > int(latestCases)/10):
        x = math.nan
    if(int(earliestCases) > int(latestCases)/100):
        y = math.nan
    if(int(earliestCases) == 0 and int(latestCases) == 0):
        x = math.nan
        y = math.nan
    retup = (x,y)
    #print(retup)
    return retup


def get_dist(first, second):
    mini = 10000
    for i in range(len(first)):
        for j in range(len(second)):
            dist = math.sqrt((first[i][0] - second[j][0]) * (first[i][0] - second[j][0]) + (first[i][1] - second[j][1]) * (first[i][1] - second[j][1]))
            if(dist < mini):
                mini = dist
    return mini


def min_dist(dataset):
    x = 0
    y = 0
    mini = 10000
    dist = 0
    #print(dataset[0])
    for i in range(len(dataset)):
        if(len(dataset[i]) == 0):
            continue
        for j in range(i + 1, len(dataset)):
            if(len(dataset[j]) == 0):
                continue
            dist = get_dist(dataset[i], dataset[j])
            if(dist < mini):
                mini = dist
                x = i
                y = j
    
    
    return x, y, mini
    

def create_dataset():
    a = load_data("time_series_covid19_confirmed_global.csv")
    ret = []
    for i in range(len(a)):
        tup = calculate_x_y(a[i])
        ret.append(tup)
             
    ret = np.array(ret)
    
    return ret


def hac(dataset):
    ret = []
    mainList = []
    
    for i in range(len(dataset)):
        if(math.isnan(dataset[i][0]) or math.isnan(dataset[i][1])):
            continue;
        else:
            ret.append(dataset[i])
    
    for i in range(len(ret)):
        a = [ret[i]]
        mainList.append(a)
    #print(ret[0])
    clusters = np.zeros((len(ret) - 1, 4))
    
    for i in range(len(clusters)):
        x, y, dist = min_dist(mainList)
        
        clusters[i][0] = x
        clusters[i][1] = y
        clusters[i][2] = dist
        
        clusters[i][3] = len(mainList[x]) + len(mainList[y])
        for j in range(len(mainList[y])):
            temp = mainList[y][j]
            mainList[x].append(temp)
        
        mainList.append(mainList[x])
        mainList[x] = []
        mainList[y] = []
        
#    for i in range(len(clusters)):
#        print(clusters[i])
    clusters = np.array(clusters)
    return clusters
    
def main():
    create_dataset()
    
if __name__ == "__main__":
    main()