from cal import square

# start the first test:


def main():
    # test_square()
    '''def test_square():
        if square(2) != 4:
            print("2 squared was not 4")
        if square(3) != 9:
            print("3 squared was not 9")'''
   # test_square2()

    '''def test_square2():
        try:
            assert square(2) == 2
            assert square(3) == 9
        except AssertionError:
            print(" some tests are failed using the function square()")'''

# pytest is used


def test_positives():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


if __name__ == "__main__":
    main()
