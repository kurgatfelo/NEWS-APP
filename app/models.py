class Sources:
    """
    Sources class to define our sources objects.
    """
    def __init__(self, id, name, description, category, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.country = country


class Articles:
    """
    Articles class to define our articles objects.
    """
    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
