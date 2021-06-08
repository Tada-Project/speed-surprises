"""GA Knapsack example from DEAP."""

# Reference:
# https://github.com/DEAP/deap/blob/master/examples/ga/knapsack.py

#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import random
import numpy
from deap import algorithms, base, creator, tools

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.genetic_algorithm.knapsack --function=knapsack --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/double_int_list.json --startsize=50 --max=1000

# Quit due to indicator:  0.0990873786000493
# +------+---------------------+---------------------+--------------------+
# | Size |         Mean        |        Median       |       Ratio        |
# +------+---------------------+---------------------+--------------------+
# |  50  |  0.5215219102363335 |  0.5215180784871336 |         0          |
# | 100  | 0.31394614902092144 | 0.31344564599567093 | 0.6019807468465768 |
# | 200  |  0.2573390010657022 |  0.257054961490212  | 0.8196915358517523 |
# +------+---------------------+---------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def knapsack(knapsack_items):
    """Solve the 0-1 knapsack problem."""
    # pylint: disable=too-many-locals
    IND_INIT_SIZE = 5
    MAX_ITEM = 50
    MAX_WEIGHT = 50
    NBR_ITEMS = len(knapsack_items)

    # To assure reproductibility, the RNG seed is set prior to the items
    # dict initialization. It is also seeded in main().
    random.seed(64)

    # Create the item dictionary: item name is an integer, and value is
    # a (weight, value) 2-uple.
    items = {}
    # Create random items and store them in the items' dictionary.
    # for i in range(NBR_ITEMS):
    #     items[i] = (random.randint(1, 10), random.uniform(0, 100))

    for i, item in enumerate(knapsack_items):
        items[i] = item

    creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
    creator.create("Individual", set, fitness=creator.Fitness)

    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("attr_item", random.randrange, NBR_ITEMS)

    # Structure initializers
    toolbox.register(
        "individual",
        tools.initRepeat,
        creator.Individual,
        toolbox.attr_item,
        IND_INIT_SIZE,
    )
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def evalKnapsack(individual):
        weight = 0.0
        value = 0.0
        for item in individual:
            weight += items[item][0]
            value += items[item][1]
        if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
            return 10000, 0  # Ensure overweighted bags are dominated
        return weight, value

    def cxSet(ind1, ind2):
        """Apply a crossover operation on input sets.

        The first child is the intersection of the two sets,
        the second child is the difference of the two sets.
        """
        temp = set(ind1)  # Used in order to keep type
        ind1 &= ind2  # Intersection (inplace)
        ind2 ^= temp  # Symmetric Difference (inplace)
        return ind1, ind2

    def mutSet(individual):
        """Mutation that pops or add an element."""
        if random.random() < 0.5:
            if len(individual) > 0:  # We cannot pop from an empty set
                individual.remove(random.choice(sorted(tuple(individual))))
        else:
            individual.add(random.randrange(NBR_ITEMS))
        return (individual,)

    toolbox.register("evaluate", evalKnapsack)
    toolbox.register("mate", cxSet)
    toolbox.register("mutate", mutSet)
    toolbox.register("select", tools.selNSGA2)

    random.seed(64)
    NGEN = 50
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(
        pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats, halloffame=hof
    )

    return pop, stats, hof
