




import os
try:
    import certifi
except ImportError:
    certifi = None


def where():

    if certifi:
        return certifi.where()
    else:
        f = os.path.split(__file__)[0]
        return os.path.join(f, 'cacert.pem')

if __name__ == '__main__':
    print(where())
