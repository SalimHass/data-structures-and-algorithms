from data_structures_and_algorithms.validate_brackets import validate_brackets



def test_validate_true():
    actual = validate_brackets("[{}]")
    expected = True

    assert actual == expected

def test_validate_false():
    actual = validate_brackets("[{]")
    expected = False

    assert actual == expected


def test_validate_true2():
    actual = validate_brackets("[(coding)[]]")
    expected = True

    assert actual == expected