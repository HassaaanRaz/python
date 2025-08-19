# Example program: calculate running pace (minutes per mile)

def main():
    # Call get_pace() with total miles = 26.2 (a marathon distance) and minutes = 33
    # This means: "If I run 26.2 miles in 33 minutes, what's my pace per mile?"
    pace = get_pace(miles=26.2, minutes=33)

    # round(pace, 2) → round result to 2 decimal places
    # Example: 1.259... → 1.26
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    # Defensive programming: check if minutes is a valid value (> 0)
    if not minutes > 0:
        # If invalid (minutes <= 0), stop execution and raise an error
        raise ValueError("INVALID VALUE")
    
    # Otherwise, calculate and return the pace:
    # minutes per mile = total minutes ÷ total miles
    return minutes / miles


# Program entry point (runs only if the script is executed directly)
if __name__ == "__main__":
    main()
