"""Sample data generation functions."""
import random


def generate_dict_and_int(chosen_size):
    """Generate a dictionary and an int."""
    output = {k: random.random() for k in range(int(chosen_size))}
    return (output, random.random())
