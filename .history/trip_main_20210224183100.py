import math
import random
import pandas as pd
# from scipy import spatial
import kdtree as kdtree

# To convert the lat and long to distance
def cartesian(latitude, longitude, elevation=0):
    # Convert to radians
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)
    return (latitude, longitude)


places = []
data = pd.read_csv('museums.csv')

def Program(array, Startpoint, startTime, time, budget):
    programs_list=[]
    program = []
    i = 0
    totalhours = 0
    totalbudget = 0
    startpoint = Startpoint
    startTime = startTime
    totaltime=time
    neddedbudget=budget

    while True:
        if (i < 20):    # length array
            # and places[array[i]][2] >= 3
            # check the start time of the place
            if places[array[i]][5] >= startTime:
                totalhours += places[array[i]][3]
                totalbudget += places[array[i]][4]

                # To add: traffic time
                program.append(
                    {
                        "From": f'{startTime}',
                        "To": f"{round(startTime + places[array[i]][3], 2)}",
                        "you will visit": f"{places[array[i]][0]}",
                        "rating of this place is ": f"{places[array[i]][2]}",
                        "The cost is ": f"{places[array[i]][4]}",
                     }
                )
                #to change the startTime value
                startTime = round(startTime + places[array[i]][3], 2)
                i += 1
            else:
                continue
            if totalhours >= totaltime or totalbudget == neddedbudget:
                break

    return program, totalhours, totalbudget
    # print("Your program sir is : \n", program)
    # print("the total hours of your program is :", round(totalhours, 2))
    # print("the total Budget of your program is :", totalbudget)
    # print('\n')

######################################################

# store all the data in places array
for i in range(len(data)):
    lat = data.iat[i, 4]
    lng = data.iat[i, 5]
    name = data.iat[i, 6]
    rate = data.iat[i, 8]
    dur = data.iat[i, 10]
    price = data.iat[i, 13]
    endTime = data.iat[i, 12]
    coordinates = [lat, lng]
    cartesian_coord = cartesian(*coordinates)

    place = (name, cartesian_coord, rate, dur, price, endTime)
    places.append(place)


# build the kTree depending on the lat and lng
x = []
for index in range(len(places)):
    lat = places[index][1][0]
    lng = places[index][1][1]
    f = (lat, lng)
    x.append(f)
tree = kdtree.KDTree(x, leafsize=50)    # leafsize => optional


def find_population(lat, lon, startTime, time, budget):
    programs_list=[]
    time = time
    budget = budget
    cartesian_coord = cartesian(lat, lon)
    lattuide = cartesian_coord[0]
    longtuide = cartesian_coord[1]
    # preform the Kdtree to find the nearest places
    closest = tree.query([lattuide, longtuide], 20, p=2)   # display closest
    # print('Closest: \n ', closest)
    #get the indexes of the nearets places in the Xcel sheet
    indcies = closest[1]
    prog1,totalhours,totalmoney= Program(indcies, cartesian_coord, startTime, time, budget)
    programs_list.append(
        {
            "program":prog1,
            "totalhours":float(totalhours),
            "totalmoney":float(totalmoney)
        }
    )
    print(f'[DEBUG] Program 1: {prog1}')
    for i in range(3):
        copy = indcies[1:]
        random.shuffle(copy)
        indcies[1:] = copy
        prog1, totalhours, totalmoney = Program(indcies, cartesian_coord, startTime, time, budget)
        programs_list.append(
            {
                "program": prog1,
                "totalhours": float(totalhours),
                "totalmoney": float(totalmoney)
            }
        )
    print(f'[DE')
    return programs_list


# input for the main function -> find_population is the following
# This should be the input of the REST API
budget = 200
time = 8
lat = 30.050053
long = 31.235964

if __name__ == '__main__':
    # this result is the ouput
    result = find_population(lat, long, 9, time, budget)
    print(result)

#output is a list conatin 5 programs each program(type:list of {}),total hours,total money
#
# # if you want to access the fist program
#     print(result[0]['program'])
# # if you want to acess the details of the first  program list the first elment of this json
#     print(result[0]['program'][0])
# # if you want to acess the details of the program list the first elment of this json and the first elment in it
#     print(result[0]['program'][0]['From'])
# #if you want to access the total hours of program and the same for total money
#     print(result[0]['totalhours'])


