# Imports go below
import requests

# Variables go below
api_url = "https://api.covidtracking.com/v2/us/daily.json"

# Step 01 - Get the data
r = requests.get(api_url)

# Step 02 - Process the data
data = r.json() # Convert to JSON
data = data['data'] # Get the 'data key' only

# Create new dictionary for us to store our data in
new_data = {
    'deaths': [],
    'cases': [],
    'tests': []
}

# Loop over the entries in our data (loop over each day)
for entry in data:
    date = entry['date'] # get the date from the main dict bit

    # Add date to the 'tests', 'cases' and 'death' dicts
    entry['outcomes']['death']['total']['date'] = date
    entry['cases']['total']['date'] = date
    entry['testing']['total']['date'] = date

    # Add entries to 'tests', 'deaths' and 'cases'
    new_data['deaths'].append(entry['outcomes']['death']['total'])
    new_data['cases'].append(entry['cases']['total'])
    new_data['tests'].append(entry['testing']['total'])

# Step 02 - Tests
# print the length of each section to make sure there's data there
print(
    len(new_data['deaths']),
    len(new_data['cases']),
    len(new_data['tests']),
    "< if these aren't zero we're good"
    )
