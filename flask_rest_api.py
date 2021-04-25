'''REST API for DUX Trip'''
import json
from flask import Flask, request
from trip_main import find_population
from replace_place import replace_place

# TODO: Unit testing for budget and time
# TODO: Exception handling
# TODO: Load testing
# TODO: Look for other algorithms
# TODO:
    # Get traffic time and save it in columns
    # Traffic at day and time => columns

app = Flask(__name__, template_folder="templates")

@app.route("/trip/recommendPlaces", methods=['GET', 'POST'])
def recommend_places():
    '''Recommend places'''
    response = {'trip': {}}    # Initiate respnse dict
    data = request.json

    print(f'[DEBUG] data: {data}')
    if request.method == 'POST':
        # Read items from POST request
        start_time = int(data['startTime'])
        budget = int(data['budget'])    # Test large budget
        time = int(data['time'])        # Test large time
        lat = float(data['lat'])
        lng = float(data['lng'])
        age = data['age'].lower()
        nationality = data['nationality'].lower()
        museum_type = data['museumType'].lower()

        valid_museum_types = ['modern age', 'pharaonic',\
            'science', 'art', 'islamic', 'coptic', 'all']

        if museum_type not in valid_museum_types:
            return json.dumps({"ERROR": "Invalid museum type",
                               "Valid museum types": f"{valid_museum_types}"})

        # Get the response i.e. suggested programs
        response['trip'] = find_population(lat, lng, start_time, time, budget, \
            age, nationality, museum_type)

        # Return the JSON objects
        return json.dumps(response, indent=4)


@app.route("/trip/replacePlace", methods=['GET', 'POST'])
def replace_places():
    '''Replace a place'''
    response = {'alternativePlaces': {}}    # Initiate respnse dict
    data = request.json
    # print(f'[DEBUG] data: {data}')

    if request.method == 'POST':
        # Read items from POST request
        program = data['fullProgram']['program']
        index_to_remove = data['index']
        age = data['age'].lower()
        nationality = data['nationality'].lower()
        museum_type = data['museumType'].lower()

        valid_museum_types = ['modern age', 'pharaonic',\
            'science', 'art', 'islamic', 'coptic', 'all']
        if museum_type not in valid_museum_types:
            return json.dumps({"ERROR": "Invalid museum type",
                               "Valid museum types": f"{valid_museum_types}"})

        # Get the response i.e. suggested programs
        response['alternativePlaces'] = replace_place(program,\
            age, nationality, index_to_remove, museum_type)

        valid_museum_types = ['modern age', 'pharaonic', 'science', 'art', 'islamic', 'coptic']
        if museum_type.lower() not in valid_museum_types:
            return json.dumps({"ERROR": "Invalid museum type",
                               "Valid museum types": f"{valid_museum_types}"})

        # Return the JSON objects
        return json.dumps(response, indent=4)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
