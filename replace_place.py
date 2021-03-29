import pandas as pd

data = pd.read_csv('museums1.csv')


def replace_place(global_price, program, index):
    '''
    Replace a place whose index is `index` with three other places

    Args:
        full_program (dict): dict containing list of places in a program
        index (int): index of place to be removed

    Returns:
        alternate_places (list of dicts): nearest three places to that removed
    '''
    alternate_places = []
    dist_dict = {}
    num_of_places = 3

    places_in_program = [program[i]['visit'] for i in range(len(program))]

    ptbr = program[index]['visit']    # name of place to be removes
    start_time = program[index]['from']
    ptbr_lng = float(data[data['name'] == ptbr]['longitude'])
    ptbr_lat = float(data[data['name'] == ptbr]['latitude'])

    # Calculate EucDist between this place and all others
    # Save in dict {place: dist}
    for i, row in data.iterrows():
        place = row['name']
        lng = row['longitude']
        lat = row['latitude']

        euc_dist = (((ptbr_lng - lng)**2 + (ptbr_lat - lat)**2)**1/2)*10000
        # print(f'[DEBUG] Distance between {ptbr} and {place} is {euc_dist}')

        # Remove enteries that are already in the program
        if place not in places_in_program:
            dist_dict[place] = euc_dist

    # Sort dict by distance ascendingly
    dist_dict = dict(sorted(dist_dict.items(), key=lambda item: item[1]))

    # Get list of first three places
    nearest_places = list(dist_dict.keys())[:num_of_places]
    # print(f'[DEBUG] Nearest places: {nearest_places}')

    # Get info of first three places (from, to, name, rating, cost)
    for nearest_place in nearest_places:
        dicc = {'from': '', 'to': '', 'visit': '',
                'rating': '', 'cost': ''}

        nearest_place_info = data[data['name'] == nearest_place]
        # print(f'[DEBUG] Nearest place info: {nearest_place_info}')
        duration = nearest_place_info['duration(hour)'].values[0]
        rating = nearest_place_info['rate'].values[0]
        cost = nearest_place_info[global_price].values[0]

        dicc['from'] = str(start_time)
        dicc['to'] = str(float(start_time) + float(duration))
        dicc['visit'] = nearest_place
        dicc['rating'] = str(rating)
        dicc['cost'] = str(cost)

        alternate_places.append(dicc)

    return alternate_places
