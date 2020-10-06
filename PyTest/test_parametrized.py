# https://www.youtube.com/watch?v=RC9ssdxmE08&list=PLFGoYjJG_fqoMMmCKLeLGQzh6Jz4CmO2Y&index=3&ab_channel=NaveenAutomationLabs
import pytest

@pytest.mark.parametrize("num, result",[(1,11),(2,22),(3,33),(4,44),(5,55)] )
def test_calculation(num, result):
    assert 11*num == result
    