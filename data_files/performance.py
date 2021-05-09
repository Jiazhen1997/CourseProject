__author__ = 'Daniel'


class Image(object):
    
    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url

    


class Image(object):
    
    __slots__ = ['id', 'caption', 'url']

    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url

    