def main():

    # Create a dictionary to hold spacecraft details
    # Each key stores a piece of information about the spacecraft
    spacecraft = {
        "name": "Voyager 1",   # Name of spacecraft
        "distance": 163        # Distance in Astronomical Units (AU)
    }

    # Another spacecraft dictionary with only a name initially
    spacecraft1 = {
        "name": "james webb"   # Name of spacecraft
    }

    # Add more key-value pairs to spacecraft1 using dictionary update()
    # speed in km/s, orbit around solar system
    spacecraft1.update({"speed": 0.01, "orbit": "solar"})

    # Add a new key "distance" directly using assignment
    spacecraft1["distance"] = 0.01

    # Generate and print reports for both spacecraft
    print(report(spacecraft))
    print(report(spacecraft1))



# Function to generate a formatted spacecraft report
# spacecraft: dictionary containing spacecraft details
def report(spacecraft):
    return f"""
    ========= REPORT =========

    NAME = {spacecraft["name"]}
    DISTANCE = {spacecraft["distance"]} AU
    SPEED = {spacecraft.get("speed", "Unknown")} km/s
    ORBIT = {spacecraft.get("orbit", "Unknown")}

    ===========================
    """


# Run the program
main()
