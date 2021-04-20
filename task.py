# Calculates cost of hotel stay
def hotel_cost(nights):
    return 140 * nights


# Returns round trip cost for valid city entry
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


# Calculates car rental cost and discount based on number of days
def rental_car_cost(days):
    if days >= 3:
        if days >= 7:
            return days * 40 - 50
        else:
            return days * 40 - 20
    else:
        return days * 40


# Calculates total cost including spending money
def trip_cost(city, days, spending_money):
    x = rental_car_cost(days)
    y = hotel_cost(days)
    z = plane_ride_cost(city)
    return x + y + z + spending_money


# if wrong city inserted or spelled incorrectly, allows for attempts until valid entry is obtained
cit = input("What city are you travelling to?(Cape Town, Durban, JHB, BFN): ")
while (cit != "Cape Town") and (cit != "Durban") and (cit != "JHB") and (cit != "BFN"):
    cit = input("Make sure you enter valid city or inputted the city as indicated in brackets(Cape Town, Durban, "
                "JHB, BFN. Try again: ")

# If incorrect type inserted, returns error message
try:
    night = int(input("How many nights will you be staying? "))
    day = int(input("How much days for car rental? "))
    spend = int(input("What is your spending money?"))

except ValueError:
    print("Invalid entry: Not a number")

print("")
print("Round trip to", cit, "cost: R", plane_ride_cost(cit))
print("Hotel cost: R", hotel_cost(night))
print("Car rental cost: R", rental_car_cost(day))
print("Total cost (including spending money): R", trip_cost(cit, day, spend))
