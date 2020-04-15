from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()

newGroup = comm.group.Excl([size-1])

newComm = comm.Create_group(newGroup)
if newComm != MPI.COMM_NULL:
    rank = comm.Get_rank()
    if rank == 0:
        data = "Hi, Parallel Programmer!"
    else:
        data = None
    data = comm.bcast(data, root=0)
    print(f"{rank}: {data}")
    MPI.Comm.Free(newComm)
MPI.Group.Free(newGroup)