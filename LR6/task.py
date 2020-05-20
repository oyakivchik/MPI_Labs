from mpi4py import MPI

data = [6, 10, 2, 8, 9, 8, 3, 4, 10, 5, 1, 8, 4, 11, 4,
        8, 1, 2, 9, 1, 5, 10, 10, 7, 4, 8, 4, 10, 7, 5, 7, 2]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = comm.scatter(data, root=0)


count = 32
group_size = 2
while(group_size <= count):
    groups_count = int(count / group_size)
    group = int(rank/group_size)
    direction = int(group % 2)
    rank_in_group = rank - group_size*group
    step = int(group_size / 2)
    if rank_in_group < step:
        comm.send(data, dest=rank+step)
        recv_data = comm.recv(source=rank+step)
        if (data > recv_data and direction == 0) or (data < recv_data and direction == 1):
            data = recv_data
    else:
        comm.send(data, dest=rank-step)
        recv_data = comm.recv(source=rank-step)
        if (data < recv_data and direction == 0) or (data > recv_data and direction == 1):
            data = recv_data
    flag = "Finished"
    for i in range(count):
        if i != rank:
            comm.send(flag, dest=i)
        else:
            pass
    for i in range(count):
        if i != rank:
            flag_recv = comm.recv(source=i)
        else:
            pass
    inner_count = group_size
    inner_rank = rank_in_group
    while (step > 2):
        inner_group_size = int(inner_count/2)
        inner_group = int(inner_rank/inner_group_size)
        step = int(inner_group_size/2)
        inner_rank_in_group = inner_rank - inner_group_size*inner_group
        if inner_rank_in_group < step:
            comm.send(data, dest=rank+step)
            recv_data = comm.recv(source=rank+step)
            if (data > recv_data and direction == 0) or (data < recv_data and direction == 1):
                data = recv_data
        else:
            comm.send(data, dest=rank-step)
            recv_data = comm.recv(source=rank-step)
            if (data < recv_data and direction == 0) or (data > recv_data and direction == 1):
                data = recv_data
        flag = "Finished"
        for i in range(count):
            if i != rank:
                comm.send(flag, dest=i)
            else:
                pass
        for i in range(count):
            if i != rank:
                flag_recv = comm.recv(source=i)
            else:
                pass
        inner_count = inner_group_size
        inner_rank = inner_rank_in_group
    for i in range(count):
        if i != rank:
            comm.send(flag, dest=i)
        else:
            pass
    for i in range(count):
        if i != rank:
            flag_recv = comm.recv(source=i)
        else:
            pass
    group_size=int(group_size*2)
print(f"{rank}: {data}")