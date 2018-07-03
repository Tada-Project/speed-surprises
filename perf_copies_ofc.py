"""Benchmarks with perf for the functions in the copies module"""

import sys

import perf

from speedsurprises.text import copies


def bench_copy_function(copy_function, chosen_size):
    """Run a copy benchmark for a copy_function and a chosen_size"""
    copy_function(chosen_size)


# Example of calling the function:
# copied_character_string = copies.mcopies_ofc(copies_as_string)

# Idea: imagine calling this iteratively multiple times with larger
# inputs (chosen_size by doubling experiment and data by hypothesis)


if __name__ == "__main__":
    # Read the chosen_size
    filepath = "configuration.txt"
    with open(filepath) as fp:
        chosen_size = fp.readline().replace('\n', '')
    # configure perf
    runner = perf.Runner()
    # perform the small doubling experiment
    experiment_name = "mcopies_ofc" + str(chosen_size)
    runner.metadata["description"] = experiment_name
    benchmark = runner.bench_func(
        "mcopies", bench_copy_function, copies.mcopies_ofc, chosen_size
    )
    benchmark.dump("results/" + experiment_name + ".json", compact=False, replace=True)
    chosen_size = chosen_size * 2
