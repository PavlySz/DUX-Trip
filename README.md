# **DUX Trip**

This is an algorithm for DUX trip.


### **Steps**

 - Run the server for suggesting programs
```Python
python3 flask_rest_api.py
```

 - Run the CURL command and send in the parameters specified above
```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"budget":200, "time": 3, "lat":30.050053, "lng":31.235964, "start_time":9, "age":"adult", "nationality":"egyptian"}' http://localhost:5000/
```
Where:

- `lng` is the longitude of the starting place (str)
- `lat` is the latitude of the starting place (str)
- `time` total time available for the user (int)
- `budget` total budget available for the user (int)
- `start_time` start time that the user specifies (int)
    - ***Note*** if `start_time` is less that `9` it will be automatically
      converted to 9, since all museums start working at 9:00 AM
- `age` age of the user (string)
    - 'student' or 'adult'
- `nationality` nationality the user (string)
    - 'egyptian' or 'foreigner'


### **Output**
```
{
  "trip": [
    {
      "program": [
        {
          "From": "9",
          "To": "13.0",
          "you will visit": "The Museum of Egyptian Antiquities",
          "rating of this place is ": "4.5",
          "The cost is ": "30"
        }
      ],
      "totalhours": 4.0,
      "totalmoney": 30.0
    },
    {
      "program": [
        {
          "From": "9",
          "To": "13.0",
          "you will visit": "The Museum of Egyptian Antiquities",
          "rating of this place is ": "4.5",
          "The cost is ": "30"
        }
      ],
      "totalhours": 4.0,
      "totalmoney": 30.0
    },
    {
      "program": [
        {
          "From": "9",
          "To": "13.0",
          "you will visit": "The Museum of Egyptian Antiquities",
          "rating of this place is ": "4.5",
          "The cost is ": "30"
        }
      ],
      "totalhours": 4.0,
      "totalmoney": 30.0
    },
    {
      "program": [
        {
          "From": "9",
          "To": "13.0",
          "you will visit": "The Museum of Egyptian Antiquities",
          "rating of this place is ": "4.5",
          "The cost is ": "30"
        }
      ],
      "totalhours": 4.0,
      "totalmoney": 30.0
    }
  ]
}
```

***

### Run the server for replacing a place
```Python
python3 replace_place_rest.py
```

 - Run the CURL command and send in the parameters specified above
```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"program":{program here}, "index": 3,"age":"adult", "nationality":"egyptian"}' http://localhost:8000/
```
Where:

- `program` suggested program that the user had chosen (JSON)
- `index` index of place to be replaced place (int)
- `age` age of the user (string)
    - 'student' or 'adult'
- `nationality` nationality the user (string)
    - 'egyptian' or 'foreigner'

### **Note**
To install libraries, run the following command:
```Python
pip install -r requirements.txt
```
