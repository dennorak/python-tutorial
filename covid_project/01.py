# Imports go below
import requests

# Variables go below
api_url = "https://api.covidtracking.com/v2/us/daily.json"

# Step 01 - Get the data
r = requests.get(api_url)

# Step 01 - Tests
print(r.status_code, "< if it's not 200 there's a problem") # Check response
print( len(r.text), "< as long as this isn't zero we got data" ) # Check data
