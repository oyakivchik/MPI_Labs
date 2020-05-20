from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if (size % 2 != 0):
    print("ERROR! Run  even number of processes!!!")
    exit
else:
    if (rank % 2 == 0):
        message = f"Hi, {rank+1} Processor!"
        comm.send(message, dest=rank+1)
    else:
        message = comm.recv(source=rank-1)
        print(message)
