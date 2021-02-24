'''REST API for DUX Trip'''
import json
from trip_main import find_population
from flask import Flask, request

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=['GET', 'POST'])

def home():
    '''Home page // only page'''
    response = {'trip': {}}    # Initiate respnse dict
    data = request.json
    print(f'[DEBUG] data: {data}')

    if request.method == 'POST':
        # Read items from POST request
        start_time = int(data['start_time'])
        budget = int(data['budget'])
        time = int(data['time'])
        lat = float(data['lat'])
        lng = float(data['lng'])

        # Get the response i.e. suggested programs
        response['trip'] = find_population(lat, lng, start_time, time, budget)

        # Return the JSON objects
        return json.dumps(response, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
