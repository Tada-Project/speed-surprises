"""Perform an append with nested data structures."""

# append is O(1)

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=single_nested_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_list_of_list.json --startsize=50 --max=1000 --level 1 --position 0 0 0

# Quit due to reaching max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.9576860758463542e-05 | 2.857889404296875e-05  |         0          |
# | 100  | 6.247991780598958e-05  |  5.6762744140625e-05   | 2.112459409273538  |
# | 200  | 0.0001277647119140625  | 0.00011244672851562504 | 2.0448924454541206 |
# | 400  |   0.0002369446484375   | 0.00022073134765624998 | 1.8545390576771656 |
# | 800  | 0.0004947792317708334  | 0.00044429726562500004 | 2.0881637759434084 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=single_nested_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_list_of_list.json --startsize=50 --max=800 --log --level 2 --position 0 0 0

# Quit due to reached max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 5.193517496744792e-05  | 4.6323498535156255e-05 |         0          |
# | 100  | 9.915232991536459e-05  | 9.046301269531248e-05  | 1.9091555959426645 |
# | 200  | 0.00019504392903645833 | 0.00017901874999999996 | 1.967113926651505  |
# | 400  |  0.00036019759765625   |  0.00034900478515625   | 1.846751136708903  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
# Hypothesis crashed at 800, generates too many data
# hypothesis.errors.Unsatisfiable: Unable to satisfy assumptions of hypothesis store_global.
# You can add @seed(136063654759816880798066148671082908938) to this test to reproduce this failure.

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=single_nested_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_list_of_list.json --startsize=50 --max=800 --log --level 3 --position 0 0 0
# Quit due to reached max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.514886189778646e-05  | 2.3533679199218745e-05 |         0          |
# | 100  | 4.557787394205729e-05  | 4.4867907714843736e-05 | 1.812323520933126  |
# | 200  | 9.110090413411459e-05  | 8.574645996093752e-05  | 1.9987967023194253 |
# | 400  | 0.00016872017903645834 | 0.00016799194335937503 | 1.8520143201660897 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def single_nested_append(nested):
    """Append a value to a list of lists of lists."""
    res = []
    for item in nested:
        res.append(item)
        for subitem in item:
            res.append(subitem)
            for num in subitem:
                res.append(num)


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=double_nested_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/double_list_of_list_of_list.json --startsize=50 --max=700 --log --level=2 --position 1 1 1

# Quit due to reached max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 4.837522094726562e-05  | 4.810449218750001e-05  |         0          |
# | 100  | 9.918508219401042e-05  |  9.22799072265625e-05  | 2.050328251774461  |
# | 200  | 0.0001881338134765625  | 0.00018106108398437495 | 1.8967954587017877 |
# | 400  | 0.00036657145182291664 | 0.0003518763671874999  | 1.9484612842793605 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic

def double_nested_append(nested1, nested2):
    """Perform an append for a double list of list list of lists structure."""
    res = []
    for item1 in nested1:
        res.append(item1)
        for subitem1 in item1:
            res.append(subitem1)
            for num1 in subitem1:
                res.append(num1)
    for item2 in nested2:
        res.append(item2)
        for subitem2 in item2:
            res.append(subitem2)
            for num2 in subitem2:
                res.append(num2)


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=append_list_of_two_lists --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_double_list_of_double_list.json --startsize=50 --max=1000 --log --level=3 --position 0 0 0

# Quit due to indicator:  0.020567897394309233
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 6.532128779093425e-07 |  6.43624687194824e-07 |         0          |
# | 100  | 6.806475830078125e-07 | 6.400806427001952e-07 | 1.0419996390553061 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=append_list_of_two_lists --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_double_list_of_double_list.json --startsize=50 --max=1000 --log --level=3 --position 0 0 1

# Quit due to indicator:  0.061993304220029744
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 6.947120857238769e-07 | 6.481122970581054e-07 |         0          |
# | 100  | 7.865397834777832e-07 | 6.543621063232421e-07 | 1.1321809417756474 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=append_list_of_two_lists --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_double_list_of_double_list.json --startsize=50 --max=1000 --log --level=3 --position 0 1 0
# Quit due to indicator:  0.001325059786719021
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 6.402162869771322e-07 | 6.400392532348633e-07 |         0          |
# | 100  | 6.419151878356934e-07 | 6.404048919677734e-07 | 1.0026536357995246 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.nested.basic_nested --function=append_list_of_two_lists --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_of_double_list_of_double_list.json --startsize=50 --max=1000 --log --level=3 --position 0 1 1

# Quit due to indicator:  0.004662021849348527
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 7.129557673136393e-07 | 6.481370925903321e-07 |         0          |
# | 100  | 7.063389841715496e-07 | 6.462240219116213e-07 | 0.9907192234841984 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

def append_list_of_two_lists(nested):
    """Perform an append for a list of doubly nested lists."""
    res = []
    for item in nested:
        for thelist in item:
            res.append(list)
