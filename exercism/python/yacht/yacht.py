"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = lambda d: 50 if d.count(d[0]) == 5 else 0
ONES = lambda d: d.count(1)
TWOS = lambda d: d.count(2) * 2
THREES = lambda d: d.count(3) * 3
FOURS = lambda d: d.count(4) * 4
FIVES = lambda d: d.count(5) * 5
SIXES = lambda d: d.count(6) * 6
FULL_HOUSE = lambda d: sum(d) if len(set(d)) == 2 and (d.count(d[0]) == 2 or d.count(d[0]) == 3) else 0
FOUR_OF_A_KIND = lambda d: 4 * sorted(set(d))[-1]  if len(set(d)) <= 2 and (d.count(d[0]) <= 1 or d.count(d[0]) >= 4) else 0
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda d: 30 if sorted(d) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda d: sum(d)


def score(dice, category):
    return category(dice)
