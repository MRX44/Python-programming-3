#dialogue 1
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    print(tastedive_response.url)
    return tastedive_response.json()




#dialogue 2
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    #print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(l):
        li.append(dic['Results'][i]['Name'])
    return li



#dialogue 3
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    #print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(5):
        li.append(dic['Results'][i]['Name'])
    return li

def get_related_titles(movie_lis):
    li=[]
    for movie in movie_lis:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))




#dialogue 4
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
import json


def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)


#dialogue 5
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))
import requests_with_caching
import json


def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)

def get_movie_rating(dic):
    rating = dic['Ratings']
    for item in rating:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0




#dialogue 6
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
import requests_with_caching
import json
def get_movies_from_tastedive(string):
    base_url="https://tastedive.com/api/similar"
    params_diction = {}
    params_diction['q']=string
    params_diction['type']='movies'
    params_diction['limit']=5
    tastedive_response = requests_with_caching.get(base_url, params = params_diction)
    #print(tastedive_response.url)
    return tastedive_response.json()

def extract_movie_titles(result):
    dic=result['Similar']
    l=len(dic['Results'])
    li=[]
    for i in range(5):
        li.append(dic['Results'][i]['Name'])
    return li

def get_related_titles(movie_lis):
    li=[]
    for movie in movie_lis:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))

def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = title
    params_diction['r'] = 'json'
    this_page_cache = requests_with_caching.get(base_url, params=params_diction)

    return json.loads(this_page_cache.text)

def get_movie_rating(dic):
    rating = dic['Ratings']
    for item in rating:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0
   

def get_sorted_recommendations(listt):
    n_list = get_related_titles(listt)
    n_dict = {}
    for i in n_list:
        rating = get_movie_rating(get_movie_data(i))
        n_dict[i] = rating
    print(n_dict)
    print(sorted(n_dict, reverse=True))
    return [i[0] for i in sorted(n_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

