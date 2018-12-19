from recommendations import critics
from math import sqrt

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # get the list of shared_items
    si = {}
    # for every movie person1 rated, if person2
    # also rated it, add to si
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if no common ratings, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in si])

    return 1 / (1 + sqrt(sum_of_squares))

print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
