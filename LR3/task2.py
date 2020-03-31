from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
sender = int
receiver = int
if rank == 0:
    sender = size-1
    receiver = rank+1
elif rank == size-1:
    sender = rank-1
    receiver = 0
else:
    sender = rank-1
    receiver = rank+1
comm.send(f"{rank}", dest=receiver)
while True:
    rec_message = comm.recv(source=sender)
    print(f"Process #{str(rank)}: {rec_message}\n\n\n\n--------------------------------------------------------\n\n\n\n")
    send_message = f"{rec_message},{rank}"
    comm.send(send_message, dest=receiver)
    