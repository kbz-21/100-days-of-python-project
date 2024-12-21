dictionary = {"kal": "He is Adama science and technology student"}
print(dictionary['kal'])

# adding new element in to dictionary
dictionary["loop"]="the action of something again and again."
print(dictionary)

# creating empty dictionary
dictionary={}
# wipe and existing dictionary
dictionary = {}

# edit an item dictionary
dictionary["kal"] = "at 2022 last he will gratuate." 
print(dictionary)

dictionary_dict = {"kal":"Astu", "Medi":"Selale", "Beka":"ArbaMinch"}

for key in dictionary_dict:
    print(key)
    print(dictionary_dict[key])


# .........................................................
# nesting dictionary in a dictionary

travel_countries = {

    "Ethiopia": {"cities_visited":["addis ababa", "bahid dar", "Adama", "Hawassa"],"Total_visits":67}
}

print(travel_countries)

# Nesting dictionary in to list

travel_countries = [

    {"country": "Ethiopia",
     "cities_visited":["addis ababa", "Gondar", "Bahir dar"] ,
     "Total_visits":3
    },

    {"country": "Russia", 
     "cities_visited":["addis ababa", "Gondar", "Bahir dar"] , 
     "Total_visits":3,
    }
    
]

# ..........................................................
# exersice 
travel_log = [
{
    "country":"france",
    "visit":12,
    "cities": ["paris","lille", "dijon"]
},
{
    "country":"german",
    "visit":5,
    "cities": ["berlin","humberg", "Stutgart"]
}
               
]

def add_new_country(country, visit, cities):
    dic ={}

    dic["country"]= country
    dic["visit"]= visit
    dic["cities"]= cities
    travel_log.append(dic)
add_new_country("Ethiopia", 65, ["berlin","humberg", "Stutgart"])
print(travel_log)