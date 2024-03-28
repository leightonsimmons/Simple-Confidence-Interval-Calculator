import math

# Creating Variables / Asking For Numbers
plus = 0
minus = 0
median = float(input('Median: '))
upper = float(input('Upper Quartile: '))
lower = float(input('Lower Quartile: '))
n = float(input('Sample Size: '))
decimal = input('Round To Decimal Place? Y/N: ')
dcm_place = 0
n_sqrt = math.sqrt(n)

# If User Wishes To Round The Number Then Ask What To Round It To
if decimal == 'Y':
    dcm_place = int(input('Decimal Place To Round To: '))

# Do The Calculations
def calc():
    plus = median + 1.5 * ((upper - lower) / n_sqrt)
    minus = median - 1.5 * ((upper - lower) / n_sqrt)
    # If User Wanted It Rounded Then Print Rounded
    if decimal == 'Y':
        print(round(plus, dcm_place))
        print(round(minus, dcm_place))
    # Else Do Not Round
    else:
        print(plus)
        print(minus)

# Call The Function
calc()