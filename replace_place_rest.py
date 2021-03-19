'''REST API for DUX Trip'''
import json
from flask import Flask, request
from replace_place import remove_place

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=['GET', 'POST'])

def home():
    '''Home page // only page'''
    response = {'trip': {}}    # Initiate respnse dict
    data = request.json
    print(f'[DEBUG] data: {data}')

    if request.method == 'POST':
        # Read items from POST request
        program = data['program']
        age = data['age']
        nationality = data['nationality']
        index_to_remove = data['index']

        if age == 'adult' and nationality == 'foreigner':
            global_price = 'foreigner'
        elif age == 'adult' and nationality == 'egyptian':
            global_price = 'egyptian and arab'
        elif age == 'student' and nationality == 'foreigner':
            global_price = 'egyptian and arab student'
        elif age == 'student' and nationality == 'foreigner':
            global_price = 'foreigner student'
        else:
            global_price = 'foreigner'


        # Get the response i.e. suggested programs
        response['trip'] = remove_place(global_price, program, index_to_remove)

        # Return the JSON objects
        return json.dumps(response, indent=4)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
