def first_half(a_string):
    half_str = len(a_string) // 2
    if len(a_string) % 2 == 0: #even number
        return a_string[0:half_str]
    else:
        return a_string[0: half_str+1]

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'
