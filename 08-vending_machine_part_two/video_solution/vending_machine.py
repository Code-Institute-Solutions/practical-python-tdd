from byotest import *

usd_coins = [100, 50, 25, 10, 5, 2, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]


def get_change(amount, coins=eur_coins):
    """
    Takes the payment amount and returns the change

    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)

    Returns a list of coin values
    """
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change


#  Write our tests for our code
test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])

print("All tests pass!")