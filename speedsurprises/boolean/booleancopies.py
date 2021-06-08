"""Functions that create copies of boolean and booleanlists."""

Boolean_T = True

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.boolean.booleancopies --function=bcopies_oft --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 2.7212159729003907e-06 | 2.5887359619140627e-06 |         0          |
# |  50  | 5.621989491780599e-06  | 5.536944580078127e-06  | 2.065984305460488  |
# | 100  | 9.934102579752604e-06  | 9.585531616210938e-06  | 1.7670083863152635 |
# | 200  | 1.866694600423177e-05  |   1.838916015625e-05   | 1.8790772346440423 |
# | 400  | 3.989381062825521e-05  | 3.9436743164062495e-05 | 2.1371364453088004 |
# | 800  | 8.102415364583334e-05  | 8.066245117187499e-05  | 2.030995594801544  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def bcopies_oft(inputlength):
    """Create empty list for boolean true."""
    list_of_boolean_true = []
    # iterate length of inputlength times, appending a boolean true at each iteration
    # pylint: disable=unused-variable
    for i in range(int(inputlength)):
        list_of_boolean_true.append(Boolean_T)
    # return copied list
    return list_of_boolean_true


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.boolean.booleancopies --function=bcopies_of --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_boolean.json --startsize=25 --max=1000
# Quit due to researched max size

# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 2.3464551544189455e-06 | 2.152455902099609e-06  |         0          |
# |  50  | 3.825736490885417e-06  | 3.613996887207031e-06  | 1.6304323923176733 |
# | 100  | 7.327943522135417e-06  | 6.517599487304686e-06  | 1.9154334177468297 |
# | 200  | 1.3473921508789063e-05 | 1.2415991210937499e-05 | 1.838704333362911  |
# | 400  | 3.1770015869140626e-05 | 2.9370544433593746e-05 | 2.357889338186881  |
# | 800  | 6.507920735677084e-05  | 5.943293457031252e-05  | 2.048447429955005  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def bcopies_of(inputlength, boolean):
    """Create empty list for boolean true."""
    list_of_boolean_true = []
    # iterate length of inputlength times, appending a boolean true at each iteration
    # pylint: disable=unused-variable
    for i in range(int(inputlength)):
        list_of_boolean_true.append(boolean)
    # return copied list
    return list_of_boolean_true
