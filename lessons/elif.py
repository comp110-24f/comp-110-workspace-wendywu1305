def get_weather_report() -> str:
    """display weather instruction"""
    weather: str = input("What is the weather? ")
    # ask the user "What is the weather? " as input and save as local variable
    if weather == "rainy" or weather == "cold":
        # need to write "weather =" on both sides to be boolean True or False
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
