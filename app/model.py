class Articles:
    '''
    A class that defines the article object
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Sources:
    def __init__(self,id,name,description,url,category,country,language):
        '''
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language
