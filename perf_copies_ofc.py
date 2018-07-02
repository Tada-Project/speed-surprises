"""Benchmarks with perf for the mcopies_ofc function in the copies module"""

import os
import sys

import perf

import speedsurprises
from speedsurprises.text import copies


def bench_copies(copy_function, size):
    """Run a benchmark"""
    copy_function(size)


if __name__ == "__main__":
    runner = perf.Runner()
    runner.metadata["description"] = "Benchmark for the mcopies_ofc function"
    # Example of calling the function:
    # copied_character_string = copies.mcopies_ofc(copies_as_string)
    benchmark = runner.bench_func("mcopies", bench_copies, copies.mcopies_ofc, "1000")
    benchmark.dump("mcopies_ofc.json", compact=False, replace=True)
