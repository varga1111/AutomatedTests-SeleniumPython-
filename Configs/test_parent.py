import pytest

from testdata import Testdata

@pytest.mark.usefixtures("metadata")
class Parent_test(Testdata):
    

    pass


