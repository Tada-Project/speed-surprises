"""Function that reverses strings."""

# Source and/or inspiration for function(s):
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.text.string_reverser --function=reverse --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/string.json --startsize=25 --max= 1000
# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 2.5298746744791665e-06 | 2.533021545410156e-06  |         0          |
# |  50  | 5.1293666585286455e-06 | 5.026287841796875e-06  | 2.0275180862801614 |
# | 100  | 1.0340181376139323e-05 | 1.0436883544921877e-05 | 2.015878775003656  |
# | 200  | 2.846676717122396e-05  | 2.7855419921875006e-05 | 2.753023968894102  |
# | 400  | 5.7691081542968755e-05 |  6.34750732421875e-05  | 2.026611634400362  |
# | 800  | 0.00014513589680989583 | 0.00014419794921874998 | 2.515742345752307  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
