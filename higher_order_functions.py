SCORES = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 } 

def score_word(word):
    total = 0
    word = word.upper()
    for letter in word:
        total += SCORES[letter]

    return total

def get_max_with_ties_for_score(data):
    best = []
    best_score = None
    for item in data:
        score = score_word(item)
        if best_score is None or score > best_score:
            best = [item]
            best_score = score
        elif score == best_score:
            best.append(item)
    return best

def get_max_with_ties_for_len(data):
    best = []
    best_score = None
    for item in data:
        score = len(item)
        if best_score is None or score > best_score:
            best = [item]
            best_score = score
        elif score == best_score:
            best.append(item)
    return best

# scorer is a parameter that refers to a function that will be passed
def get_max_with_ties(data, scorer): 
    best = []
    best_score = None
    for item in data:
        score = scorer(item)
        if best_score is None or score > best_score:
            best = [item]
            best_score = score
        elif score == best_score:
            best.append(item)
    return best

restaurants = [
    {"name": "Grillby's", "rating": 1},
    {"name": "Crow's Nest", "rating": 5},
    {"name": "Spicy City", "rating": 5},
    {"name": "Applebee's", "rating": 3}
]

def get_rating(restaurant):
    return restaurant["rating"]

# Here, get_max_with_ties is being called using restaurants as the 'data' parameter
# and get_rating as the 'scorer' paramemter (a function)
print(get_max_with_ties(restaurants, get_rating))

# to do the same thing, however using a lmabda function rather than named function:
print(get_max_with_ties(restaurants, lambda r: r["rating"]))



# Further examples, here using 'words' as the data, and score_word() as the scorer function,
# then len() as the scorer function
words = ["hello", "za", "today", "qi"]
print(get_max_with_ties(words, score_word))
print(get_max_with_ties(words, len))