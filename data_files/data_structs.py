import json
import itertools

__author__ = 'Danyang'


class Sorter(object):
    @staticmethod
    def argsort(A, f=None):
        
        n = len(A)
        if f is None:
            f = lambda k: A[k]
        return sorted(range(n), key=f)


class ExcelColumn(object):
    def __init__(self):
        self.cur = None
        self.restore()

    def restore(self):
        self.cur = []

    def _plus(self, cur, idx):
        if idx>=len(cur):
            cur.append('a')
        elif cur[idx]<'z':
            cur[idx] = chr(ord(cur[idx])+1)
        else:
            cur[idx] = 'a'
            self._plus(cur, idx+1)

    def columns(self, n):
        
        self.restore()
        for i in xrange(n):
            self._plus(self.cur, 0)
            yield ''.join(reversed(self.cur))


class Displayer(object):
    @staticmethod
    def dump(obj):
        
        return json.dumps(obj, default=lambda o: o.__dict__)

    @staticmethod
    def display(obj):
        
        return str(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ': ')))


class Searcher(object):
    @staticmethod
    def binary_search(low, up, predicate):
        
        while low<up:
            m = (low+up)/2
            if predicate(m)<0:
                low = m+1
            elif predicate(m)>0:
                up = m
            else:
                return m
        return -1


class Wrapper(object):
    @staticmethod
    def to_dict(keys, values):
        
        return dict(itertools.izip(keys, values))

    @staticmethod
    def unpack(lst):
        
        return zip(*lst)
