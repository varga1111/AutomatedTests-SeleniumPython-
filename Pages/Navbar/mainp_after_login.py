import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests(SeleniumPython)/Configs')

from testdata import Testdata
from basemethods import Base_methods


class Mainp_after_login(Base_methods):

    def __init__(self, browser):
    
        super().__init__(browser)
        self.browser.get(Testdata.URL_AFTER_LOGIN)

    def get_title_after_login(self, title):
    
        return self.get_title(title)

