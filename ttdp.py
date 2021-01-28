import math
import random
from time import process_time

import pandas as pd
# from binarytree import tree
import kdtree as kdtree
# import kdtree
import json
from mapbox import DirectionsMatrix

service = DirectionsMatrix(access_token="pk.eyJ1IjoicGF1bGFlaGFiMTIzIiwiYSI6ImNraGdndHV5azBsZm8ycm53NTZtZmNlaTUifQ.25Pi_sDAFLZFn9-IHObgzA")


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


response = service.matrix([[30.007196, 31.235327],
                            [30.052585, 31.261698],
                            [29.84955, 31.254917],
                            [30.005157, 31.230167]],
                            sources=[0], profile='mapbox/driving-traffic', annotations=['duration'])

secondes=set(x for lst in response.json()['durations'] for x in lst)
# totalTIme = convert(int(secondes[0]))
print(secondes)

places=[]
data = pd.read_csv('./museums.csv')

#store all the data in places array
for i in range(len(data)):
    name = data.iat[i, 6]
    long = data.iat[i, 5]
    lat = data.iat[i, 4]
    rate = data.iat[i, 8]
    dur = data.iat[i, 10]
    price = data.iat[i, 13]
    endTime = data.iat[i, 12]
    coordinates = [lat, long]
    image=data.iat[i,3]
    place = (name, coordinates, rate, dur, price, endTime,image)

    places.append(place)
######################################
cordinates_list = []
for index in range(len(places)):
    cordinates = places[index][1]
    cordinates_list.append(cordinates)
###############################################
tree = kdtree.KDTree(cordinates_list, leafsize=5)

lattuide = 30.044272
longtuide = 31.235685
closest = tree.query([lattuide, longtuide], 20, p=2)
print(closest)
indcies = closest[1]
print(indcies)
# 31.235685
print(places[indcies[0]][0])
print(places[indcies[1]][0])
print(places[indcies[2]][0])
print(places[indcies[3]][0])
print(places[indcies[0]][0])

# Tourist Trip Design Trip
# A* => Doesn't have a specific destination
# Cant have start == dest because the algo would not move
