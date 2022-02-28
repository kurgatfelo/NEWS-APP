import urllib.request,json
from .models import Sources, Articles
from datetime import datetime

#Getting the api key
api_key = None

# Getting the source base url
sources_base_url = None

#Getting source articles base url
articles_base_url = None

def configure_request(app):
    global api_key, sources_base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['SOURCE_ARTICLES_BASE_URL']


def get_sources(category):
    """
    Function to get the json response to our url request
    """
    get_sources_url = sources_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results =process_results(sources_results_list)

    return sources_results

def process_results(sources_resulting_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    """
    sources_results = []
    for single_source in sources_resulting_list:
        id = single_source.get('id')
        name = single_source.get('name')
        description = single_source.get('description')
        category = single_source.get('category')
        url = single_source.get('url')
        country = single_source.get('country')

        source_object = Sources(id, name, description, category, url, country)
        sources_results.append(source_object)

    return sources_results

def get_articles(id):
    """
    Function to get the articles json response to our url request
    """
    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            source_articles_list = articles_response['articles']
            articles_results = process_articles_results(source_articles_list)

    return articles_results

def process_articles_results(articles_results_list):
    """
    Function that process the list of article from the request.
    """
    articles_results = []
    for single_article in articles_results_list:
        title = single_article.get('title')
        description = single_article.get('description')
        url = single_article.get('url')
        urlToImage = single_article.get('urlToImage')
        publishedAt = single_article.get('publishedAt')

        # convert date from json to string and backto my specific  format
        publishing_date = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
        date = publishing_date.strftime('%d.%m.%Y')


        article_object = Articles(title, description, url, urlToImage, date)
        articles_results.append(article_object)

    return articles_results