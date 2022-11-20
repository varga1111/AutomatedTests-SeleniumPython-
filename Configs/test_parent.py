import pytest
from testdata import Testdata


#@pytest.mark.usefixtures('test_failed_check')
@pytest.mark.usefixtures("init_driver")
class Parent_test(Testdata):


    pass