
def config(argSection):
    import configparser
    import json
    config = configparser.ConfigParser()
    config.read('config.ini')
    dict1 = {}
    options = config.options(argSection)
    for option in options:
        try:
            if option == "subreddits" or option == "colors":
                dict1[option] = json.loads(config.get(argSection, option))
            else:
                dict1[option] = config.get(argSection, option)
        except:
            print("exception with config file: on %s!" % option)
            dict1[option] = None
    return dict1
