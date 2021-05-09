from unittest import TestCase
from util.commons_util.fundamentals.generators import *
__author__ = 'Daniel'


class TestGenerator(TestCase):
    def test_coroutine(self):
        itr = first_coroutine()
        itr.next()  
        self.assertEquals(itr.send(1), "R"e"c"e"i"v"e"d":" "1"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""s""(""i""t""r"".""s""e""n""d""(""2"")"","" 