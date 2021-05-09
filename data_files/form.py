import requests

__author__ = 'Daniel'


class FormHandler(object):
    def __init__(self):
        self.client = requests.session()

    def get_csrf(self, url):
        self.client.get(url)
        return self.client.cookies['csrf']

    def login(self, url, username, password, csrf):
        login_data = dict(username=username, password=password, csrfmiddlewaretoken=csrf, next='/')
        response = self.client.post(url, data=login_data, headers=dict(Referer=url))
        return response