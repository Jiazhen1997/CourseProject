from util.commons_util.logger_utils.timer import Timer

__author__ = 'Danyang'


def timestamp(func):
    
    def ret(*args):
        timer = Timer()
        timer.start()
        result = func(*args)
        print timer.end()
        return result
    return ret


def print_func_name(func):
    
    def ret(*args):
        print func.func_name
        result = func(*args)
        return result
    return ret
