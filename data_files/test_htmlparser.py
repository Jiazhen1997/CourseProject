

from bs4.testing import SoupTest, HTMLTreeBuilderSmokeTest
from bs4.builder import HTMLParserTreeBuilder

class HTMLParserTreeBuilderSmokeTest(SoupTest, HTMLTreeBuilderSmokeTest):

    @property
    def default_builder(self):
        return HTMLParserTreeBuilder()

    def test_namespaced_system_doctype(self):
        
        pass

    def test_namespaced_public_doctype(self):
        
        pass
