"""Test for the one max problem with GA."""

from speedsurprises.genetic_algorithm import knapsack


def test_knapsack_with_input():
    """Test if knapsack function gives right result."""
    # example from DEAP
    items = [
        (8, 12.48509930835593),
        (10, 40.396096956847295),
        (1, 20.351113369770758),
        (5, 70.41144439033413),
        (4, 69.86574666158654),
        (3, 7.981206373372229),
        (7, 44.003630577221465),
        (1, 8.366591038506865),
        (1, 92.7646786450061),
        (3, 10.541265149933377),
        (1, 95.00359117156347),
        (5, 21.924990817330915),
        (4, 8.882167797500228),
        (1, 76.96797658382238),
        (7, 89.16384444665715),
        (5, 74.23923323846317),
        (9, 42.688343941286256),
        (9, 30.701913496381728),
        (6, 68.83604339265639),
        (9, 17.89634902035938),
    ]
    pop, stats, hof = knapsack.knapsack(items)
    assert len(pop) == 50
    assert stats != ""
    assert len(hof) == 22
