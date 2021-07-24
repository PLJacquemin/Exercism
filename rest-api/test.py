import json

input_json = """
[
    {
        "type": "1",
        "name": "name 1"
    },
    {
        "type": "2",
        "name": "name 2"
    },
    {
        "type": "1",
        "name": "name 3"
    }
]"""

# Transform json input to python objects
input_dict = json.loads(input_json)

# Filter python objects with list comprehensions
output_dict = [x for x in input_dict if x['name'] == 'name 2']

# Transform python object back into json
output_json = json.dumps(output_dict)

# Show json
print output_json
