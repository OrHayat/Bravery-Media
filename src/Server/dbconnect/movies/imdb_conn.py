import json
import requests
import Server.dbconnect.movies.config as config


class MovieResult:
    def __init__(self, id, title, type, image, plot):
        self.id = id
        self.title = title
        self.type = type
        self.image = image
        self.plot = plot


def search(text):
    results = []
    i = 1
    while (len(results) < 4 and i < 3) or (len(results) == 0 and i < 7):
        results = results + (search_page(text, i))
        i = i + 1
    return results


def search_page(text, page):
    url = config.get['search_movie_url'].format(config.get['API_Key'], text, page)
    request = requests.get(url=url, params=config.get['PARAMS'])
    results = json.loads(json.dumps(request.json()['results']))
    results_with_keywords = map(lambda m: add_keywords(m), results)
    relevant_results = list(filter(is_movie_relevant, results_with_keywords))
    return list(map(dict_to_object, relevant_results))


def add_keywords(movie):
    url = config.get['movie_keywords_url'].format(movie['id'], config.get['API_Key'])
    r = requests.get(url=url, params=config.get['PARAMS'])
    movie['keywords'] = json.loads(json.dumps(r.json()['keywords']))
    return movie


def is_movie_relevant(movie):
    if any(s in movie['keywords'] for s in config.relevant_keywords_tier1):
        return True
    contained_secondary_keywords = list(filter(lambda s: s in movie['keywords'], config.relevant_keywords_tier2))
    if len(contained_secondary_keywords) > 1:
        return True
    return False


def get_movie(movie_id):
    url = config.get['get_movie_url'].format(movie_id, config.get['API_Key'])
    request = requests.get(url=url, params=config.get['PARAMS'])
    result = json.loads(json.dumps(request.json()))
    return dict_to_object(result)


def dict_to_object(movie):
    return MovieResult(movie['id'], movie['title'], "Movie", "https://www.themoviedb.org/t/p/w1280" + movie['poster_path'],
                       movie['overview'])