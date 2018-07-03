"""Benchmarks with perf for the functions in the copies module"""

import perf

from speedsurprises.text import copies


def bench_copy_function(copy_function, chosen_size):
    """Run a benchmark"""
    copy_function(chosen_size)


# Example of calling the function:
# copied_character_string = copies.mcopies_ofc(copies_as_string)

# Idea: imagine calling this iteratively multiple times with larger
# inputs (size by doubling experiment and data by hypothesis)


if __name__ == "__main__":
    # configure perf
    runner = perf.Runner()
    # setup parameters of simple doubling experiment
    size = 100
    factor = 2
    size_stop = 1600
    # perform the small doubling experiment
    while size <= size_stop:
        print("Start running experiment for size " + str(size) + "...")
        experiment_name = "mcopies_ofc" + str(size)
        runner.metadata["description"] = experiment_name
        benchmark = runner.bench_func(
            "mcopies", bench_copy_function, copies.mcopies_ofc, size
        )
        time.sleep(2)
        benchmark.dump(
            "results/" + experiment_name + ".json", compact=False, replace=True
        )
        size = size * 2
        print("... Done running experiment for size " + str(size))
