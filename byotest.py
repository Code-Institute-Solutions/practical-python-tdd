def assert_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def assert_not_equal(actual, unexpected):
    assert actual != unexpected, "Expected anything but {0}".format(actual)


def assert_is_in(collection, item):
    assert item in collection, "Expected {0} to contain {1}".format(
        collection, item)
