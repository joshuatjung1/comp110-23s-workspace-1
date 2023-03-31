"""If it's raining, tell me to pack an umbrella"""

weather: str = input("What is the weather like? ")

if (weather =="rain"):
    print("Pack an umbrella!")
    print("But Splash in the Puddles!")
else:
    if weather == "snow":
        print("Pack a Jacket!")
    else:
         print("You don't need an umbrella")
print("Have a lovely day!")
