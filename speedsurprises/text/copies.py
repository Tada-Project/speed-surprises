"""Functions that create copies of characters and strings."""

# Source and/or inspiration for function(s):
# http://whatcanbecomputed.com/

LETTER_C = "C"

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.text.copies --function=mcopies_ofc --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 2.6645809936523435e-06 |   2.561279296875e-06   |         0          |
# |  50  | 4.4364535522460934e-06 | 4.431591796874999e-06  | 1.6649723025176437 |
# | 100  | 7.979669494628906e-06  | 7.944918823242185e-06  | 1.7986595375463692 |
# | 200  | 1.5205923461914064e-05 | 1.516878662109375e-05  | 1.905583116211659  |
# | 400  | 3.296632120768229e-05  | 3.1434313964843745e-05 | 2.167992051929782  |
# | 800  | 6.485352213541666e-05  |   6.460771484375e-05   | 1.9672659781129462 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def mcopies_ofc(input_string):
    """Create copy_count (number in input_string) copies of the letter 'C'."""
    copy_count = int(input_string)
    list_of_letter_c = []
    # iterate copy_count times, appending a 'C' character at each iteration
    # pylint: disable=unused-variable
    for i in range(copy_count):
        list_of_letter_c.append(LETTER_C)
    # join all the C's together into a single string, with no separator
    return "".join(list_of_letter_c)


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.text.copies --function=mcop ies_of --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_char.json --startsize=25 --max=1 000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  |  2.65678347269694e-06  | 2.614089202880859e-06  |         0          |
# |  50  | 4.683578389485677e-06  | 4.8348190307617194e-06 | 1.7628754611045918 |
# | 100  | 9.260162658691406e-06  | 9.220468139648435e-06  | 1.9771554757105931 |
# | 200  | 2.0233614705403645e-05 | 1.886336059570312e-05  | 2.1850172023072156 |
# | 400  | 0.0002457738899739583  | 0.00028976699218749997 | 12.146810817165619 |
# | 800  | 0.0008970620182291668  |   0.001037065234375    | 3.6499484071486097 |
# +------+------------------------+------------------------+--------------------+
# O(n^2) quadratic


def mcopies_of(input_string, character):
    """Create copy_count (number in input_string) copies of the character."""
    copy_count = int(input_string)
    list_of_letter = []
    # iterate copy_count times, appending a character at each iteration
    # pylint: disable=unused-variable
    for i in range(copy_count):
        list_of_letter.append(character)
    # join all the letters together into a single string, with no separator
    return "".join(list_of_letter)
