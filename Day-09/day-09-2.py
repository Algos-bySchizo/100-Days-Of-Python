""" Nesting Dictionaries and Lists """
capitals={
    "France":"Paris",
    "Germany":"Berlin"
}
""" Nesting list in dictionary """
travel_log={
    "France":['Paris','Lille','Dijon'],
    "Germany":['Berlin','Hamburg','Stuttgart']
}
print(travel_log["France"])
""" Nesting dictonary in a dictionary """
travel_log={
    "France":{"cities_visited":['Paris','Lille','Dijon'],"total_visits":12},
    "Germany":{"cities_visited":['Berlin','Hamburg','Stuttgart'],"total_visits":5}
}
""" Nesting dictonary in a List """
travel_log={
    {
        "country":"France",
        "cities_visited":['Paris','Lille','Dijon'],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":['Berlin','Hamburg','Stuttgart'],
        "total_visits":5
    }
}