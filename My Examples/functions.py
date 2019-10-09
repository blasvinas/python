def make_shirt(message, size="large"):
    """ Accepts the size and message that should be printed on the t-shirt """
    print("You got a {} t-shirt with the message {}".format(size, message))


def city_country(city, country="USA"):
    """ Returns City, Country """
    return city + ", " + country


def make_great_magicians(magicians):
    """ Takes a list and return a modified list """
    great = []
    for magician in magicians:
        great.append("Great " + magician)

    return great


def make_pizza(*toppings):
    """ Take a variable number of topings """
    print("You pizza has the following toppins:")
    for toping in toppings:
        print("-" + toping)


def create_user_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

