import time
import random

from search import algorithms
from search import constants
from search import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(sorted(data_generator.get_random_list(size)))

    return [
        take_time_for_algorithm(samples, algorithms.linearSearch),
        take_time_for_algorithm(samples, algorithms.jumpSearch),
        take_time_for_algorithm(samples, algorithms.binarySearch),
        take_time_for_algorithm(samples, algorithms.ternarySearch),
    ]


"""
    Returns the median of the execution time measures for a searching approach given in 
"""


def take_time_for_algorithm(samples_array, searching_approach):
    times = []
    targets = []

    for sample in samples_array:
        targets.append(sample[-1])
        
    for i in range(len(samples_array)):
        start_time = time.time()
        searching_approach(samples_array[i].copy(), targets[i])
        times.append(constants.TIME_MULTIPLIER * (time.time() - start_time))

    times.sort()
    return times[len(times) // 2]
