from byotest import assert_equal

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]


def get_change(amount, coins=eur_coins):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change

assert_equal(get_change(0), [])
assert_equal(get_change(1), [1])
assert_equal(get_change(2), [2])
assert_equal(get_change(5), [5])
assert_equal(get_change(10), [10])
assert_equal(get_change(20), [20])
assert_equal(get_change(50), [50])
assert_equal(get_change(100), [100])

assert_equal(get_change(3), [2, 1])
assert_equal(get_change(7), [5, 2])
assert_equal(get_change(9), [5, 2, 2])

assert_equal(get_change(35), [20, 10, 5])
assert_equal(get_change(35, usd_coins), [25, 10])

print("All tests pass!")
