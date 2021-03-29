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
```json
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

### Example
#### **Command**
```shell
curl -i -H "Content-Type: application/json" -X POST -d '{"full_program": {"program": [{"from": "9", "to": "10.5", "visit": "The Museum of Egyptian Antiquities", "rating": "4.5", "cost": "0.66"}, {"from": "10.5", "to": "12.0", "visit": "Aisha Fahmi Palace", "rating": "5.0", "cost": "0.66"}, {"from": "12.0", "to": "13.0", "visit": "Museum of Islamic Ceramics", "rating": "3.0", "cost": "0.66"}, {"from": "13.0", "to": "14.25", "visit": "Cairo Tower", "rating": "4.0", "cost": "0.66"}, {"from": "14.25", "to": "14.7", "visit": "House of the People Beit El-Umma Museum", "rating": "4.5", "cost": "0.66"}, {"from": "14.7", "to": "16.7", "visit": "Abdeen Palace Museum", "rating": "4.0", "cost": "0.66"}, {"from": "16.7", "to": "17.7", "visit": "National Geographic Society Museum", "rating": "4.5", "cost": "0.66"}], "totalHours": 8.7, "totalMoney": 4.62}, "nationality": "egyptian", "age": "adult", "index": 3}' http://localhost:8000/
```


#### **Output**
```json
{
    "alternativePlaces": [
        {
            "from": "13.0",
            "to": "13.45",
            "visit": "Sami Amin",
            "rating": "3.0",
            "cost": "1.33"
        },
        {
            "from": "13.0",
            "to": "14.0",
            "visit": "Manial Palace Museum",
            "rating": "4.5",
            "cost": "1.33"
        },
        {
            "from": "13.0",
            "to": "14.0",
            "visit": "German Evangelical Church",
            "rating": "4.0",
            "cost": "0.0"
        }
    ]
}
```

### **Note**
To install libraries, run the following command:
```Python
pip install -r requirements.txt
```
