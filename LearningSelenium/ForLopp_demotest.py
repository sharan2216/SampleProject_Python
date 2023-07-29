# STRING :-----------------
city = 'Delhi'
for i in city:
    print(i)
print("------------------------")
# LIST :-----------------
city = ["Delhi", "Melbourne", "Lucknow", "Sydney"]
for i in city:
    print(i)
print("------------------------")

# Tuple :-----------------
city = ("Delhi", "Melbourne", "Lucknow", "Sydney")
for i in city:
    print(i)
print("------------------------")

# Access list within list
# IN List : String with 2 values(country and city) :-----------------
cities = (["India", "Delhi"], ["Australia", "Melbourne"], ["Canada", "Vancouver"], ["USA", "New York"])
for country, city in cities:
    print("The country is " + country + " and city is " + city)
print("------------------------")

# IN SET : String with 2 values(country and city) :-----------------
cities = {"Ney York", "Delhi"}
for city in cities:
    print(city)
print("------------------------")

# IN Dictionary : String with 2 values(country and city) :-----------------
cities = (["India", "Delhi"], ["Australia", "Melbourne"], ["Canada", "Vancouver"], ["USA", "New York"])
my_dict = dict(cities)
for country,city in my_dict.items():
    print(country , city)
print("------------------------")

