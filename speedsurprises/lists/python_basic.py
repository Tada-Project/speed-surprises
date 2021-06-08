"""python default list functions"""

# https://wiki.python.org/moin/TimeComplexity

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.python_basic --function=list_copy --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000
# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 3.2364913676578555e-07 |  3.22893491745517e-07  |         0          |
# | 100  | 4.911724624635274e-07  | 4.900162143706838e-07  | 1.5176078248556337 |
# | 200  | 6.632680439632061e-07  | 6.627776565548346e-07  | 1.3503770969498479 |
# | 400  | 1.1246698706308724e-06 | 1.1228371047961733e-06 | 1.6956491133066889 |
# | 800  | 2.7629981994630365e-06 | 2.758518898009904e-06  | 2.456719319699709  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def list_copy(list):
    res = list.copy()
    return res


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.python_basic --function=list_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000
# Quit due to indicator:  0.004793372806200558
# +------+------------------------+------------------------+-------------------+
# | Size |          Mean          |         Median         |       Ratio       |
# +------+------------------------+------------------------+-------------------+
# |  50  | 2.5686807730998866e-07 | 2.5611526679970506e-07 |         0         |
# | 100  | 2.5934246689485414e-07 | 2.588452558517987e-07  | 1.009632919788158 |
# +------+------------------------+------------------------+-------------------+
# O(1) constant or O(logn) logarithmic


def list_append(list):
    print(list)
    res = []
    res.append(list)
    return res


# hypothesis will try generate empty list, which will cause error


def list_poplast(list):
    # print(list)
    list.pop()
    return list


# def list_popintermediate(list):
#     size = len(range(list))
#     res = list.pop(size)
#     return res


# tada --directory . --module speedsurprises.lists.python_basic \
#      --function list_in --types hypothesis \
#      --schema speedsurprises/jsonschema/list_and_int.json \
#      --log --startsize 50
# Quit due to exceeding the max time limit: 478.51705503463745
# +-----------------------------------------------------------------------------+
# |                list_in: O(n) linear or O(nlogn) linearithmic                |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 5.723192871729533e-07  | 6.681185903549194e-07  |         0          |
# | 100  | 1.015495890299479e-06  | 1.1431828041076649e-06 | 1.774352032264464  |
# | 200  | 2.0622932581583656e-06 | 2.1035167121887197e-06 | 2.030823834796787  |
# | 400  | 3.6632898279825847e-06 | 4.3830122375488295e-06 | 1.7763185781123652 |
# | 800  | 7.170516546344757e-06  | 9.591324890136719e-06  | 1.9573980992635904 |
# +------+------------------------+------------------------+--------------------+
def list_in(list, x):
    res = 0
    if x in list:
        res = 1
    return res


# tada --directory . --module speedsurprises.lists.python_basic \
#      --function dict_in --types hypothesis \
#      --schema speedsurprises/jsonschema/dict_and_int.json \
#      --log --startsize 50

# Quit due to indicator: 0.020965382063434217
# +-----------------------------------------------------------------------------+
# |                dict_in: O(1) constant or O(logn) logarithmic                |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.331694175402323e-07  | 2.3315152549743658e-07 |         0          |
# | 100  | 2.2359321444829305e-07 | 2.293726587295533e-07  | 0.9589302782802255 |
# +------+------------------------+------------------------+--------------------+

# tada --directory . --module speedsurprises.lists.python_basic \
#      --function dict_in --types custom \
#      --data_directory . \
#      --data_module speedsurprises.data_generation.custom_data_generation  \
#      --data_function generate_dict_and_int --startsize 50 --log --indicator 0.0001 --maxsize 6400
# Quit due to reaching max size: 6400
# +-----------------------------------------------------------------------------+
# |                dict_in: O(1) constant or O(logn) logarithmic                |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.3057441749572756e-07 | 2.2695994472503667e-07 |         0          |
# | 100  | 2.2558496786753337e-07 | 2.246794471740724e-07  | 0.9783607839829558 |
# | 200  | 2.264443063100179e-07  | 2.262993516921997e-07  | 1.0038093781274875 |
# | 400  | 2.248823666572571e-07  | 2.2364899444580066e-07 | 0.9931023231353743 |
# | 800  | 2.2710467341740926e-07 | 2.2731162738800045e-07 | 1.0098820854350896 |
# | 1600 | 2.2639746948877972e-07 | 2.2578625774383547e-07 | 0.9968860001074055 |
# | 3200 | 2.2807491916020713e-07 | 2.259561786651612e-07  | 1.0074093128126176 |
# +------+------------------------+------------------------+--------------------+
def dict_in(dict, x):
    res = 0
    if x in dict:
        res = 1
    return res


# tada --directory . --module speedsurprises.lists.python_basic \
#      --function dict_iterate_in --types hypothesis \
#      --schema speedsurprises/jsonschema/dict_and_int.json \
#      --log --startsize 50 --maxsize 200
# +----------------------------------------------------------------------------+
# |           dict_iterate_in: O(n) linear or O(nlogn) linearithmic            |
# +------+-----------------------+------------------------+--------------------+
# | Size |          Mean         |         Median         |       Ratio        |
# +------+-----------------------+------------------------+--------------------+
# |  50  | 2.146034294382731e-06 | 2.1284195175170893e-06 |         0          |
# | 100  | 3.909726494852702e-06 | 3.858912918090823e-06  | 1.8218378453161048 |
# +------+-----------------------+------------------------+--------------------+
# tada --directory . --module speedsurprises.lists.python_basic \
#      --function dict_iterate_in --types custom \
#      --data_directory . \
#      --data_module speedsurprises.data_generation.custom_data_generation  \
#      --data_function generate_dict_and_int --startsize 50 --log --maxsize 6400
# Quit due to exceeding the max time limit: 216.12506294250488
# +-----------------------------------------------------------------------------+
# |            dict_iterate_in: O(n) linear or O(nlogn) linearithmic            |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.609085034942627e-06  | 2.5874949569702137e-06 |         0          |
# | 100  | 4.7543861551920575e-06 | 4.736902969360352e-06  | 1.822242698692496  |
# | 200  | 9.061589477539062e-06  | 9.006818298339847e-06  | 1.9059430979629823 |
# | 400  |  1.79077449991862e-05  | 1.7699565612792972e-05 | 1.9762255886314513 |
# | 800  | 3.535039537760417e-05  | 3.521524963378906e-05  | 1.974028297767845  |
# | 1600 | 7.028248163248697e-05  | 6.956451074218749e-05  | 1.9881667766865663 |
# | 3200 | 0.0001466154940266927  | 0.00014004887255859378 | 2.086088746742858  |
# +------+------------------------+------------------------+--------------------+
def dict_iterate_in(dict, x):
    for k, _ in dict.items():
        if k == x:
            return True
    return False


# tada --directory . --module speedsurprises.lists.python_basic \
#      --function set_in make_set --types hypothesis \
#      --schema speedsurprises/jsonschema/list_and_int.json \
#      --log --startsize 50 --contrast
#
# At the greatest common size 800:
# Mean: set_in is 0.35% slower than make_set
# Median: set_in is 2.94% slower than make_set+------------------------------------------------------------------------------------------------+
# |             Contrast for set_in and make_set: O(1) constant or O(logn) logarithmic             |
# +---------+-------------------------------------+-------------------------------------+----------+
# |   Size  |                 Mean                |                Median               |  Ratio   |
# +---------+-------------------------------------+-------------------------------------+----------+
# |    50   |        1.3182056681315037e-08       |        1.7278144836426557e-08       |    0     |
# |   100   |        1.3046748250325515e-07       |        8.596386718750092e-08        |   1.0    |
# |   200   |         2.21897921244302e-08        |        4.474352264404307e-08        |   1.0    |
# |   400   |        2.9731409403483104e-07       |        5.106773071289006e-07        |   1.0    |
# |   800   |        4.321645609537532e-08        |        3.556418151855411e-07        |   1.0    |
# +---------+-------------------------------------+-------------------------------------+----------+

# tada --directory . --module speedsurprises.lists.python_basic \
#      --function set_in --types hypothesis \
#      --schema speedsurprises/jsonschema/list_and_int.json \
#      --log --startsize 50

# Quit due to reaching max size: 1500
# +-----------------------------------------------------------------------------+
# |                 set_in: O(1) constant or O(logn) logarithmic                |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 1.6363803606669108e-06 | 1.5881035919189457e-06 |         0          |
# | 100  | 2.8042603741963702e-06 | 2.919090576171875e-06  | 1.7136971584366163 |
# | 200  | 4.3429263056437175e-06 | 4.6028233032226525e-06 | 1.5486886829787658 |
# | 400  |  9.2377468170166e-06   |  9.5580735168457e-06   | 2.1270788788223203 |
# | 800  | 1.2620241599527994e-05 | 1.236202178955079e-05  | 1.3661601524173181 |
# +------+------------------------+------------------------+--------------------+
def set_in(input_lst, x):
    res = 0
    set_lst = set(input_lst)
    if x in set_lst:
        res = 1
    return res


# tada --directory . --module speedsurprises.lists.python_basic \
#      --function make_set --types hypothesis \
#      --schema speedsurprises/jsonschema/list_and_int.json \
#      --log --startsize 50

# Quit due to reaching max size: 1500
# +-----------------------------------------------------------------------------+
# |                make_set: O(n) linear or O(nlogn) linearithmic               |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 1.1569102081298828e-06 | 1.151319801330567e-06  |         0          |
# | 100  | 2.290835321299235e-06  | 2.2806309432983385e-06 | 1.9801323432026021 |
# | 200  | 3.3972589314778645e-06 | 3.3146266479492167e-06 | 1.4829782393747655 |
# | 400  | 7.861703441365558e-06  | 7.766165069580072e-06  | 2.314131362941354  |
# | 800  | 1.2422611956787111e-05 | 1.232102755737305e-05  | 1.5801425288346078 |
# +------+------------------------+------------------------+--------------------+
def make_set(input_lst, x):
    lst_set = set(input_lst)
    return lst_set
