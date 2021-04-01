get = {
    'search_movie_url': "https://api.themoviedb.org/3/search/movie?api_key={}&query={}&page={}",
    'get_movie_url': "https://api.themoviedb.org/3/movie/{}?api_key={}",
    'movie_keywords_url': "https://api.themoviedb.org/3/movie/{}/keywords?api_key={}",
    'API_Key': "735ba7d8abc892126da430a42173f953",
    'PARAMS': {'accept': "application/json"}
}

relevant_keywords_tier1 = [
    {
        "name": "holocaust (shoah)",
        "id": 1739
    },
    {
        "id": 1631,
        "name": "concentration camp"
    },
    {
        "name": "holocaust survivor",
        "id": 10939
    },
    {
        "name": "holocaust denial",
        "id": 259137
    },
    {
        "id": 2450,
        "name": "auschwitz-birkenau concentration camp"
    }
]

relevant_keywords_tier2 = [
    {
        "id": 1956,
        "name": "world war ii"
    },
    {
        "id": 2433,
        "name": "jew persecution"
    },
    {
        "id": 2394,
        "name": "ghetto"
    },
    {
        "name": "jewish ghetto",
        "id": 2444
    },
    {
        "name": "death camp",
        "id": 177913
    }
    ,
    {
        "name": "auschwitz",
        "id": 264089
    }
]