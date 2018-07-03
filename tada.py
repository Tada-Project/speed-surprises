"""Run doubling experiments and 'Tada'! get the time complexity"""

import subprocess


def run_command(command):
    """Run a command and return the output and error code"""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error


if __name__ == "__main__":
    # setup parameters of simple doubling experiment
    size = 100
    factor = 2
    size_stop = 400
    # perform the small doubling experiment
    while size <= size_stop:
        print("Start running experiment for size " + str(size) + "...")
        current_output, current_error = run_command("python3 perf_copies_ofc.py")
        print(current_output)
        print(current_error)
        print("... Done running experiment for size " + str(size))
        size = size * 2
