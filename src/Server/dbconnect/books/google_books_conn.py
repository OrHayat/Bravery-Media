import json
import requests
import Server.dbconnect.books.config as config


class BookResult:
    def __init__(self, id, title, type, image, plot, creator, score):
        self.id = id
        self.title = title
        self.type = type
        self.image = image
        self.plot = plot
        self.creator = creator
        self.score = score


def search(keyword):
    results = []
    for subject in config.get['subjects']:
        if len(results) == 0 or subject == "History / Holocaust":
            results = results + search_by_subject(keyword, subject)
        else:
            break
    list.sort(results, key=lambda b: b.score, reverse=True)
    return results


def search_by_subject(keyword, subject):
    if subject != "non":
        search_params = {'q': """{} subject:"{}" """.format(keyword, subject), 'maxResults': 40,
                         'key': config.get['google_api_key']}
    else:
        search_params = {'q': keyword, 'maxResults': 40, 'key': config.get['google_api_key']}
    request = requests.get(url=config.get['book_search_url'], params=search_params)
    r = request.json()
    if r['totalItems'] == 0:
        return []
    results = json.loads(json.dumps(r['items']))
    relevant_results = list(filter(is_result_relevant, results))
    score_results(relevant_results, keyword)
    return list(map(dict_to_obj, relevant_results))


def is_result_relevant(book):
    if 'description' in book['volumeInfo']:
        desc = book['volumeInfo']['description'].lower()
    elif 'subtitle' in book['volumeInfo']:
        desc = book['volumeInfo']['subtitle'].lower()
    else:
        return False
    if any(s in desc for s in config.relevant_keywords_tier1):
        return True
    contained_secondary_keywords = list(
        filter(lambda s: s in desc, config.relevant_keywords_tier2))
    if len(contained_secondary_keywords) > 1:
        return True
    return False


def score_results(books, keyword):
    for book in books:
        score = 0
        if keyword in book['volumeInfo']['title'].lower():
            score += 10
        if 'subtitle' in book['volumeInfo'] and keyword in book['volumeInfo']['subtitle'].lower():
            score += 4
        if 'description' in book['volumeInfo'] and keyword in book['volumeInfo']['description'].lower():
            score += 4
        if 'authors' in book['volumeInfo'] and keyword in (a.lower() for a in book['volumeInfo']['authors']):
            score += 9
        book['score'] = score


def dict_to_obj(book):
    authors = ""
    if 'authors' in book['volumeInfo']:
        for a in book['volumeInfo']['authors']:
            authors = "{}, {}".format(authors, a)
    if 'imageLinks' in book['volumeInfo']:
        image = book['volumeInfo']['imageLinks']['smallThumbnail'] if 'smallThumbnail' in book['volumeInfo'][
            'imageLinks'] else ""
    else:
        image = ""
    return BookResult(book['id'], book['volumeInfo']['title'], "Book", image,
                      book['volumeInfo']['description'], authors, book['score'])
