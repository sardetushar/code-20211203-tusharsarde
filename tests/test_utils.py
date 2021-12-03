from bmi.utils import get_square, get_count
import pytest
import pandas as pd

def test_get_square():
    # test getting count of dataframe col depending on value match
    test_date = ['tushar', 'sarde', 'data', 'engineer', 'tushar']
    test_df = pd.DataFrame(test_date, columns=['TestCol'])
    search_word = 'tushar'
    col_name = 'TestCol'
    count_occ = get_count(test_df, col_name, search_word)

    # tushar occurred 2 times in df
    expected = 2
    assert expected == count_occ

    # valid condition
    val = 4
    expected = 16
    test_call = get_square(val)
    assert expected == test_call

    # invalid condition
    with pytest.raises(TypeError) as inv_num:
        val = None
        get_square(val)
