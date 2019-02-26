""" Main file for Speed-Surprises Benchmarking Tool. """

# Sample run: python3 benchmark.py -m speedsurprises.numbers.factorial -f compute_factorial -t int

# Imports:
import getopt
import importlib
import inspect
import sys
import time

# Set defaults:
input_size_start = 100
input_growth_factor = 2
previous_time = 1


def get_num_of_rounds():
    """Recieves user-inputted number of rounds for experiment."""
    user_rounds = int(input("Please specify a number of rounds: "))
    return user_rounds


def generate_data(current_size, type):
    """Generates data to be used in experiment."""
    if type == "int":
        # generate int
        exp_data = int(current_size)
    elif type == "list":
        # generate list
        default_list = [1]
        exp_data = default_list * current_size
    elif type == "string":
        # generate string
        default_string = "str"
        exp_data = default_string * current_size
    elif type == "char":
        # generate char
        default_char = "c"
        exp_data = default_char * current_size
    else:
        print("Unsupported data type")
    print(exp_data) # print what is being generated for testing
    return exp_data


def run_benchmark(previous_time, user_module, function, type):
    current_size = input_size_start

    print("************************************************")
    print("Running Benchmark with", function)
    run_function = getattr(user_module, function)

    user_rounds = get_num_of_rounds()
    round_num = 1

    test_list = [1]
    test_list2 = [1]
    while(round_num <= user_rounds):
        current_size = current_size * input_growth_factor

        current_data = generate_data(current_size, type)

        params = (data) # testing for the list

        start_time = time.time()

        run_function(data) # run the function with data size

        stop_time = time.time()
        time_elapsed = stop_time - start_time

        if(round_num == 1):
            avg_runtime = 0
        else:
            avg_runtime = time_elapsed / previous_time

        print("Round", round_num, " --- Size:", current_size, " --- ", time_elapsed, " --- AVG RUN: ", avg_runtime) # print results

        previous_time = time_elapsed
        round_num += 1


def main(argv):
    module = ""
    function = ""
    type = ""

    try:
        opts, args = getopt.getopt(argv, "m:f:t:h", ["module=", "function=", "type=", "help"])
    except getopt.GetoptError:
        print("Incorrect Format!")
        print("benchmark.py -m <module> -f <function> -t <type>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("benchmark.py -m <module> -f <function> -t <type>")
            sys.exit(2)
        elif opt in ("-m", "--module"):
            module = arg
        elif opt in ("-f", "--function"):
            function = arg
        elif opt in ("-t", "--type"):
            type = arg
        else:
            print("benchmark.py -m <module> -f <function> -t <type>")

    print("***User Arguments***")
    print("Module:", module)
    print("Function:", function)
    print("Type:", type)

    user_module = importlib.import_module(module)

    run_benchmark(previous_time, user_module, function, type)


if __name__ == "__main__":
   main(sys.argv[1:])
