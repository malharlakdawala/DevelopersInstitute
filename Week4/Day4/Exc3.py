import random


def get_random_temp():
    return random.randint(-10,40)

def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature<0:print("Brrr, that’s freezing! Wear some extra layers today")
    else:print("Pleasant weather")

