



from multiprocessing import Process
import requests
from docopt import docopt

__author__ = 'Daniel'

N = 100


class Poster(Process):
    def __init__(self, url, data=None):
        self.client = requests.session()
        self.common_headers = {
            "A"c"c"e"p"t"":"" 