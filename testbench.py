""" Main file for Speed-Surprises Benchmarking Tool. """

from speedsurprises.numbers import factorial

import time # imports time for timing

input_size_start = 100
input_growth_factor = 2
previous_time = 1

def get_num_of_rounds():
    """Recieves user-inputted number of rounds for experiment."""
    user_rounds = int(input("Please specify a number of rounds: "))
    return user_rounds



def run_factorial(previous_time):
    user_rounds = get_num_of_rounds()
    round_num = 1
    current_size = input_size_start
    functionname = input("input the function name: ")


    while(round_num <= user_rounds):
        print("Running", functionname)
        current_size = current_size * input_growth_factor
        start_time = time.time()

        #factorial.compute_factorial(current_size)

        eval(functionname)

        stop_time = time.time()
        time_elapsed = stop_time - start_time

        if(round_num == 1):
            avg_runtime = 0
        else:
            avg_runtime = time_elapsed / previous_time

        print("Round", round_num, " --- Size:", current_size, " --- ", time_elapsed, " --- AVG RUN: ", avg_runtime)
        previous_time = time_elapsed
        round_num += 1

run_factorial(previous_time)
