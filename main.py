# Exercise1
def distance_from_zero(x):
    if type(x) == float or type(x) == int:
        return abs(x)
    else:
        return "Nope"


y = -5.6
z = "what?"
print(distance_from_zero(y))
print(distance_from_zero(z))


# Exercise2
def is_leap(x):  # x argument represents year
    leap = False
    # Makes sure entry is valid and asks until valid entry is given
    while (10 ** 5) < x or x < 1900:
        x = int(input("Invalid entry. Try again(1900 - 10^5): "))
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        leap = True
    return leap


try:
    year = int(input("Enter year to be evaluated: "))
    print(is_leap(year))
except ValueError:
    print("Not a number")
