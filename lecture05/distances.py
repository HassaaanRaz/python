# Dictionary storing spacecraft names as keys
# and their distances as values (some raw numbers, some with "AU")
distances = {
    "Voyager 1": "163",        # stored as string, numeric
    "Voyager 2": "134",        # stored as string, numeric
    "Pioneer 10": "80 AU",     # string with "AU" inside
    "New Horizosn": "58",      # typo in "Horizons"
    "Pioneer 11": "44 AU"      # string with "AU" inside
}


def main():
    # Ask the user to enter a spacecraft name
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        # Try to fetch distance and convert it to float
        # This works if value is plain number (e.g., "163")
        au = float(distances[spacecraft])
    except ValueError:
        # Raised if value contains non-numeric characters ("80 AU")
        print("can't convert distance to float")
        return
    except KeyError:
        # Raised if user entered a spacecraft not in the dictionary
        print("Value not present")
        return

    # Convert AU to meters
    m = convert(au)

    # Print the distance in meters
    print(f"{m} m away")


def convert(au):
    # Conversion factor: 1 Astronomical Unit (AU) = 149,597,870,700 meters
    return au * 149597870700


# Run only if executed directly
if __name__ == "__main__":
    main()
