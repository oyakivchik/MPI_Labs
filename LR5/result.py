import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import subprocess
import os
import time
import socket
import sys
import multiprocessing

num_cpus = multiprocessing.cpu_count()
num_of_processes = [2, 10, 100, int(num_cpus/2), num_cpus]
num_of_processes.sort()
intervals = []
for entry in num_of_processes:
    TASK_OUTPUT = subprocess.run(["mpiexec", "-n", str(entry), "python3",
                                  "task.py"], stdout=subprocess.PIPE, universal_newlines=True).stdout
    TASK_ENTRIES = TASK_OUTPUT.split('\n')
    intervals.append(float(TASK_ENTRIES[1]))
print(intervals)
plt.figure(figsize=(20, 10))
plt.plot(num_of_processes, intervals)
plt.xticks(num_of_processes)
# plt.yticks(intervals)
plt.ylabel('Intervals')
plt.xlabel('Number of processes')
plt.savefig('plot.png')
plt.show()
