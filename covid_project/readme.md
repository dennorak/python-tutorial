# COVID-19 Python Project
## Introduction
This project is an easy way to get yourself coding in python! During this project, you will learn how to use the `requests` library to poll a server for data, as well as the `matplotlib` library to display the data gathered.

### Steps
- Request the data from the server
- Process the data (clean it up)
- Display the data

Along the way, we're going to run tests to make sure our code runs smoothly. These tests can be left in if you'd like, but for our purposes I'm going to assume they're removed after each step.

## Step 01 - Get the Data
To begin, let's create a new python file. This can be called whatever you want, but make sure it ends in `.py`. To start off, let's import the `requests` library we mentioned a bit ago.

```python
import requests
```

In order for us to get data to display, we need to have somewhere to get the data from. In our case, it will be a JSON file from [this website](covidtracking.com). Let's create a new variable to store our API link in.

```python
api_url = "https://api.covidtracking.com/v2/us/daily.json"
```

Next, we'll use `requests` to actually ask the server for the data, passing in the link we just set. We'll call this <b>r</b> for <b>response</b>.

```python
r = requests.get(api_url)
```
### Tests
Now that we have our data, we should check to make sure that everything went okay! When we made the request to the server, it returned the data that we asked for as well as a status code. There are lots of status codes that mean lots of different things, but the one we'll be looking for is the 200 code. If the status code is 200, that means everything went okay and we should have our data. We can also use python to determine the length of the data that we received. As long as that length isn't zero, we should have some data.

```python
print(r.status_code, "< if it's not 200 there's a problem")
print( len(r.text), "< as long as this isn't zero we got data" )
```

As long as those lines run correctly, we should have our data!

## Step 02 - Process the data
With our response in hand, it's time to sort through it! We'll start by storing the data in a new variable we'll call `data`. To do this, we need to convert the response data from JSON to a python dictionary.

```python
data = r.json()
```

> If you don't understand why we're processing the data instead of just displaying it, you can view the raw data using `print(data)` at this point. It's a mess, and it's better if we clean it up first.

The data we receive has a bunch of excess in it that we should remove. Right now in `data`, there are three keys (`links`, `meta`, `data`) from which we need one. To remove the others, we'll set `data` equal to the key that we want from itself

```python
data = data['data']
```

Now that `data` only has what we want in it, it's time to sort out the data itself. Let's start by creating a new variable `new_data`, and add some empty lists to store our data in. Our data is sorted by day, but we want to display trend lines. Each day has entries for `deaths`, `cases`, and `tests`, so we'll create lists for each of the three.

> Again, you can `print(data)` if you're unsure why we're doing this.

```python
new_data = { 'deaths': [], 'cases': [], 'tests': [] }
```

Now that we have somewhere to put our data, let's start going through it! this part might get a bit tricky as we need a for loop (and I'm trying to put it in markdown), so if you get lost remember to check the python files for reference.
```python
for entry in data:
```
### the `for` loop:
Inside the loop, we're iterating over each item. let's start by getting the date:

```python
    date = entry['date']
```

Because the date is part of the day's item and not it's `deaths`, `cases`, and `tests` items, we'll add it to them.

```python
    entry['outcomes']['death']['total']['date'] = date
    entry['cases']['total']['date'] = date
    entry['testing']['total']['date'] = date
```

Finally, let's append the formatted data from the entry to our `new_data` dict.

```python
    new_data['deaths'].append(entry['outcomes']['death']['total'])
    new_data['cases'].append(entry['cases']['total'])
    new_data['tests'].append(entry['testing']['total'])
```

> If you're unsure why we're routing through the dictionary the way we are, `print(entry)` inside the for loop will display each item we're looping through so you can see the structure of the data firsthand.

### end `for` loop (and tests)
Now that we've gotten all of our data formatted, it's time to test what we've done! We can do this by printing the length of the items in new_data, and as long as they aren't zero we should have our data!

```python
print(
    len(new_data['deaths']),
    len(new_data['cases']),
    len(new_data['tests']),
    "< if these aren't zero we're good"
    )
```

## Step 03 - Display the data
Now that everything's looking good on the backend, let's display what we've collected! To do this, we'll need to import `pyplot` from `matplotlib` (put this import at the top with the requests import).

```python
import matplotlib.pyplot as plt
```
Back down to after our `for` loop from the last step, we need to create a few new variables. We need lists for our points and a counter for our days passed.

```python
day = 0
points_days = []
points_cases = []
points_deaths = []
points_tests = []
```

Now that we have somewhere to store our points, let's iterate over our data to get our points! We'll do this with another `for` loop. We need to iterate over the length of our data - 1, because while `len()` returns the actual length of our lists the lists start at zero.

> In our `for` loop, we're using `new_data['cases']` to get our length. Any of our stats could be used though, as they're all the same length.

```python
for day in range(0, len(new_data['cases']) - 1):
```

### the `for` loop:
For each item, we want to add a point with the current day to our `points_days` list and we want ot add our data to their respective lists. Afterwards, we want to increment our `day` counter and move on to the next element!

```python
    points_days.append(day)
    points_cases.insert(0, new_data['cases'][day]['value'])
    points_deaths.insert(0, new_data['deaths'][day]['value'])
    points_tests.insert(0, new_data['tests'][day]['value'])
    day += 1
```

### end `for` loop
Now that we've gotten our points, let's plot them! We can do this using `plt.plot()`, where the args are `(x_value, y_value, label)` (label is optional but we want to know which data is which). Let's do this for each of our three lines.

```python
plt.plot(points_days, points_cases, label="cases")
plt.plot(points_days, points_deaths, label="deaths")
plt.plot(points_days, points_tests, label="tests")
```

Now we'll just do some things to make our graph look nicer, such as adding a legend, title, and axes labels.

```python
plt.legend()
plt.xlabel('day')
plt.ylabel('quantity')
plt.title('cases per day since {}'.format(new_data['cases'][-1]['date']))
```

Now that our data and labels are in place, let's see what we've done!

```python
plt.show()
```

> To quit, press `CTRL + C` on the terminal or press `q` on the graph.

And that's that! We've successfully retrieved data from a server, formatted that data, and displayed it! Congratulations!

## Final Notes
While this project is a good intro to python and python data manipulation, there's a ton more out there to learn. Now that you have a basic idea of how to go about a python project like this, get out there and make your own! Find something that interests you and see what you can do with it, as (in my opinion) experience is the best teacher.
