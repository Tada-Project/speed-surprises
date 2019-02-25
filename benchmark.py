""" Main file for Speed-Surprises Benchmarking Tool. """

import getopt
from speedsurprises.numbers import factorial
import sys
import time

input_size_start = 100
input_growth_factor = 2
previous_time = 1

def get_num_of_rounds():
    """Recieves user-inputted number of rounds for experiment."""
    user_rounds = int(input("Please specify a number of rounds: "))
    return user_rounds


def main(argv):
    directory = ""
    module = ""
    function = ""
    type = ""

    try:
        opts, args = getopt.getopt(argv, "d:m:f:t:h", ["directory=", "module=", "function=", "type=", "help"])
    except getopt.GetoptError:
        print("Incorrect Format!")
        print("benchmark.py -d <directory> -m <module> -f <function> -t <type>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("benchmark.py -d <directory> -m <module> -f <function> -t <type>")
            sys.exit(2)
        elif opt in ("-d", "--directory"):
            directory = arg
        elif opt in ("-m", "--module"):
            module = arg
        elif opt in ("-f", "--function"):
            function = arg
        elif opt in ("-t", "--type"):
            type = arg
        else:
            print("benchmark.py -d <directory> -m <module> -f <function> -t <type>")

    print("***User Arguments***")
    print("Directory:", directory)
    print("Module:", module)
    print("Function:", function)
    print("Type:", type)

    function_call = module + "." + function + "(" + type + ")"

    run_benchmark(previous_time, function_call, function)


def run_benchmark(previous_time, function_call, function):
    print("************************************************")
    print("Running Benchmark with", function)

    user_rounds = get_num_of_rounds()
    round_num = 1
    current_size = input_size_start

    while(round_num <= user_rounds):
        current_size = current_size * input_growth_factor
        start_time = time.time()

        #factorial.compute_factorial(current_size)
        #run_function = locals()['factorial.compute_factorial'](current_size)
        exec('factorial.compute_factorial(current_size)')

        stop_time = time.time()
        time_elapsed = stop_time - start_time

        if(round_num == 1):
            avg_runtime = 0
        else:
            avg_runtime = time_elapsed / previous_time

        print("Round", round_num, " --- Size:", current_size, " --- ", time_elapsed, " --- AVG RUN: ", avg_runtime)
        previous_time = time_elapsed
        round_num += 1


if __name__ == "__main__":
   main(sys.argv[1:])
