from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = "Hi, Parallel Programmer!"
else:
    data = None
data = comm.bcast(data, root=0)
print(f"{rank}: {data}")