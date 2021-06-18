#!/usr/bin/env python
from mpi4py import MPI


size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

print("Hello, World! I am process %d of %d on %s.\n"% (rank, size, name))
