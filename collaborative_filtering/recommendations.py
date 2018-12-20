from euclidean_distance_score import sim_distance
from pearson_correlation_score import sim_pearson
# from math import sqrt

# A dictionary of movie critics and their ratings of a  small
# set of movies

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me, and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on  plane': 3.5,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me, and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me, and Dupree': 3.5},
'Toby': {'Snakes on a Plane': 4.5, 'You, Me, and Dupree': 1.0, 'Superman Returns': 4.0}}

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity functional are optional params,
# where n is number of results and similarity is the scoring algorithm.
def top_matches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other)
                        for other in prefs if other != person]

    # Sort the list so highest scores are on top
    scores.sort()
    scores.reverse()
    return scores[0:n]

print(top_matches(critics, 'Toby', n = 6))
