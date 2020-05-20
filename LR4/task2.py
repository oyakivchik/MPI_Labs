from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    x = input()
    y = input()
    z = input()
    data = []
    data.append(x)
    data.append(y)
    data.append(z)
else:
    data = None
data = comm.bcast(data, root=0)
print(f"{rank}: {data}")
