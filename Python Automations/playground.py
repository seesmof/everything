from src.utils.misc import getClothing


weathers = [-3, 4, 6, 9, 12, 16, 30, "-3°C"]
for weather in weathers:
    clothes = getClothing(weather)
    print(f"{weather}: {clothes}")
