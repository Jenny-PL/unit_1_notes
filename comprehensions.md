# List, set, and dictonary comprehensions

## List comprehensions
Lists avoid the need to make an empty list, do a for loop, and append to the empty list.  Instead, it is all done in one line of code.

    verbs = ['work', 'eat', 'sleep']
    new_list = [element for element in verbs if 'a' in element]
    new_list = ['eat']

<mark>syntax: 
    created_list = [i for i in old_list if conditional] </mark> 

**original code:**

    rating_list = []
    for movie_dict in user_data["watched"]:
        rating_list.append(movie_dict["rating"])
**written as a comprehension**

    rating_list = [movie_dict["rating"]for movie_dict in user_data["watched"]]

**original code:**  

    genre_list = []
    for movie_dict in user_data["watched"]:
        genre_list.append(movie_dict["genre"])
**written as a comprehension**:

    genre_list = [movie_dict["genre"] for movie_dict in user_data["watched"]]

**original code:**

    list_of_recommendations = []
        for movie in movies_friends_watched:
            if movie['host'] in user_data['subscriptions']:
                list_of_recommendations.append(movie)

**written as a comprehension**:

    list_of_recommendations = [movie for movie in movies_friends_watched if movie['host'] in user_data['subscriptions']]

--
## Set comprehensions

new_set = {element **for** element **in** iterable (**if** conditional)}

## dictionary comprehensions

new_dictionary = {key:value **for**(key:value) **in** old_dict (**if** conditional)}


  