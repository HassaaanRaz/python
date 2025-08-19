distances = {
    "voyager1": 163,
    "Voyager2": 162,
    "james webb": 0.01,
    "Hubble": 0.01
}

def main():

    for name in distances.keys():
        print(f"{name} is {distances[name]} AU away from the sun")
        print()

    for distance in distances.values():
        print(f" {distance} AU is {cvt(distance)} km")
        print()


def cvt(au):
    return au * 149597870.7  # Convert AU to kilometers
main()