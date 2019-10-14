import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SOURCE_ARTICLE_URL  = os.environ.get('SOURCE_ARTICLE_URL ')
    NEWS_ARTICLE_APL_URL  = os.environ.get('NEWS_ARTICLE_APL_URL ')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # NEWS_API_BASE_URL = 'https://newsap/i.org/v2/sources?country=ke&category={}&apiKey={}'
    # NEWS_ARTICLE_APL_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

   

class ProdConfig(Config):
    '''

    Production configuration child class

    Arg:
        Config: The parent configuration class with General configuration settings
    '''    
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Arg:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True



config_options={
    'development':DevConfig,
    'production':ProdConfig
}


    

