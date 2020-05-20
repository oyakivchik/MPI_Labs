from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
sender = int
receiver = int
message = f"{rank}"
for i in range(0, size):
    if i == rank:
        pass
    else:
        comm.send(message, dest=i)

while True:
    for i in range(0, size):
        if i == rank:
            pass
        else:
            message = comm.recv(source=i)
            print(f"Process #{rank}: {message}")
            comm.send(f"{message},{rank}", dest=i)
