
import threading
__author__ = 'Daniel'


class Solution_unsafe:
    obj = None
    @classmethod
    def getInstance(cls):
        
        if not Solution.obj:
            Solution.obj = cls()
        return Solution.obj


class Solution:
    __lock = threading.Lock()
    __obj = None

    @classmethod
    def getInstance(cls):
        if not cls.__obj:
            with cls.__lock:
                if not cls.__obj:
                    cls.__obj = cls()

        return cls.__obj
