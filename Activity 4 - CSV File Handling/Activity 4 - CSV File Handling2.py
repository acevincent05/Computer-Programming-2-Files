import csv

with open('census.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #storing the data of each state and it cities
    states = {}

    #going through the data of the csv file by putting it in a dictionary
    for row in csv_reader:
        each_state = row['STNAME']
        each_city = row['CTYNAME']
        state_pop = row['CENSUS2010POP']
        if each_state not in states:
            states[each_state] = {}
        
        states[each_state][each_city] = int(state_pop)

#finding the state with the highest number of cities
max_state_cities = max(states, key=lambda x: len(states[x]))
num_max_state_cities = len(states[max_state_cities])

#finding the state with the lowest number of cities
min_state_cities = min(states, key=lambda x: len(states[x]))
num_min_state_cities = len(states[min_state_cities])

#displays the number of cities per state
print('Number of cities per state:')
num = 1
for state in states:
    print(f'{num}. {state} - {len(states[state])}')
    num += 1

#displays the state with highest number of cities
print()
print(f'State with the highest number of cities:')
print(f'{max_state_cities} - {num_max_state_cities}')

#displays the state with lowest number of cities
print()
print(f'State with the lowest number of cities:')
print(f'{min_state_cities} - {num_min_state_cities}')

#population of each cities in every state
for state, cities in states.items():  
    num = 1
    print()
    print(f"State of {state}:")  
    for city, population in cities.items():
        print(f"{num}. {city} - {population}")
        num += 1

#storing the least and most populated cities
most_populated_cities = {}
least_populated_cities = {}

#finding the most populated cities
for state, cities in states.items():
    most_populated_city = max(cities, key=lambda city: cities[city]) 
    most_populated_cities[state] = (most_populated_city, cities[most_populated_city])

#displays most populated city per state
print()
print(f'Most populated city per state:')
num = 1
for state, (city, population) in most_populated_cities.items():
    print(f"{num}. {state}: {city} - {population}")
    num += 1

#finding the least populated cities
for state, cities in states.items():
    least_populated_city = min(cities, key=lambda city: cities[city]) 
    least_populated_cities[state] = (least_populated_city, cities[least_populated_city])

#displays least populated city per state
print()
print(f'Least populated city per state:')
num = 1
for state, (city, population) in least_populated_cities.items():
    print(f"{num}. {state}: {city} - {population}")
    num += 1
