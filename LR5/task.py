from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

size1 = 1000
size2 = 1000


if rank == 0:
    matrix = []
    random.seed(1)
    for i in range(size1):
        matrix.append([])
    for i in range(size1):
        for j in range(size2):
            matrix[i].append(random.randrange(1, 101))
    parts = []
    for i in range(size):
        parts.append(int(size1/size))
    for i in range(size1 % size):
        parts[i] = parts[i]+1
    ranges = []
    index = 0
    for i in range(len(parts)):
        if i == 0:
            ranges.append(range(parts[i]))
            index = parts[i]
        else:
            ranges.append(range(index, index+parts[i]))
            index = index + parts[i]
    data = {'matrix': matrix, 'ranges': ranges}
else:
    data = None

data = comm.bcast(data, root=0)
start = time.time()
summary = 0
for i in data['ranges'][rank]:
    if i % 2 == 0:
        summary = summary + sum(data['matrix'][i])
summary = comm.reduce(summary, MPI.SUM, root=0)

if rank == 0:
    finish = time.time()
    interval = finish - start
    print(f"{summary}\n{interval}")
else:
    assert summary is None
