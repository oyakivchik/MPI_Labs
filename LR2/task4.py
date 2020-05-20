from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if size != 2:
    print("ERROR! Run exactly 2 processes!!!")
    exit
if rank == 0:
    message = "Hi, Second Processor!"
    comm.send(message, dest=1)
elif rank == 1:
    message = comm.recv(source=0)
    print(message)
