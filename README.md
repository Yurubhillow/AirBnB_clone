Hbnb logo

Hbnb
An AirBnB clone CLI.

AirBnB Clone 
This project emulates a simplified AirBnB system for managing lodging listings.

File Structure 
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── file_storage.py

Models 
BaseModel
id (string)
created_at (datetime)
updated_at (datetime)
Contains methods to initialize, save, convert to a dictionary, and format string.

User 
Extends BaseModel with:

email (string)
password (string)
first_name (string)
last_name (string)
Place 
Extends BaseModel with:

city_id (string)
user_id (string)
name (string)
description (string)
number_rooms (int)
number_bathrooms (int)
max_guest (int)
price_by_night (int)
latitude (float)
longitude (float)
amenity_ids (list of strings)
Review 
Extends BaseModel with:

place_id (string)
user_id (string)
text (string)
City 
Extends BaseModel with:

state_id (string)
name (string)
Amenity 
Extends BaseModel with:

name (string)
State 
Extends BaseModel with:

name (string)
Storage 
FileStorage
  |
  | serializes 
  v
objects dict
  |
  | saved to
  v
file.json
  |
  | reloaded from
  v
objects dict 
Uses JSON serialization to file for persistent storage.

File Storage
Serializes and deserializes data to file with methods to:

Get all objects
Create new object
Save to file
Reload from file
Usage 
Run Console
$ ./console.py
Console Commands
The console supports the following commands and their uses:

EOF: Exit the console.
all [CLASS_NAME]: Display all instances of the specified class or all classes.
create [CLASS_NAME]: Create a new instance of the specified class.
destroy [CLASS_NAME] [INSTANCE_ID]: Delete an instance based on the class name and ID.
help [COMMAND]: Show documentation for the specified command.
quit: Exit the console.
show [CLASS_NAME] [INSTANCE_ID]: Display details of an instance based on class name and ID.
update [CLASS_NAME] [INSTANCE_ID] [ATTR_NAME] [ATTR_VAL]: Update an instance's attribute based on class name, ID, attribute name, and new value.
To get help on any specific command, type help [COMMAND].

Tests 
Unit tests for the project are defined in the tests folder. The test cases cover models and the console functionalities.

Models and Console Tests
The tests folder contains test cases for each model class and the console:

tests
├── test_models
│   ├── test_amenity.py
│   ├── test_city.py
│   ├── test_place.py
│   ├── test_review.py
│   ├── test_state.py
│   └── test_user.py
└── test_console.py

These tests ensure proper model initialization, methods, and attributes. Additionally, test_console.py utilizes the unittest module to test console functions.

To run all tests:

$ python3 -m unittest discover tests
This command executes all test files to validate the functionality of your AirBnB Clone.

If you need more details or have specific test scenarios in mind, feel free to let us know!
