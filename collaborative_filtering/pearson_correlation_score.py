# from recommendations import critics
from math import sqrt

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # Find the number of elements
    n = len(si)

    # If nothing is found in common, return 0
    if n == 0:
        return 0

    # Add up all of the preferences
    sum1 = sum([prefs[p1][mut_rated] for mut_rated in si])
    sum2 = sum([prefs[p2][mut_rated] for mut_rated in si])

    # Sum up the squares
    square_sum1 = sum([pow(prefs[p1][mut_rated], 2) for mut_rated in si])
    square_sum2 = sum([pow(prefs[p2][mut_rated], 2) for mut_rated in si])

    # Sum up the products
    product_sum = sum([prefs[p1][mut_rated] * prefs[p2][mut_rated]
                        for mut_rated in si])

    # Calculate Pearson score
    # Pretty discrete, but it works.
    numerator = product_sum - (sum1 * sum2 / n)
    denominator = sqrt((square_sum1 - pow(sum1, 2) / n) * (square_sum2 - pow(sum2, 2) / n))
    if denominator == 0:
        return 0

    r = numerator / denominator

    return r

# print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
