from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

size1 = 8
size2 = 4

sequence = [6, 10, 2, 8, 9, 8, 3, 4, 10, 5, 1, 8, 4, 11, 4,
            8, 1, 2, 9, 1, 5, 10, 10, 7, 4, 8, 4, 10, 7, 5, 7, 2]

if rank == 0:
    data = []
    for i in range(size1):
        data.append([])
    for i in range(size1):
        for j in range(size2):
            data[i].append(sequence.pop(0))
            print(data[i][j], end=' ')
        print()
else:
    data = None

data = comm.scatter(data, root=0)
print(f"{rank}: {data}")
data = min(data)
print(f"{rank}: min_num = {data}")

data = comm.reduce(data, MPI.PROD, root=0)
if rank == 0:
    print(f"Data in process #{rank} is {data}")
else:
    assert data is None
