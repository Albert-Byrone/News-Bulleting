# from app import app
import urllib.request,json
from .model import Articles,Sources

# News = news.News
# Sources = news.Sources
# Articles = news.Articles
#Getting the api KEY
api_key = None
article_url = None
source_url =None
base_url = None

def configure_request(app):
    global api_key,base_url,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['SOURCE_ARTICLE_URL']
    article_url = app.config['NEWS_ARTICLE_APL_URL']




#Getting the api base url

def get_sources(category):
    '''
    a function that get responses from the api
    '''
    get_source_url = source_url.format(category,api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        source_data = url.read()
        get_source_response = json.loads(source_data)

        sources_outcome = None

        if get_source_response['sources']:
            sources_outcome_list = get_source_response['sources']
            sources_outcome = process_new_sources(sources_outcome_list)

    return sources_outcome

def process_new_sources(sources_list):
    sources_outcome = []


    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')


        new_sources = Sources(id,name,description,url,category,country,language)
        sources_outcome.append(new_sources)

    return sources_outcome


def get_articles(article):

    get_article_url = article_url.format(article,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_response = None

        if article_response['articles']:
            article_response_list = article_response['articles']
            article_response = process_new_article(article_response_list)

    return article_response

def process_new_article(article_list):
    article_response = []

    for  article_item in article_list :
        title = article_item.get('title')
        author = article_item.get('author')
        source = article_item.get('source')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        new_article = Articles(title,author,source,description,url,urlToImage,publishedAt)
        article_response.append(new_article)
        
    return article_response


def article_source(source):
    sources_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(sources_url) as url:
        art_data = url.read()
        response = json.loads(art_data)

        source_article =  None

        if response['articles']:
            source_article_list = response['articles']
            source_article = process_article_source(source_article_list)

    return source_article

def process_article_source(article_list):
    article_source = []

    for one_art in article_list:
        source = one_art.get('source')
        author = one_art.get('author')
        title = one_art.get('title')
        description = one_art.get('description')
        url = one_art.get('url')
        urlToImage = one_art.get('urlToImage')
        publishedAt = one_art.get('publishedAt')


        article_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        article_source.append(article_object)

    return article_source

def search_article(article_name):
    search_article_url= article_url.format(article_name,api_key)

    with urllib.request.urlopen(search_article_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)
        

        search_result = None

        if search_response['articles']:
            all_search_result = search_response['articles']
            search_outcome =process_result(all_search_result)

    return search_outcome

 