from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    message = "0"
    comm.send(message, dest=1)
    rec_message = comm.recv(source=size-1)
    print(f"{str(rank)}: {rec_message}")
elif (rank < size-1):
    message = comm.recv(source=rank-1)
    send_message = f"{message},{rank}"
    comm.send(send_message, dest=rank+1)
else:
    message = comm.recv(source=rank-1)
    send_message = f"{message},{rank}"
    comm.send(f"{message},{rank}", dest=0)
