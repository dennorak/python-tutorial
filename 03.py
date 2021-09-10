# Imports go below
import requests
import matplotlib.pyplot as plt # New in step 03

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

# Step 03 - Display the data
day = 0

# Points for the x-axes
points_days = []

# Points for the Y-axes
points_cases = []
points_deaths = []
points_tests = []

# iterate over items
for day in range(0, len(new_data['cases']) - 1):
    points_days.append(day)
    points_cases.insert(0, new_data['cases'][day]['value'])
    points_deaths.insert(0, new_data['deaths'][day]['value'])
    points_tests.insert(0, new_data['tests'][day]['value'])
    day += 1 # increment the day counter

plt.plot(points_days, points_cases, label="cases") # plot the points
plt.plot(points_days, points_deaths, label="deaths") # plot the points
plt.plot(points_days, points_tests, label="tests") # plot the points

plt.legend() # this line displays the legend on the graph

plt.xlabel('day') # set x-axis label
plt.ylabel('quantity') # set y-axis label

# set title - using '{}' and .format()
plt.title('cases per day since {}'.format(new_data['cases'][0]['date']))

# show the graph
plt.show()
