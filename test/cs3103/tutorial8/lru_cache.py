from functools import lru_cache
import math
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--size", "-s", type=int, required=True)
args = parser.parse_args()


@lru_cache(maxsize=args.size)
def used(_time: int):
    # print(f'sleep {_time}')
    return _time


# sleep_list = [2, 2, 3, 3, 4, 5, 2, 1]
# [time_sleep(item) for item in sleep_list]

trace_file = open(args.file)
trace = trace_file.read().splitlines()
for current_step in range(len(trace)):
    address = trace[current_step]
    used(address)
print(used.cache_info())
